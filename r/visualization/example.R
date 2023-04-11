# Author      : zhai1xiao
# Date        : 2023-04-11
# Function    : create boxplot with scattered plot together
# Instructions: Rscript boxplot_with_scattered.R

# read data
df <- read.csv("../fmri.csv", sep="\t")
head(df)
str(df)
MEAN <- aggregate(df$SP.score, by=list(order=df$order), mean)
SD <- aggregate(df$SP.score, by=list(order=df$order), sd)
MEAN$SD <- SD$x
MEAN

# import ggplot2
library(ggplot2)


# box plot
box <- ggplot(df, aes(x=order, y=SP.score, color=order)) + geom_boxplot() + theme_bw()
box
# # scatter plot 
scatter <- ggplot(df, aes(x=order, y=SP.score, color=order)) + geom_jitter() + theme_bw()
scatter
# # violin plot 
violin <- ggplot(df, aes(x=order, y=SP.score, color=order)) + geom_violin() + theme_bw()
violin

# combine the three plots(boxplot, scatter plot, bar plot)
cbPalette <- c("#E69F00", "#CC79A7", "#56B4E9", "#009E73", "#CC79A7", "#F0E442", "#999999","#0072B2","#D55E00")
ggplot(data=df,aes(x=order, y=SP.score, color=order))+
        geom_point(alpha=0.2,
                   position=position_jitterdodge(jitter.width = 0.35, 
                                                    jitter.height = 0, 
                                                    dodge.width = 0.8))+
        geom_boxplot(alpha=0.2,width=0.45,
                    position=position_dodge(width=0.8),
                    linewidth=0.75,outlier.colour = NA)+
        geom_bar(data=MEAN, aes(order,x), stat="identity", alpha=0) +
        # geom_errorbar(aes(ymin=x-SD, ymax=x+SD)) +
        scale_color_manual(values = cbPalette)+
        theme_classic() +
        theme(legend.position="none") + 
        theme(text = element_text(size=16)) + 
        # ylim(1000,4000) +
        ylab("Avg SP score")

