library(ggplot2)
library(GGally)


setwd("C:/Users/taesa/Desktop/Programing Assignments/AIT_580_FINAL/Data/K_streamlit")
df <- read.csv("./refined_insurance_discriptive Stats.csv")

ggpairs(df, ggplot2::aes(colour = smoker, alpha = 0.4),bins = 20)

