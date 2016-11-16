setwd("~/Documents/estudos/unb/earthquakemodels/code/")
options(scipen=999)
library(grid)
library(latticeExtra)
library(png)
library(grDevices)
library(RColorBrewer)



loadData = function(type, region, year, depth){
    file = paste('loglike/',type,region,'_',depth,'_',year,".txt",sep="")
    data = read.csv2(file, sep='\n', header=F)
    return(data)
}

convertToNumeric = function(model){
    values = rep(0, length(model$V1))
    for (k in 1:length(model$V1)){
        values[k] = as.numeric(levels(model$V1[k]))[model$V1[k]]
    }
    return(values)
}

calcMedia = function(type, year, depth, region,r,c){
    soma = rep(0, r*c)
    for(i in 1:10){
        file = paste(type,'/',region,'_',depth,'_',year,i-1,".txt",sep="")
        raw_data = read.csv2(file, sep='\n', header=F)
        for (k in 1:length(raw_data$V1)){
            value = as.numeric(levels(raw_data$V1[k]))[raw_data$V1[k]]
            soma[k]=soma[k]+value
        }
    }
    return(soma/10)
}

plotMatrixModel = function(modelData, fileToSave, r, c){
    # TODO -- hardcoded map is BAD
    matrixData = matrix(nrow = r, ncol = c) 
    k = 1
    for (i in 1:r){
        for (j in 1:c){
            if(is.na(modelData[k])==T){
                value=0 
            }
            else{
                value = modelData[k]
                if (value > 12){
                    value = 12 
                }
            }
            matrixData[i,j] = value
            k = k + 1
        }
    }
    png(fileToSave, width = 800, height = 800)
    jBrewColors <- rev(heat.colors(16))
    p = levelplot((matrixData), col.regions = jBrewColors, alpha.regions=0.6)
    grid.raster(as.raster(readPNG(imagePath)))
    print( p+ layer(grid.raster(as.raster(readPNG(imagePath))), under=T))
    dev.off()
}


plotModelsByYears= function(type, depth){
    year=2005
    #modelo
    while(year<=2008){
        
        region="Kanto"
        saveFile = paste("./heatMap/",type,region,"_",depth,'_',year,".png",sep="")
        mediaKanto=calcMedia(type=type,year=year, region=region, depth=depth, 45,45)
        imagePath<<-"../data/kantomap.png"
        plotMatrixModel(mediaKanto, saveFile, 45, 45) 
        
        year=year+1
    }
}


setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/DataFromR")
load("newdata.Rda")
summary(finalData)
setwd("~/Documents/estudos/unb/earthquakemodels/code/")
chooseRegion = function(i){
    if (i==1) {
        region="Kanto"
    }
    else if (i==2) {
        region="Kansai"
    }
    else if (i==3) {
        region = "Tohoku"
    }
    else{
        region = "EastJapan"
    }
    return(region)
}

region = chooseRegion(1)
for (year in 2005:2010){
    #gamodelpar
    gaModelPar100 = loadData('parallel-random', region, year, '100')
    valuesGAPar100 = convertToNumeric(gaModelPar100)
    
    loglikeValues = c(valuesGAPar100)
    nameGa = c(rep("GAModelPar",10))
    years = c(rep(toString(year),10))
    regions = c(rep(region, 10))
    depth100 = c(rep('100',10))
    depthsAmodel = c(depth100)
    
    model = c(nameGa)
    depths = c(depthsAmodel, depthsAmodel)
    data = data.frame(loglikeValues, model,depths, years, regions)
    finalData=rbind(finalData, data)
    rm(data) 
    #parallelList
    gaModelPar100 = loadData('parallelList-random', region, year, '100')
    valuesGAPar100 = convertToNumeric(gaModelPar100)
    
    loglikeValues = c(valuesGAPar100)
    nameGa = c(rep("ReducedGAModelPar",10))
    years = c(rep(toString(year),10))
    regions = c(rep(region, 10))
    depth100 = c(rep('100',10))
    depthsAmodel = c(depth100)
    
    model = c(nameGa)
    depths = c(depthsAmodel, depthsAmodel)
    data = data.frame(loglikeValues, model,depths, years, regions)
    finalData=rbind(finalData, data)
    rm(data) 
    #sc-parallel-random
    gaModelPar100 = loadData('sc-parallel-random', region, year, '100')
    valuesGAPar100 = convertToNumeric(gaModelPar100)
    
    loglikeValues = c(valuesGAPar100)
    nameGa = c(rep("GAModelParSC",10))
    years = c(rep(toString(year),10))
    regions = c(rep(region, 10))
    depth100 = c(rep('100',10))
    depthsAmodel = c(depth100)
    
    model = c(nameGa)
    depths = c(depthsAmodel, depthsAmodel)
    data = data.frame(loglikeValues, model,depths, years, regions)
    finalData=rbind(finalData, data)
    rm(data) 
    #sc-parallelList-
    gaModelPar100 = loadData('sc-parallelList-random', region, year, '100')
    valuesGAPar100 = convertToNumeric(gaModelPar100)
    
    loglikeValues = c(valuesGAPar100)
    nameGa = c(rep("ReducedGAModelParSC",10))
    years = c(rep(toString(year),10))
    regions = c(rep(region, 10))
    depth100 = c(rep('100',10))
    depthsAmodel = c(depth100)
    
    model = c(nameGa)
    depths = c(depthsAmodel, depthsAmodel)
    data = data.frame(loglikeValues, model,depths, years, regions)
    finalData=rbind(finalData, data)
    rm(data) 
}
summary(finalData)

