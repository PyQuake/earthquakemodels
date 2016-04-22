#!/usr/bin/env Rscript
options(scipen=999)
library(grid)
library(latticeExtra)
library(png)
library(grDevices)
library(RColorBrewer)

setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/dataForR")


#region(kanto), year(2000~2005), model (listas, ga, RI), depth(25,60,100)
finalData = data.frame(setNames(replicate(5,numeric(0), simplify = F),c("loglikeValues", "model", "depths", "years", "regions")))
for (i in 1:4) {
  if (i==1) {
    region="Kanto"
  }
  else if (i==2) {
    region="Kansai"
  }
  else if (i==3) {
    region == "Tohoku"
  }
  else{
    region = "EastJapan"
  }
  for (year in 2000:2005) {
    file = paste(region,"_",year,"_LastGen","25","gaModel",".txt",sep="")
    gaModel25 = read.csv2(file, sep='\n', header=F)
    file = paste(region,"_",year,"_LastGen","60","gaModel",".txt",sep="")
    gaModel60 = read.csv2(file, sep='\n', header=F)
    file = paste(region,"_",year,"_LastGen","100","gaModel",".txt",sep="")
    gaModel100 = read.csv2(file, sep='\n', header=F)
    
    valuesGA25 = rep(0, length(gaModel25$V1))
    for (k in 1:length(gaModel25$V1)){
      valuesGA25[k] = as.numeric(levels(gaModel25$V1[k]))[gaModel25$V1[k]]
    }
    valuesGA60 = rep(0, length(gaModel60$V1))
    for (k in 1:length(gaModel60$V1)){
      valuesGA60[k] = as.numeric(levels(gaModel60$V1[k]))[gaModel60$V1[k]]
    }
    valuesGA100 = rep(0, length(gaModel100$V1))
    for (k in 1:length(gaModel100$V1)){
      valuesGA100[k] = as.numeric(levels(gaModel100$V1[k]))[gaModel100$V1[k]]
    }
    loglikeGA = c(valuesGA25, valuesGA60, valuesGA100)
    
    file = paste(region,"_",year,"_LastGen","25","listaGA_New",".txt",sep="")
    lista25 = read.csv2(file, sep='\n', header=F)
    file = paste(region,"_",year,"_LastGen","60","listaGA_New",".txt",sep="")
    lista60 = read.csv2(file, sep='\n', header=F)
    file = paste(region,"_",year,"_LastGen","100","listaGA_New",".txt",sep="")
    lista100 = read.csv2(file, sep='\n', header=F)
    
    valuesLista25 = rep(0, length(lista25$V1))
    for (k in 1:length(lista25$V1)){
      valuesLista25[k] = as.numeric(levels(lista25$V1[k]))[lista25$V1[k]]
    }
    valuesLista60 = rep(0, length(lista60$V1))
    for (k in 1:length(lista60$V1)){
      valuesLista60[k] = as.numeric(levels(lista60$V1[k]))[lista60$V1[k]]
    }
    valuesLista100 = rep(0, length(lista100$V1))
    for (k in 1:length(lista100$V1)){
      valuesLista100[k] = as.numeric(levels(lista100$V1[k]))[lista100$V1[k]]
    } 
    file = paste("ri_",year,sep="")
    dataRI = read.csv2(file, sep='', header=F)
    
    loglikeRI = as.numeric(as.character(dataRI[9,9]))
    loglikeLista = c(valuesLista25, valuesLista60, valuesLista100)
    loglikeValues = c(loglikeGA, loglikeLista, loglikeRI)
    
    nameGa = c(rep("gaModel",30))
    nameLista = c(rep("lista",30))
    model = c(nameGa, nameLista, "RI")
    
    years = c(rep(year,61))
    
    regions = c(rep(region, 61))
    
    depth25 = c(rep("25",10))
    depth60 = c(rep("60",10))
    depth100 = c(rep("100",10))
    depthsAmodel = c(depth25, depth60, depth100)
    depths= c(depthsAmodel, depthsAmodel, 'RI')
    data = data.frame(loglikeValues, model, depths, years, regions)
    if (dim(finalData)[1]==0) {
      finalData = merge(finalData, data, all.y=T)  
    }
    else{
      finalData=rbind(finalData, data)
    }
    rm(data)
  }
}

save(finalData,file="data.Rda")
  


#filtro das linhas que quero e não quero
load("data.Rda")
resultANOVA = aov(finalData$loglikeValues~finalData$model+finalData$depths+finalData$years+finalData$regions)
summary(resultANOVA)
resultANOVA = aov(finalData$loglikeValues~finalData$model+finalData$depths+finalData$regions)
summary(resultANOVA)
tuk = TukeyHSD(resultANOVA)
plot(tuk)
# 
# fileToSave = paste(region,year,"aovANOVA.txt",sep='')
# dataToSave = as.data.frame(do.call(rbind, summary(aov_testing)))
# write.table(dataToSave, fileToSave)
# fileToSave = paste(region,year,"TukeyTest.png",sep='')
# png(fileToSave, width = 800, height = 800)

# print(tuk)
# plot(tuk)
# dev.off() 