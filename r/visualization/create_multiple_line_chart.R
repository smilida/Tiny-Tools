library(ggplot2)

stderror <- function(x) sd(x)/sqrt(length(x))

similarity_list <- list("99", "98", "97", "96", "95", "94", "93", "92", "91", "90", "85", "80", "75", "70")
color_list <- list("#E69F00", "#CC79A7", "#56B4E9", "#009E73", "#CC79A7", "#F0E442", "#999999","#0072B2","#D55E00")
plots_list <- list()

# Create a function to plot the data
plot_fun <- function(df, similarity) {
  ggplot(data=df,aes(x=order, y=x, color="#F0E442", group=1)) + 
        geom_line() + 
        geom_point() +
        geom_errorbar(aes(ymin=x-SEM, ymax=x+SEM), width=0.3) +
        ylab("Avg SP score") +
        ggtitle(similarity) + 
        theme(legend.position = "none")
}

for (i in 1:length(similarity_list)) {
  df <- read.csv("../fmri.csv", sep="\t")
  df <- data.frame(
    Dataset = rep(df$Dataset, 10),
    SP = c(df$ClustalW2, df$Dialign.TX, df$Kalign3, df$MAFFT, df$MUSCLE3, df$MUSCLE5, df$PCMA, df$POA, df$T.Coffee, df$Default),
    order = c(rep("ClustalW2", 42), rep("Dialign-TX", 42), rep("Kalign3", 42), rep("MAFFT", 42), rep("MUSCLE3", 42),
              rep("MUSCLE5", 42), rep("PCMA", 42), rep("POA", 42), rep("T-Coffee", 42), rep("Default", 42))
  )
  df <- df[df$Dataset == similarity_list[[i]], ]
  MEAN <- aggregate(df$SP, by=list(order=df$order), mean)
  SEM <- aggregate(df$SP, by=list(order=df$order), stderror)
  MEAN$SEM <- SEM$x
  plots_list[[i]] <- plot_fun(MEAN, similarity_list[[i]])
}

# Set font size
theme_set(theme_bw(base_size = 5))

# Create a grid of 14 plots
gridExtra::grid.arrange(grobs=plots_list, nrow = 5, ncol = 3)
