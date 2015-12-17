#!/usr/bin/env Rscript
setwd("~/Documents/estudos/unb/earthquakemodels/code")
options(scipen=999)
library(grid)
library(latticeExtra)
library(png)
library(grDevices)
library(RColorBrewer)
#display.brewer.all()
image <- readPNG("../data/kantomap.png")

plotMatrixModel = function(modelData, fileToSave){
  # TODO -- hardcoded map is BAD
  matrixData = matrix(nrow = 45, ncol = 45) 
  k = 1
  for (i in 1:45){
    for (j in 1:45){
      value = as.numeric(levels(modelData$V1[k]))[modelData$V1[k]]
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

plotMatrixReal = function(modelData, fileToSave){
  # TODO -- hardcoded map is BAD
  matrixData = matrix(nrow = 45, ncol = 45) 
  k = 1
  for (i in 1:45){
    for (j in 1:45){
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



year = 2005
#sem ri
while(year<=2010){
  #etas
  setwd("~/Documents/estudos/unb/earthquakemodels/Zona/model/")
  file = paste("teste_etasNP",year,"exec.txt",sep="")
  raw_data = read.csv2(file, sep='\n', header=F)
  saveFile = paste("../model_heatMap/etasNP",year,"heatMap.png",sep="")
  plotMatrixModel(raw_data, saveFile)  
  
  #gaModel
  file = paste("modelo",year,"exec.txt",sep="")
  raw_data = read.csv2(file, sep='\n', header=F)
  saveFile = paste("../model_heatMap/gaModel",year,"heatMap.png",sep="")
  plotMatrixModel(raw_data, saveFile) 
  
  #control 1
  file = paste("teste_tudo1model",year,".txt",sep="")
  raw_data = read.csv2(file, sep='\n', header=F)
  saveFile = paste("../model_heatMap/tudo1model",year,"heatMap.png",sep="")
  plotMatrixModel(raw_data, saveFile) 
  
  #control 2
  file = paste("teste_randModel",year,".txt",sep="")
  raw_data = read.csv2(file, sep='\n', header=F)
  saveFile = paste("../model_heatMap/randModel",year,"heatMap.png",sep="")
  plotMatrixModel(raw_data, saveFile) 
  
  #real
  setwd("~/Documents/estudos/unb/earthquakemodels/Zona")
  file = paste("realEtas",year,".txt",sep="")
  raw_data = read.csv2(file, sep='\n', header=F)
  saveFile = paste("model_heatMap/real",year,"heatMap.png",sep="")
  plotMatrixModel(raw_data, saveFile)  
  
  
  
  year=year+1
}

year = 2005
#Com RI
while(year<=2010){
  #etas
  setwd("~/Documents/estudos/unb/earthquakemodels/Zona/model/")
  file = paste("teste_etasNP",year,"WithRI.txt",sep="")
  raw_data = read.csv2(file, sep='\n', header=F)
  saveFile = paste("../model_heatMap/etasNP",year,"WithRIheatMap.png",sep="")
  plotMatrixModel(raw_data, saveFile)  
  
  #gaModel
#   file = paste("teste_gaModel",year,"WithRI.txt",sep="")
#   raw_data = read.csv2(file, sep='\n', header=F)
#   saveFile = paste("../model_heatMap/gaModel",year,"WithRIheatMap.png",sep="")
#   plotMatrixModel(raw_data, saveFile) 
  
  
  
  year=year+1
}


#as.numeric(levels(raw_data$V1[k]))[raw_data$V1[k]]

