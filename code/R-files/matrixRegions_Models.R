#!/usr/bin/env Rscript
setwd("~/Documents/estudos/unb/earthquakemodels/Zona/paper_exp")
options(scipen=999)
library(grid)
library(latticeExtra)
library(png)
library(grDevices)
library(RColorBrewer)

loadData = function(region, year, depth, type){
    file = paste(type,'_',region,"_",depth,'_',year,".txt",sep="")
    data = read.csv2(file, sep='\n', header=F)
    return(data)
}

plotMatrixReal = function(modelData, fileToSave, r, c){
    # TODO -- hardcoded map is BAD
    matrixData = matrix(nrow = r, ncol = c) 
    k = 1
    for (i in 1:r){
        for (j in 1:c){
            value = as.numeric(levels(modelData$V1[k]))[modelData$V1[k]]
            value = value + 1
            if (value > 12){
                value = 12 
            }
            matrixData[i,j] = value
            k = k + 1
        }
    }
    png(fileToSave, width = 800, height = 800)
    jBrewColors <- rev(heat.colors(16))
    p = levelplot((matrixData), col.regions = jBrewColors, alpha.regions=0.6)
    print( p+ layer(grid.raster(as.raster(image)), under=T))
    dev.off()
}


year=2005
while(year<=2010){
    setwd("~/Documents/estudos/unb/earthquakemodels/Zona2")
    
    region="EastJapan"
    image <- readPNG("../data/coast.png")
    file = paste("3.0",region,"real",year,".txt",sep="")
    raw_data = read.csv2(file, sep='\n', header=F)
    saveFile = paste("./heatMap/real",region,"_",year,".png",sep="")
    plotMatrixReal(raw_data, saveFile, 40, 40) 
    #20X40!
    # a imagem tá uma merda
    region="Tohoku"
    image <- readPNG("../data/touhoku.png")
    file = paste("3.0",region,"real",year,".txt",sep="")
    raw_data = read.csv2(file, sep='\n', header=F)
    saveFile = paste("./heatMap/real",region,"_",year,".png",sep="")
    plotMatrixReal(raw_data, saveFile, 20, 40) 
    region="Kansai"
    image <- readPNG("../data/kansai.png")
    file = paste("3.0",region,"real",year,".txt",sep="")
    raw_data = read.csv2(file, sep='\n', header=F)
    saveFile = paste("./heatMap/real",region,"_",year,".png",sep="")
    plotMatrixReal(raw_data, saveFile, 40, 40) 
    region="Kanto"
    image <- readPNG("../data/kantomap.png")
    file = paste("3.0",region,"real",year,".txt",sep="")
    raw_data = read.csv2(file, sep='\n', header=F)
    saveFile = paste("./heatMap/real",region,"_",year,".png",sep="")
    plotMatrixReal(raw_data, saveFile, 45, 45)   
    print(year)
    year=year+1
    
}

setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/dataForR")

calcMediaNP = function(year, region,r,c){
    soma = rep(0, r*c)
    setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/dataForR")
    for(i in 1:10){
        file = paste(region,"paper_etasNP",year,i-1,".txt",sep="")
        raw_data = read.csv2(file, sep='\n', header=F)
        for (k in 1:length(raw_data$V1)){
            value = as.numeric(levels(raw_data$V1[k]))[raw_data$V1[k]]
            soma[k]=soma[k]+value
        }
    }
    return(soma/10)
}

