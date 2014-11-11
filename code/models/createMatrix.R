#!/usr/bin/env Rscript
setwd("~/Documents/Estudos/Tsukuba/earthquakemodels/code")
options(scipen=999)
library(grid)
library(latticeExtra)
library(png)
setwd("~/Documents/Estudos/Tsukuba/earthquakemodels/code/models")

plotMatrizModel = function(filename, fileToSave){
  print ("passo0")
  image <- readPNG("../../data/kantomap.png")
  print ("passo1")
  raw_data = read.csv2(filename, sep='', header=F)
  teste = apply(raw_data, 1, as.character)
  modelData = apply(teste, 1, as.numeric)
  print ("passo2")
  matrixData = matrix(nrow = 45, ncol = 45) 
  k = 1
  for (i in 1:45){
    for (j in 1:45){
      matrixData[i,j] = modelData[k] + 1
      k = k + 1
    }
  }
  png(fileToSave, width = 800, height = 800)
  print ("passo3")
  p = levelplot(log(matrixData), col.regions = terrain.colors,
                alpha.regions = 0.5, contour = 1)
  p + layer(grid.raster(as.raster(image)), under=TRUE)
  print(p)
  dev.off()
}