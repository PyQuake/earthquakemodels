setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/DataFromR")
load("TESTEdata.Rda")
summary(finalData)
resultANOVA = aov(loglikeValues~model+depths+years+regions , data = finalData)
summary(resultANOVA)
tuk = TukeyHSD(resultANOVA)
op <- par(mar = c(5,15,4,2) + 0.1)
plot(tuk,las=1)
print(tuk)

resultANOVA = aov(loglikeValues~model+depths , data = finalData)
summary(resultANOVA)
tuk = TukeyHSD(resultANOVA)
op <- par(mar = c(5,15,4,2) + 0.1)
plot(tuk,las=1)
print(tuk)

# subtabela para testar se clustered faz diferenca
# pq se eu usar so uma regiao eu chego a essa conclusao usando a versao paired???
subTabela = finalData[finalData$regions=='Kansai',]

# "gaModel"            "lista"  "hybrid_gaModel"  "hybrid_listaGA_New" "gaModelCluster"     "listaCluster"
t.test(finalData$model=='gaModel', finalData$model=='lista', paired = T)
t.test(finalData$model=='gaModel', finalData$model=='hybrid_gaModel', paired = T)
t.test(finalData$model=='gaModel', finalData$model=='hybrid_listaGA_New', paired = T)
t.test(finalData$model=='gaModel', finalData$model=='gaModelCluster', paired = T)
t.test(finalData$model=='gaModel', finalData$model=='listaCluster', paired = T)

t.test(finalData$model=='lista', finalData$model=='gaModel', paired = T)
t.test(finalData$model=='lista', finalData$model=='hybrid_gaModel', paired = T)
t.test(finalData$model=='lista', finalData$model=='hybrid_listaGA_New', paired = T)
t.test(finalData$model=='lista', finalData$model=='gaModelCluster', paired = T)
t.test(finalData$model=='lista', finalData$model=='listaCluster', paired = T)

t.test(finalData$model=='hybrid_gaModel', finalData$model=='lista', paired = T)
t.test(finalData$model=='hybrid_gaModel', finalData$model=='gaModel', paired = T)
t.test(finalData$model=='hybrid_gaModel', finalData$model=='hybrid_listaGA_New', paired = T)
t.test(finalData$model=='hybrid_gaModel', finalData$model=='gaModelCluster', paired = T)
t.test(finalData$model=='hybrid_gaModel', finalData$model=='listaCluster', paired = T)

t.test(finalData$model=='hybrid_listaGA_New', finalData$model=='lista', paired = T)
t.test(finalData$model=='hybrid_listaGA_New', finalData$model=='gaModel', paired = T)
t.test(finalData$model=='hybrid_listaGA_New', finalData$model=='hybrid_gaModel', paired = T)
t.test(finalData$model=='hybrid_listaGA_New', finalData$model=='gaModelCluster', paired = T)
t.test(finalData$model=='hybrid_listaGA_New', finalData$model=='listaCluster', paired = T)

t.test(finalData$model=='gaModelCluster', finalData$model=='lista', paired = T)
t.test(finalData$model=='gaModelCluster', finalData$model=='gaModel', paired = T)
t.test(finalData$model=='gaModelCluster', finalData$model=='hybrid_gaModel', paired = T)
t.test(finalData$model=='gaModelCluster', finalData$model=='hybrid_listaGA_New', paired = T)
t.test(finalData$model=='gaModelCluster', finalData$model=='listaCluster', paired = T)

t.test(finalData$model=='listaCluster', finalData$model=='lista', paired = T)
t.test(finalData$model=='listaCluster', finalData$model=='gaModel', paired = T)
t.test(finalData$model=='listaCluster', finalData$model=='hybrid_gaModel', paired = T)
t.test(finalData$model=='listaCluster', finalData$model=='hybrid_listaGA_New', paired = T)
t.test(finalData$model=='listaCluster', finalData$model=='gaModelCluster', paired = T)

subTabela = finalData[finalData$model=='gaModelCluster'|finalData$model=='listaCluster',]
head(subTabela)
summary(subTabela)
resultANOVA = aov(loglikeValues~model+depths+years+regions , data = subTabela)
tuk = TukeyHSD(resultANOVA)
op <- par(mar = c(5,15,4,2) + 0.1)
plot(tuk,las=1)
print(tuk)
