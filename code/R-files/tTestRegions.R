#!/usr/bin/env Rscript
setwd("~/Documents/estudos/unb/earthquakemodels/Zona/paper_exp")
options(scipen=999)
library(grid)
library(latticeExtra)
library(png)
library(grDevices)
library(RColorBrewer)
#display.brewer.all()

setwd("~/Documents/estudos/unb/earthquakemodels/Zona/paper_exp")

calcMediaNP = function(year, region,r,c){
  soma = rep(0, r*c)
  setwd("~/Documents/estudos/unb/earthquakemodels/Zona/paper_exp")
  for(i in 1:10){
    file = paste("MediaNP_Hybrid",region,"_",year,i-1,"cleaned.txt",sep="")
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
  setwd("~/Documents/estudos/unb/earthquakemodels/Zona/paper_exp")
  for(i in 1:10){
    file = paste("MediaModelo_Hybrid",region,"_",year,i-1,"cleaned.txt",sep="")
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
year=2006
#modelo
while(year<=2010){
  region="EastJapan"
  image <- readPNG("../../data/coast.png")
  saveFile = paste("heatMap/NP_Hybrid",region,"_",year,".png",sep="")
  mediaEastJapan=calcMediaNP(year = year, region = region, r = 40, 40)
  saveMedia = paste("./mediaNP_Hybrid",region,"_",year,".txt",sep="")
  write.table(round(mediaEastJapan,0), saveMedia)
  plotMatrixModel(mediaEastJapan, saveFile, 40, 40) 
  saveFile = paste("heatMap/modelo_Hybrid",region,"_",year,".png",sep="")
  mediaEastJapan=calcMediaModelo(year = year, region = region, r = 40, 40)
  saveMedia = paste("./mediaModelo_Hybrid",region,"_",year,".txt",sep="")
  write.table(round(mediaEastJapan,0), saveMedia)
  plotMatrixModel(mediaEastJapan, saveFile, 40, 40) 
  
  #20X40!
  # a imagem tá uma merda
  region="Tohoku"
  image <- readPNG("../../data/touhoku.png")
  saveFile = paste("heatMap/NP_Hybrid",region,"_",year,".png",sep="")
  mediaTohoku=calcMediaNP(year = year, region = region, r = 20, 40)
  saveMedia = paste("./mediaNP_Hybrid",region,"_",year,".txt",sep="")
  write.table(mediaEastJapan, saveMedia)
  plotMatrixModel(round(mediaTohoku,0), saveFile, 20, 40)
  saveFile = paste("heatMap/modelo_Hybrid",region,"_",year,"png",sep="")
  mediaTohoku=calcMediaModelo(year = year, region = region, r = 20, 40)
  saveMedia = paste("./mediaModelo_Hybrid",region,"_",year,".txt",sep="")
  write.table(round(mediaTohoku,0), saveMedia)
  plotMatrixModel(mediaTohoku, saveFile, 20, 40)
  
  region="Kansai"
  image <- readPNG("../../data/kansai.png")
  saveFile = paste("heatMap/NP_Hybrid",region,"_",year,".png",sep="")
  mediaKansai=calcMediaNP(year = year, region = region, r = 40, 40)
  saveMedia = paste("./mediaNP_Hybrid",region,"_",year,".txt",sep="")
  write.table(round(mediaKansai,0), saveMedia)
  plotMatrixModel(mediaKansai, saveFile, 40, 40)
  saveFile = paste("heatMap/modelo_Hybrid",region,"_",year,".png",sep="")
  mediaKansai=calcMediaModelo(year = year, region = region, r = 40, 40)
  saveMedia = paste("./mediaModelo_Hybrid",region,"_",year,".txt",sep="")
  write.table(round(mediaKansai,0), saveMedia)
  plotMatrixModel(mediaKansai, saveFile, 40, 40)
  
  region="Kanto"
  image <- readPNG("../../data/kantomap.png")
  saveFile = paste("heatMap/NP_Hybrid",region,"_",year,".png",sep="")
  mediaKanto=calcMediaNP(year = year, region = region, r = 45, 45)
  saveMedia = paste("./mediaNP_Hybrid",region,"_",year,".txt",sep="")
  write.table(round(mediaKanto,0), saveMedia)
  plotMatrixModel(mediaKanto, saveFile, 45, 45)
  saveFile = paste("heatMap/modelo_Hybrid",region,"_",year,".png",sep="")
  mediaKanto=calcMediaModelo(year = year, region = region, r = 45, 45)
  saveMedia = paste("./mediaModelo_Hybrid",region,"_",year,".txt",sep="")
  write.table(round(mediaKanto,0), saveMedia)
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

getingData = function(region, year){
  setwd("~/Documents/estudos/unb/earthquakemodels/Zona/paper_exp/")
  
  for (i in 1:10){
    
    file = paste("MediaModelo_Hybrid",region,"_",year,i-1,"cleaned.txtloglikelihood.txt",sep="")
    gaModel[i] <<- read.csv2(file, sep='\n', header=F)
    file = paste("MediaNP_Hybrid",region,"_",year,i-1,"cleaned.txtloglikelihood.txt",sep="")
    NP[i] <<- read.csv2(file, sep='\n', header=F)
  }
}

year=2006
while(year<=2010){
  gaModel=rep(0,10)
  NP=rep(0,10)
  getingData("Kanto", year)
  mediaGAModel = calcMediaSimples(gaModel)
  cat("mu é a media do GAModel_Hybrid", year, sep="")
  cat("against the list_Hybrid method for same year. Region: Kanto")
  print(t.test(mu=mediaGAModel, converting(NP)))
  
  gaModel=rep(0,10)
  NP=rep(0,10)
  getingData("EastJapan", year)
  mediaGAModel = calcMediaSimples(gaModel)
  cat("mu é a media do GAModel_Hybrid", year, sep="")
  cat("against the list_Hybrid method for same year. Region: EastJapan") 
  print(t.test(mu=mediaGAModel, converting(NP)))
  
  gaModel=rep(0,10)
  NP=rep(0,10)
  getingData("Tohoku", year)
  mediaGAModel = calcMediaSimples(gaModel)
  cat("mu é a media do GAModel_Hybrid", year, sep="")
  cat("against the list_Hybrid method for same year. Region: Tohoku") 
  print(t.test(mu=mediaGAModel, converting(NP)))
  
  gaModel=rep(0,10)
  NP=rep(0,10)
  getingData("Kansai", year)
  mediaGAModel = calcMediaSimples(gaModel)
  cat("mu é a media do GAModel_Hybrid", year, sep="")
  cat("against the list_Hybrid method for same year. Region: Kansai") 
  print(t.test(mu=mediaGAModel, converting(NP)))
  
  year=year+1
}


