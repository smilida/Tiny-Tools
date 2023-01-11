# Author  : zhai1xiao
# Date    : 2023-01-12
# Function: Use seaborn draw Boxplot
# Taken from
# https://medium.com/save-the-data/beautiful-beginner-box-plots-in-python-3e380eff4a4b

import pandas as pd
import seaborn as sns

# basic use
def boxplot_basic():
    raw_data = "fmri.csv"
    mri = pd.read_csv(raw_data)
    print(mri.head())
    # box plot
    b = sns.boxplot(data = mri, 
                    x = "region", 
                    y = "signal")
    # add the raw data dots
    b = sns.stripplot(data = mri, 
                        x = "region", 
                        y = "signal", 
                        color = "black")
    # save the plot
    b = b.get_figure()
    b.savefig("testBoxplot.png", dpi=200)

# advanced use
def boxplot_advanced():
    raw_data = "fmri.csv"
    mri = pd.read_csv(raw_data)
    print(mri.head())
    # change the seaborn's style settings
    sns.set(style="ticks",                     # The 'ticks' style
            rc={"figure.figsize": (6, 9),      # width = 6, height = 9
                "figure.facecolor": "ivory",   # Figure colour
                "axes.facecolor": "ivory"})    # Axes colour
    # box plot
    b = sns.boxplot(data = mri,           
                    x = "region",        # x axis column from data
                    y = "signal",        # y axis column from data
                    width = 0.4,         # The width of the boxes
                    color = "skyblue",   # Box colour
                    linewidth = 2,       # Thickness of the box lines
                    showfliers = False)  # Sop showing the fliers
    # strip plot
    b = sns.stripplot(data = mri,          
                      x = "region",      # x axis column from data
                      y = "signal",      # y axis column from data
                      color = "crimson", # Colours the dots
                      linewidth = 1,     # Dot outline width
                      alpha = 0.4)       # Makes them transparent
    # Set the y axis and font size
    b.set_ylabel("Signal", fontsize = 14)
    # Set the x axis label and font size
    b.set_xlabel("Region", fontsize = 14)
    # Set the plot title and font size
    b.set_title("FMRI signal by region", fontsize = 16)
    # Remove axis spines
    sns.despine(offset = 5, trim = True)
    # save the plot
    b = b.get_figure()
    b.savefig("testBoxplot.png", dpi=200)

if __name__ == '__main__':
    boxplot_advanced()