calcMediaModelo = function(year, region,r,c){
    soma = rep(0, r*c)
    setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/dataForR")
    for(i in 1:10){
        # raw_data = loadData(region, year, '25', 'clustered_listaGA_New')
        file = paste(region,"paper_modelo",year,i-1,".txt",sep="")
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
            #model direto
            #value = as.numeric(levels(modelData$V1[k]))[modelData$V1[k]]
            #media dos model
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
    print( p+ layer(grid.raster(as.raster(image)), under=T))
    dev.off()
}
year=2005
#modelo
while(year<=2010){
    setwd("~/Documents/estudos/unb/earthquakemodels/Zona2")
    region="EastJapan"
    image <- readPNG("../data/coast.png")
    setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/dataForR")
    saveFile = paste("heatMap/NP",region,"_",year,".png",sep="")
    mediaEastJapan=calcMediaNP(year = year, region = region, r = 40, 40)
    plotMatrixModel(mediaEastJapan, saveFile, 40, 40) 
    saveFile = paste("heatMap/modelo",region,"_",year,".png",sep="")
    mediaEastJapan=calcMediaModelo(year = year, region = region, r = 40, 40)
    plotMatrixModel(mediaEastJapan, saveFile, 40, 40) 
    
    #20X40!
    # a imagem tá uma merda
    region="Tohoku"
    image <- readPNG("../data/touhoku.png")
    setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/dataForR")
    saveFile = paste("heatMap/NP",region,"_",year,".png",sep="")
    mediaTohoku=calcMediaNP(year = year, region = region, r = 20, 40)
    plotMatrixModel(round(mediaTohoku,0), saveFile, 20, 40)
    saveFile = paste("heatMap/modelo",region,"_",year,".png",sep="")
    mediaTohoku=calcMediaModelo(year = year, region = region, r = 20, 40)
    plotMatrixModel(round(mediaTohoku,0), saveFile, 20, 40)
    
    region="Kansai"
    image <- readPNG("../data/kansai.png")
    saveFile = paste("heatMap/NP",region,"_",year,".png",sep="")
    mediaKansai=calcMediaNP(year = year, region = region, r = 40, 40)
    plotMatrixModel(mediaKansai, saveFile, 40, 40)
    saveFile = paste("heatMap/modelo",region,"_",year,".png",sep="")
    mediaKansai=calcMediaModelo(year = year, region = region, r = 40, 40)
    plotMatrixModel(mediaKansai, saveFile, 40, 40)
    
    region="Kanto"
    image <- readPNG("../data/kantomap.png")
    saveFile = paste("heatMap/NP",region,"_",year,".png",sep="")
    mediaKanto=calcMediaNP(year = year, region = region, r = 45, 45)
    plotMatrixModel(mediaKanto, saveFile, 45, 45)
    saveFile = paste("heatMap/modelo",region,"_",year,".png",sep="")
    mediaKanto=calcMediaModelo(year = year, region = region, r = 45, 45)
    plotMatrixModel(mediaKanto, saveFile, 45, 45)
    year=year+1
    print(year)
}

calcMediaSimples = function(data){
    soma = rep(0, 10)
    for (k in 1:length(data)){
        value = as.numeric(levels(data[[k]]))
        soma[k]=soma[k]+value
    }
    return(sum(soma)/10)
}

converting = function(data){
    soma = rep(0, 10)
    for (k in 1:length(data)){
        value = as.numeric(levels(data[[k]]))
        soma[k]=soma[k]+value
    }
    return(soma)
}

# getingData = function(region, year){
#     setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/dataForR")
#     
#     for (i in 1:10){
#         file = paste(region,"paper_modelo",year,i-1,".txtloglikelihood.txt",sep="")
#         gaModel[i] <<- read.csv2(file, sep='\n', header=F)
#         file = paste(region,"paper_etasNP",year,i-1,".txtloglikelihood.txt",sep="")
#         NP[i] <<- read.csv2(file, sep='\n', header=F)
#     }
# }

# year=2005
# while(year<=2010){
#     gaModel=rep(0,10)
#     NP=rep(0,10)
#     getingData("Kanto", year)
#     mediaGAModel = calcMediaSimples(gaModel)
#     cat("mu é a media do GAModel", year, sep="")
#     cat("against the list method for same year. Region: Kanto")
#     print(t.test(mu=mediaGAModel, converting(NP)))
#     
#     gaModel=rep(0,10)
#     NP=rep(0,10)
#     getingData("EastJapan", year)
#     mediaGAModel = calcMediaSimples(gaModel)
#     cat("mu é a media do GAModel", year, sep="")
#     cat("against the list method for same year. Region: EastJapan") 
#     print(t.test(mu=mediaGAModel, converting(NP)))
#     
#     gaModel=rep(0,10)
#     NP=rep(0,10)
#     getingData("Tohoku", year)
#     mediaGAModel = calcMediaSimples(gaModel)
#     cat("mu é a media do GAModel", year, sep="")
#     cat("against the list method for same year. Region: Tohoku") 
#     print(t.test(mu=mediaGAModel, converting(NP)))
#     
#     gaModel=rep(0,10)
#     NP=rep(0,10)
#     getingData("Kansai", year)
#     mediaGAModel = calcMediaSimples(gaModel)
#     cat("mu é a media do GAModel", year, sep="")
#     cat("against the list method for same year. Region: Kansai") 
#     print(t.test(mu=mediaGAModel, converting(NP)))
#     
#     year=year+1
# }

