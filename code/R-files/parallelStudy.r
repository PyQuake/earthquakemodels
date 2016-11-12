setwd("~/Documents/estudos/unb/earthquakemodels/code/parallel")
options(scipen=999)
library(grid)
library(latticeExtra)
library(png)
library(grDevices)
library(RColorBrewer)



loadData = function(region, year, depth, type){
    file = paste(region,'_',depth,'_',year,i-1,".txt",sep="")
    data = read.csv2(file, sep='\n', header=F)
    return(data)
}


calcMedia = function(type, year, depth, region,r,c){
    soma = rep(0, r*c)
    for(i in 1:10){
        file = paste(region,'_',depth,'_',year,i-1,".txt",sep="")
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
    while(year<=2010){
        
        region="EastJapan"
        saveFile = paste("./heatMap/",depth,region,"_",depth,'_',year,".png",sep="")
        mediaEastJapan=calcMedia(type=type,year=year, region=region, depth=depth, 40,40)
        imagePath<<-"../../data/coast.png"
        plotMatrixModel(mediaEastJapan, saveFile, 40, 40) 
        
        #20X40!
        # a imagem tá uma merda
        region="Tohoku"
        saveFile = paste("./heatMap/",depth,region,"_",depth,'_',year,".png",sep="")
        mediaTouhoku=calcMedia(type=type,year=year, region=region, depth=depth, 20,40)
        imagePath<<-"../../data/touhoku.png"
        plotMatrixModel(mediaTouhoku, saveFile, 20, 40) 
        
        region="Kansai"
        saveFile = paste("./heatMap/",depth,region,"_",depth,'_',year,".png",sep="")
        mediaKansai=calcMedia(type=type,year=year, region=region, depth=depth, 40,40)
        imagePath<<-"../../data/kansai.png"
        plotMatrixModel(mediaKansai, saveFile, 40, 40)  
        
        region="Kanto"
        saveFile = paste("./heatMap/",depth,region,"_",depth,'_',year,".png",sep="")
        mediaKanto=calcMedia(type=type,year=year, region=region, depth=depth, 45,45)
        imagePath<<-"../../data/kantomap.png"
        plotMatrixModel(mediaKanto, saveFile, 45, 45) 
        
        year=year+1
    }
}

plotModelsByYears('sc_hybrid_gaModel',100)


setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/DataFromR")
load("newdata.Rda")
summary(finalData)
setwd("~/Documents/estudos/unb/earthquakemodels/code/parallel")
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

loadData = function(region, year, depth, type){
    file = paste('loglikelihood',region,'_',depth,'_',year,".txt",sep="")
    data = read.csv2(file, sep='\n', header=F)
    return(data)
}

for (i in 1:4) {
    region = chooseRegion(i)
    for (year in 2005:2010){
        gaModelPar100 = loadData(region, year, '100', 'SCsc_hybrid_gaModel')
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
    }
}
summary(teste)



resultANOVA = aov(loglikeValues~model+depths+years+regions , data = finalData)
summary(resultANOVA)
tuk = TukeyHSD(resultANOVA)
op <- par(mar = c(5,15,4,2) + 0.1)
plot(tuk,las=1)
print(tuk)
