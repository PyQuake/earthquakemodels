setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/dataFromR")
load("newdata.Rda")
summary(finalData)
resultANOVA = aov(loglikeValues~model+depths+years+regions , data = finalData)
summary(resultANOVA)
tuk = TukeyHSD(resultANOVA)
op <- par(mar = c(1,24,4,2) + 0.1)
plot(tuk,las=1)

subTabela = finalData[finalData$model=='EMP-GAModelWindow'|finalData$model=='GAModelWindow'|
                          finalData$model=='EMP-ReducedGAModelWindow'|finalData$model=='ReducedGAModelWindow'|
                          finalData$model=='EMP-GAModelSLC'|finalData$model=='GAModelSLC'|
                          finalData$model=='EMP-ReducedGAModelSLC'|finalData$model=='ReducedGAModelSLC',]
summary(subTabela)

resultANOVA = aov(loglikeValues~model+years+regions+depths , data = subTabela)
summary(resultANOVA)
tuk = TukeyHSD(resultANOVA)
op <- par(mar = c(5,24,4,2) + 0.1)
plot(tuk,las=1)

subTabela2 = finalData[finalData$depth==25,]
summary(subTabela2)

resultANOVA = aov(loglikeValues~model+years+regions , data = subTabela2)
summary(resultANOVA)
tuk = TukeyHSD(resultANOVA)
op <- par(mar = c(1,24,4,2) + 0.1)
plot(tuk,las=1)
