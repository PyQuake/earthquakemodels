setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/dataForR")
load("data.Rda")

resultANOVA = aov(finalData$loglikeValues~finalData$model+finalData$depths+finalData$years+finalData$regions)
summary(resultANOVA)
resultANOVA = aov(finalData$loglikeValues~finalData$model+finalData$depths+finalData$regions)
summary(resultANOVA)

tuk = TukeyHSD(resultANOVA)
op <- par(mar = c(5,14,4,2) + 0.1)
plot(tuk,las=1)
print(tuk)
