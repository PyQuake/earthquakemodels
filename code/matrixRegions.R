  #!/usr/bin/env Rscript
options(scipen=999)
library(grid)
library(latticeExtra)
library(png)
library(grDevices)
library(RColorBrewer)

# ainda tem que por os demais modelos, hybrid e clustered   
  
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
    print( p+ layer(grid.raster(as.raster(imagem)), under=T))
    dev.off()
  }
  

  plotRealByYears = function(){
      year=2005
      while(year<=2010){
        setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/")
        region="EastJapan"
        imagem <<- readPNG("../data/coast.png")
        file = paste("realData/",region,"real_", year,".txt",sep="")
        raw_data = read.csv2(file, sep='\n', header=F)
        saveFile = paste("./heatMap/real/real",region,"_",year,".png",sep="")
        plotMatrixReal(raw_data, saveFile, 40, 40) 
        #20X40!
        # a imagem tá uma merda
        region="Tohoku"
        imagem <<- readPNG("../data/touhoku.png")
        file = paste("realData/",region,"real_", year,".txt",sep="")
        raw_data = read.csv2(file, sep='\n', header=F)
        saveFile = paste("./heatMap/real/real",region,"_",year,".png",sep="")
        plotMatrixReal(raw_data, saveFile, 20, 40) 
        region="Kansai"
        imagem <<- readPNG("../data/kansai.png")
        file = paste("realData/",region,"real_", year,".txt",sep="")
        raw_data = read.csv2(file, sep='\n', header=F)
        saveFile = paste("./heatMap/real/real",region,"_",year,".png",sep="")
        plotMatrixReal(raw_data, saveFile, 40, 40) 
        region="Kanto"
        imagem <<- readPNG("../data/kantomap.png")
        file = paste("realData/",region,"real_", year,".txt",sep="")
        raw_data = read.csv2(file, sep='\n', header=F)
        saveFile = paste("./heatMap/real/real",region,"_",year,".png",sep="")
        plotMatrixReal(raw_data, saveFile, 45, 45)   
        year=year+1
      }
  }
  
  
  calcMedia = function(type, year, depth, region,r,c){
      if (type=='hybrid_ListaGA_New') {
          soma = rep(0, r*c)
          for(i in 1:10){
              file = paste(type,'/hybrid_ListaGA_New',region,'_',depth,'_',year,'_',i-1,".txt",sep="")
              raw_data = read.csv2(file, sep='\n', header=F)
              for (k in 1:length(raw_data$V1)){
                  value = as.numeric(levels(raw_data$V1[k]))[raw_data$V1[k]]
                  soma[k]=soma[k]+value
              }
          }
          return(soma/10)
      }
      else if(type=='hybrid_gaModel'){
          soma = rep(0, r*c)
          for(i in 1:10){
              file = paste(type,'/hybrid_gaModel',region,'_',depth,'_',year,'_',i-1,".txt",sep="")
              raw_data = read.csv2(file, sep='\n', header=F)
              for (k in 1:length(raw_data$V1)){
                  value = as.numeric(levels(raw_data$V1[k]))[raw_data$V1[k]]
                  soma[k]=soma[k]+value
              }
          }
          return(soma/10) 
      }
      else if (type=='clusteredII_gaModel') {
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
      else if (type=='clusteredII_hybrid_gaModel') {
          soma = rep(0, r*c)
          for(i in 1:10){
              file = paste(type,'/hybrid_gaModel',region,'_',depth,'_',year,'_',i-1,".txt",sep="")
              raw_data = read.csv2(file, sep='\n', header=F)
              for (k in 1:length(raw_data$V1)){
                  value = as.numeric(levels(raw_data$V1[k]))[raw_data$V1[k]]
                  soma[k]=soma[k]+value
              }
          }
          return(soma/10)
      }
      else if (type=='clusteredII_hybrid_ListaGA_New') {
          soma = rep(0, r*c)
          for(i in 1:10){
              file = paste(type,'/hybrid_ListaGA_New',region,'_',depth,'_',year,i-1,".txt",sep="")
              raw_data = read.csv2(file, sep='\n', header=F)
              for (k in 1:length(raw_data$V1)){
                  value = as.numeric(levels(raw_data$V1[k]))[raw_data$V1[k]]
                  soma[k]=soma[k]+value
              }
          }
          return(soma/10)
      }
      else if (type=='clusteredII_listaGA_new') {
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
      else if (type=='clustered_gaModel') {
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
      else if (type=='clustered_hybrid_gaModel') {
          soma = rep(0, r*c)
          for(i in 1:10){
              file = paste(type,'/hybrid_gaModel',region,'_',depth,'_',year,'_',i-1,".txt",sep="")
              raw_data = read.csv2(file, sep='\n', header=F)
              for (k in 1:length(raw_data$V1)){
                  value = as.numeric(levels(raw_data$V1[k]))[raw_data$V1[k]]
                  soma[k]=soma[k]+value
              }
          }
          return(soma/10)
      }
      else if (type=='clustered_hybrid_ListaGA_New') {
          soma = rep(0, r*c)
          for(i in 1:10){
              file = paste(type,'/hybrid_ListaGA_New',region,'_',depth,'_',year,'_',i-1,".txt",sep="")
              raw_data = read.csv2(file, sep='\n', header=F)
              for (k in 1:length(raw_data$V1)){
                  value = as.numeric(levels(raw_data$V1[k]))[raw_data$V1[k]]
                  soma[k]=soma[k]+value
              }
          }
          return(soma/10)
      }
      else if (type=='clustered_listaGA_new') {
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
      else{
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
      # imageData=grid.raster(as.raster(readPNG("../data/touhoku.png")))
      p = levelplot((matrixData), col.regions = jBrewColors, alpha.regions=0.6)
      grid.raster(as.raster(readPNG(imagePath)))
      print( p+ layer(grid.raster(as.raster(readPNG(imagePath))), under=T))
      dev.off()
  }
  
  plotModelsByYears= function(type, depth){
      year=2005
      #modelo
      while(year<=2010){
          setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/")
          
          region="EastJapan"
          saveFile = paste("./heatMap/",type,region,"_",depth,'_',year,".png",sep="")
          mediaEastJapan=calcMedia(type=type,year=year, region=region, depth=depth, 40,40)
          imagePath<<-"../data/coast.png"
          plotMatrixModel(mediaEastJapan, saveFile, 40, 40) 
          
          #20X40!
          # a imagem tá uma merda
#           region="Tohoku"
#           saveFile = paste("./heatMap/",type,region,"_",depth,'_',year,".png",sep="")
#           mediaTouhoku=calcMedia(type=type,year=year, region=region, depth=depth, 20,40)
#           imagePath<<-"../data/touhoku.png"
#           plotMatrixModel(mediaTouhoku, saveFile, 20, 40) 
#           
#           region="Kansai"
#           saveFile = paste("./heatMap/",type,region,"_",depth,'_',year,".png",sep="")
#           mediaKansai=calcMedia(type=type,year=year, region=region, depth=depth, 40,40)
#           imagePath<<-"../data/kansai.png"
#           plotMatrixModel(mediaKansai, saveFile, 40, 40)  
#           
#           region="Kanto"
#           saveFile = paste("./heatMap/",type,region,"_",depth,'_',year,".png",sep="")
#           mediaKanto=calcMedia(type=type,year=year, region=region, depth=depth, 45,45)
#           imagePath<<-"../data/kantomap.png"
#           plotMatrixModel(mediaKanto, saveFile, 45, 45) 
          
          year=year+1
      }
  }
  
  plotRealByYears()
  # hybrid_ListaGA_New, hybrid_gaModel
  plotModelsByYears('gaModel',25)
  plotModelsByYears('gaModel',60)
  plotModelsByYears('gaModel',100)
  
  plotModelsByYears('listaGA_New',25)
  plotModelsByYears('listaGA_New',60)
  plotModelsByYears('listaGA_New',100)
  
  plotModelsByYears('hybrid_ListaGA_New',25)
  plotModelsByYears('hybrid_ListaGA_New',60)
  plotModelsByYears('hybrid_ListaGA_New',100)
  
  plotModelsByYears('hybrid_gaModel',25)
  plotModelsByYears('hybrid_gaModel',60)
  plotModelsByYears('hybrid_gaModel',100)
  
  # clusteredII_gaModel/hybrid_ListaGA_NewEastJapan_25_2005_0, esse e o reducedGAModelWindow
  # hybrid_gaModelEastJapan_25_2005_0, esse e o gamodelwindow
  # tem os dois tirando o hybrid
  plotModelsByYears('clusteredII_gaModel',25)#nao ta certo, nao ta hybrid
#   plotModelsByYears('clusteredII_gaModel',60)
#   plotModelsByYears('clusteredII_gaModel',100)
  
  plotModelsByYears('clusteredII_hybrid_gaModel',25)#nao ta certo, nao ta hybrid
#   plotModelsByYears('clusteredII_hybrid_gaModel',60)
#   plotModelsByYears('clusteredII_hybrid_gaModel',100)
  
  plotModelsByYears('clusteredII_hybrid_ListaGA_New',25)#nao ta certo, nao ta hybrid
#   plotModelsByYears('clusteredII_hybrid_ListaGA_New',60)
#   plotModelsByYears('clusteredII_hybrid_ListaGA_New',100)
  
  plotModelsByYears('clusteredII_listaGA_new',25)#nao ta certo, nao ta hybridclusteredII_hybrid_ListaGA_New
#   plotModelsByYears('clusteredII_listaGA_new',60)
#   plotModelsByYears('clusteredII_listaGA_new',100)
#   
  
  plotModelsByYears('clustered_gaModel',25)#nao ta certo, nao ta hybrid
#   plotModelsByYears('clustered_gaModel',60)
#   plotModelsByYears('clustered_gaModel',100)
  
  plotModelsByYears('clustered_hybrid_gaModel',25)#nao ta certo, nao ta hybrid
#   plotModelsByYears('clustered_hybrid_gaModel',60)
#   plotModelsByYears('clustered_hybrid_gaModel',100)
  
  plotModelsByYears('clustered_hybrid_ListaGA_New',25)#ta ok
#   plotModelsByYears('clustered_hybrid_ListaGA_New',60)
#   plotModelsByYears('clustered_hybrid_ListaGA_New',100)
#   
  plotModelsByYears('clustered_listaGA_new',25)#nao ta certo, nao ta hybrid
#   plotModelsByYears('clustered_listaGA_new',60)
#   plotModelsByYears('clustered_listaGA_new',100)
#   
 