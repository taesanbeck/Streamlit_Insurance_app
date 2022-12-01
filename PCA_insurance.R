setwd("C:/Users/taesa/Documents/STAT 515/Final")

data <- read.csv("Scooter Price Prediction.csv")

names(data)[2] <- "PRICE"
names(data)[3] <- "RANGE"
names(data)[4] <- "WEIGHT"
names(data)[5] <- "TOP_SPEED"
names(data)[6] <- "WEIGHT_CAPACITY"

data =  na.omit(data)

df <- data[ -c(1,7) ]

df

names(df)[1] <- "PRICE"
names(df)[2] <- "RANGE"
names(df)[3] <- "WEIGHT"
names(df)[4] <- "TOP_SPEED"
names(df)[5] <- "WEIGHT_CAPACITY"

library(psych)

summary(df)

pairs.panels(df[],
             gap = 0,
             bg = c("red", "yellow", "blue")[df$PRICE],
             pch=21)

pc <- prcomp(df[-5],
             center = TRUE,
             scale = TRUE)

attributes(pc)

pc$scale

print(pc)

summary(pc)


pairs.panels(pc$x,
             gap=0,
             bg = c("red", "yellow", "blue")[df$PRICE],
             pch=21)


library(devtools)
#install_github("vqv/ggbiplot")
library(ggbiplot)
g <- ggbiplot(pc,
              obs.scale = 1,
              var.scale = 1,
              groups = data$stage,  #this has to be categorical 
              ellipse = TRUE,
              circle = TRUE,
              ellipse.prob = 0.7) # includes 70% of dots
g <- g + scale_color_discrete(name = '')
g <- g + theme(legend.direction = 'horizontal',
               legend.position = 'top')
print(g)