subTabela = finalData[finalData$regions=='Kanto',]
subTabela = subTabela[subTabela$years!='2009'&subTabela$years!='2010',]
subTabela = subTabela[subTabela$model=='GAModelSC'&subTabela$model=='ReducedGAModelSC'&
                      subTabela$model!='Emp-GAModelWindow'&subTabela$model!='Emp-ReducedGAModelWindow'&
                      subTabela$model!='Emp-GAModelSLC'&subTabela$model!='Emp-ReducedGAModelSLC'
                      ,]
summary(subTabela)
#
mean(finalData$loglikeValues[finalData$model=='GAModelPar'&finalData$year=='2005'])
mean(finalData$loglikeValues[finalData$model=='ReducedGAModelPar'&finalData$year=='2005'])
mean(finalData$loglikeValues[finalData$model=='GAModelParSC'&finalData$year=='2005'])
mean(finalData$loglikeValues[finalData$model=='ReducedGAModelParSC'&finalData$year=='2005'])

mean(finalData$loglikeValues[finalData$model=='GAModelPar'&finalData$year=='2006'])
mean(finalData$loglikeValues[finalData$model=='ReducedGAModelPar'&finalData$year=='2006'])
mean(finalData$loglikeValues[finalData$model=='GAModelParSC'&finalData$year=='2006'])
mean(finalData$loglikeValues[finalData$model=='ReducedGAModelParSC'&finalData$year=='2006'])

mean(finalData$loglikeValues[finalData$model=='GAModelPar'&finalData$year=='2007'])
mean(finalData$loglikeValues[finalData$model=='ReducedGAModelPar'&finalData$year=='2007'])
mean(finalData$loglikeValues[finalData$model=='GAModelParSC'&finalData$year=='2007'])
mean(finalData$loglikeValues[finalData$model=='ReducedGAModelParSC'&finalData$year=='2007'])

mean(finalData$loglikeValues[finalData$model=='GAModelPar'&finalData$year=='2008'])
mean(finalData$loglikeValues[finalData$model=='ReducedGAModelPar'&finalData$year=='2008'])
mean(finalData$loglikeValues[finalData$model=='GAModelParSC'&finalData$year=='2008'])
mean(finalData$loglikeValues[finalData$model=='ReducedGAModelParSC'&finalData$year=='2008'])

mean(finalData$loglikeValues[finalData$model=='GAModelPar'&finalData$year=='2009'])
mean(finalData$loglikeValues[finalData$model=='ReducedGAModelPar'&finalData$year=='2009'])
mean(finalData$loglikeValues[finalData$model=='GAModelParSC'&finalData$year=='2009'])
mean(finalData$loglikeValues[finalData$model=='ReducedGAModelParSC'&finalData$year=='2009'])

mean(finalData$loglikeValues[finalData$model=='GAModelPar'&finalData$year=='2010'])
mean(finalData$loglikeValues[finalData$model=='ReducedGAModelPar'&finalData$year=='2010'])
mean(finalData$loglikeValues[finalData$model=='GAModelParSC'&finalData$year=='2010'])
mean(finalData$loglikeValues[finalData$model=='ReducedGAModelParSC'&finalData$year=='2010'])










# resultANOVA = aov(loglikeValues~model+depths+years+regions , data = finalData)
# summary(resultANOVA)
# tuk = TukeyHSD(resultANOVA)
# op <- par(mar = c(5,15,4,2) + 0.1)
# plot(tuk,las=1)
# print(tuk)
# plotModelsByYears('parallel-random', depth)
# plotModelsByYears('sc-parallel-random', depth)
# plotModelsByYears('sc-parallelList-random', depth)
# plotModelsByYears('parallelList-random', depth)
