setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/dataFromR")
load("newdata.Rda")
summary(finalData)
resultANOVA = aov(loglikeValues~model+depths+years+regions , data = finalData)
summary(resultANOVA)
tuk = TukeyHSD(resultANOVA)
# op <- par(mar = c(1,24,3,2) + 1.0)
plot(tuk,las=1)
levels(unique(finalData$model))
subTabela = finalData[c(which(finalData$depths==25)),]

subTabela = subTabela[c(which(subTabela$model=='EMP-GAModelWindow'|subTabela$model=='GAModelWindow'|
                                  subTabela$model=='EMP-ReducedGAModelWindow'|subTabela$model=='ReducedGAModelWindow'|
                                  subTabela$model=='EMP-GAModelSLC'|subTabela$model=='GAModelSLC'|
                                  subTabela$model=='EMP-ReducedGAModelSLC'|subTabela$model=='ReducedGAModelSLC')),]

summary(subTabela)

resultANOVA = aov(loglikeValues~model+years+regions , data = subTabela)
summary(resultANOVA)
tuk = TukeyHSD(resultANOVA)
# op <- par(mar = c(1,8,3,2) + 1.0)
op <- par(mar = c(1,24,3,2) + 1.0)
print(plot(tuk,las=1))

# gamodel sempre ganha
subTabela2 = subTabela[c(which(subTabela$model=='EMP-GAModelWindow'|subTabela$model=='GAModelWindow'|
                                   subTabela$model=='EMP-GAModelSLC'|subTabela$model=='GAModelSLC')),]

summary(subTabela2)
resultANOVA = aov(loglikeValues~model+years+regions , data = subTabela2)
summary(resultANOVA)
tuk = TukeyHSD(resultANOVA)
op <- par(mar = c(1,24,3,2) + 1.0)
print(plot(tuk,las=1))


# Summarize the n=30 repeated measures on each Problem:Algorithm combination by their mean value
ttestPaired= function(region){
    subTabela3 = subTabela2[subTabela2$regions==region,]
    aggfinaldata<-aggregate(loglikeValues~years:model, data=subTabela3,FUN=mean)
    summary(aggfinaldata)
    # Perform paired t-test
    cat(mean(aggfinaldata$loglikeValues[1:6]), mean(aggfinaldata$loglikeValues[7:12]))
    cat('in', region, 'the t.test between the models EMP-GAModelWindow and EMP-GAModelSLC is: ')
    difTimes<-with(aggfinaldata,loglikeValues[1:6]-loglikeValues[7:12])
    print(t.test(difTimes))
    cat(mean(aggfinaldata$loglikeValues[1:6]), mean(aggfinaldata$loglikeValues[13:18]))
    cat('in', region, 'the t.test between the models EMP-GAModelWindow and GAModelWindow is: ')
    difTimes<-with(aggfinaldata,loglikeValues[1:6]-loglikeValues[13:18])
    print(t.test(difTimes))
    cat(mean(aggfinaldata$loglikeValues[1:6]), mean(aggfinaldata$loglikeValues[19:24]))
    cat('in', region, 'the t.test between the models EMP-GAModelWindow and GAModelSLC is: ')
    difTimes<-with(aggfinaldata,loglikeValues[1:6]-loglikeValues[19:24])
    print(t.test(difTimes))
    cat(mean(aggfinaldata$loglikeValues[7-12]), mean(aggfinaldata$loglikeValues[13:18]))
    cat('in', region, 'the t.test between the models EMP-GAModelSL and GAModelWindow is: ')
    difTimes<-with(aggfinaldata,loglikeValues[7:12]-loglikeValues[13:18])
    print(t.test(difTimes))
    cat(mean(aggfinaldata$loglikeValues[7:12]), mean(aggfinaldata$loglikeValues[19:24]))
    cat('in', region, 'the t.test between the models EMP-GAModelSL and GAModelSLC is: ')
    difTimes<-with(aggfinaldata,loglikeValues[7:12]-loglikeValues[19:24])
    print(t.test(difTimes))
    cat(mean(aggfinaldata$loglikeValues[13:18]), mean(aggfinaldata$loglikeValues[19:24]))
    cat('in', region, 'the t.test between the models GAModelWindow and GAModelSLC is: ')
    difTimes<-with(aggfinaldata,loglikeValues[13:18]-loglikeValues[19:24])
    print(t.test(difTimes))
}

ttestPaired('Kansai')
ttestPaired('Tohoku')
ttestPaired('EastJapan')
ttestPaired('Kanto')

