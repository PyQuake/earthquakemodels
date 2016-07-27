#!/usr/bin/env Rscript

#region(kanto), year(2000~2005)=>2005~2010, model (listas, ga), depth(25,60,100)

setwd("~/Documents/estudos/unb/earthquakemodels/Zona2/dataForR")

loadData = function(region, year, depth, type){
    file = paste(type,'_',region,"_",depth,'_',year,".txt",sep="")
    data = read.csv2(file, sep='\n', header=F)
    return(data)
}

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

convertToNumeric = function(model){
    values = rep(0, length(model$V1))
    for (k in 1:length(model$V1)){
        values[k] = as.numeric(levels(model$V1[k]))[model$V1[k]]
    }
    return(values)
}

loadRI = function(year){
    file = paste("ri_",year,sep="")
    dataRI = read.csv2(file, sep='', header=F)
    
    return(dataRI)
}


finalData = data.frame(
    setNames(replicate(5,numeric(0), simplify = F),
             c("loglikeValues", "model", "depths", "years", "regions")))

for (i in 1:4) {
    region = chooseRegion(i)    
  for (year in 2000:2005) {
    gaModel25 = loadData(region, year+5, '25', 'gaModel')
    gaModel60 = loadData(region, year+5, '60', 'gaModel')
    gaModel100 = loadData(region, year+5, '100', 'gaModel')
    
    lista25 = loadData(region, year+5, '25', 'listaGA_New')
    lista60 = loadData(region, year+5, '60', 'listaGA_New')
    lista100 = loadData(region, year+5, '100', 'listaGA_New')
    
    valuesGA25 = convertToNumeric(gaModel25)
    valuesGA60 = convertToNumeric(gaModel60)
    valuesGA100 = convertToNumeric(gaModel100)
            
    valuesLista25 = convertToNumeric(lista25)
    valuesLista60 = convertToNumeric(lista60)
    valuesLista100 = convertToNumeric(lista100)
    
    loglikeGA = c(valuesGA25, valuesGA60, valuesGA100)
    loglikeLista = c(valuesLista25, valuesLista60, valuesLista100)
    loglikeValues = c(loglikeGA, loglikeLista)
    nameGa = c(rep("GAModel",30))
    nameLista = c(rep("ReducedGAModel",30))
    
    years = c(rep(toString(year+5),60))
    regions = c(rep(region, 60))
    depth25 = c(rep('25',10))
    depth60 = c(rep('60',10))
    depth100 = c(rep('100',10))
    depthsAmodel = c(depth25, depth60, depth100)
    model = c(nameGa, nameLista)
    depths= c(depthsAmodel, depthsAmodel)
    data = data.frame(loglikeValues, model, depths, years, regions)
    if (dim(finalData)[1]==0) {
        finalData = merge(finalData, data, all.y=T)  
    }
    else{
        finalData=rbind(finalData, data)
    }
    rm(data)
    
    gaModel25 = loadData(region, year+5, '25', 'hybrid_gaModel')
    gaModel60 = loadData(region, year+5, '60', 'hybrid_gaModel')
    gaModel100 = loadData(region, year+5, '100', 'hybrid_gaModel')
    
    lista25 = loadData(region, year+5, '25', 'hybrid_listaGA_New')
    lista60 = loadData(region, year+5, '60', 'hybrid_listaGA_New')
    lista100 = loadData(region, year+5, '100', 'hybrid_listaGA_New')
    
    valuesGA25 = convertToNumeric(gaModel25)
    valuesGA60 = convertToNumeric(gaModel60)
    valuesGA100 = convertToNumeric(gaModel100)
    
    valuesLista25 = convertToNumeric(lista25)
    valuesLista60 = convertToNumeric(lista60)
    valuesLista100 = convertToNumeric(lista100)
    
    loglikeGA = c(valuesGA25, valuesGA60, valuesGA100)
    loglikeLista = c(valuesLista25, valuesLista60, valuesLista100)
    
    
    loglikeValues = c(loglikeGA, loglikeLista)
    nameGa = c(rep("EMP-GAModel",30))
    nameLista = c(rep("EMP-ReducedGAModel",30))
    
    years = c(rep(toString(year+5),60))
    regions = c(rep(region, 60))
    depth25 = c(rep('25',10))
    depth60 = c(rep('60',10))
    depth100 = c(rep('100',10))
    depthsAmodel = c(depth25, depth60, depth100)
    model = c(nameGa, nameLista)
    depths= c(depthsAmodel, depthsAmodel)
    data = data.frame(loglikeValues, model, depths, years, regions)
    if (dim(finalData)[1]==0) {
        finalData = merge(finalData, data, all.y=T)  
    }
    else{
        finalData=rbind(finalData, data)
    }
    rm(data)
    
    gaModel25 = loadData(region, year+5, '25', 'clustered_hybrid_gaModel')
    gaModel60 = loadData(region, year+5, '60', 'clustered_hybrid_gaModel')
    gaModel100 = loadData(region, year+5, '100', 'clustered_hybrid_gaModel')
    
    lista25 = loadData(region, year+5, '25', 'clustered_hybrid_listaGA_New')
    lista60 = loadData(region, year+5, '60', 'clustered_hybrid_listaGA_New')
    lista100 = loadData(region, year+5, '100', 'clustered_hybrid_listaGA_New')
    
    valuesGA25 = convertToNumeric(gaModel25)
    valuesGA60 = convertToNumeric(gaModel60)
    valuesGA100 = convertToNumeric(gaModel100)
    
    valuesLista25 = convertToNumeric(lista25)
    valuesLista60 = convertToNumeric(lista60)
    valuesLista100 = convertToNumeric(lista100)
    
    loglikeGA = c(valuesGA25, valuesGA60, valuesGA100)
    loglikeLista = c(valuesLista25, valuesLista60, valuesLista100)
    loglikeValues = c(loglikeGA, loglikeLista)
    nameGa = c(rep("EMP-GAModelWindow",30))
    nameLista = c(rep("EMP-ReducedGAModelWindow",30))
    
    years = c(rep(toString(year+5),60))
    regions = c(rep(region, 60))
    depth25 = c(rep('25',10))
    depth60 = c(rep('60',10))
    depth100 = c(rep('100',10))
    depthsAmodel = c(depth25, depth60, depth100)
    model = c(nameGa, nameLista)
    depths= c(depthsAmodel, depthsAmodel)
    data = data.frame(loglikeValues, model, depths, years, regions)
    if (dim(finalData)[1]==0) {
        finalData = merge(finalData, data, all.y=T)  
    }
    else{
        finalData=rbind(finalData, data)
    }
    rm(data)
    
    gaModel25 = loadData(region, year+5, '25', 'clusteredII_hybrid_gaModel')
    gaModel60 = loadData(region, year+5, '60', 'clusteredII_hybrid_gaModel')
    gaModel100 = loadData(region, year+5, '100', 'clusteredII_hybrid_gaModel')
    
    lista25 = loadData(region, year+5, '25', 'clusteredII_hybrid_listaGA_New')
    lista60 = loadData(region, year+5, '60', 'clusteredII_hybrid_listaGA_New')
    lista100 = loadData(region, year+5, '100', 'clusteredII_hybrid_listaGA_New')
    
    valuesGA25 = convertToNumeric(gaModel25)
    valuesGA60 = convertToNumeric(gaModel60)
    valuesGA100 = convertToNumeric(gaModel100)
    
    valuesLista25 = convertToNumeric(lista25)
    valuesLista60 = convertToNumeric(lista60)
    valuesLista100 = convertToNumeric(lista100)
    
    loglikeGA = c(valuesGA25, valuesGA60, valuesGA100)
    loglikeLista = c(valuesLista25, valuesLista60, valuesLista100)
    loglikeValues = c(loglikeGA, loglikeLista)
    nameGa = c(rep("EMP-GAModelSLC",30))
    nameLista = c(rep("EMP-ReducedGAModelSLC",30))
    
    years = c(rep(toString(year+5),60))
    regions = c(rep(region, 60))
    depth25 = c(rep('25',10))
    depth60 = c(rep('60',10))
    depth100 = c(rep('100',10))
    depthsAmodel = c(depth25, depth60, depth100)
    model = c(nameGa, nameLista)
    depths= c(depthsAmodel, depthsAmodel)
    data = data.frame(loglikeValues, model, depths, years, regions)
    if (dim(finalData)[1]==0) {
        finalData = merge(finalData, data, all.y=T)  
    }
    else{
        finalData=rbind(finalData, data)
    }
    rm(data)
    
    gaModel25 = loadData(region, year+5, '25', 'clustered_gaModel')
    gaModel60 = loadData(region, year+5, '60', 'clustered_gaModel')
    gaModel100 = loadData(region, year+5, '100', 'clustered_gaModel')
    
    lista25 = loadData(region, year+5, '25', 'clustered_listaGA_New')
    lista60 = loadData(region, year+5, '60', 'clustered_listaGA_New')
    lista100 = loadData(region, year+5, '100', 'clustered_listaGA_New')
    
    valuesGA25 = convertToNumeric(gaModel25)
    valuesGA60 = convertToNumeric(gaModel60)
    valuesGA100 = convertToNumeric(gaModel100)
    
    valuesLista25 = convertToNumeric(lista25)
    valuesLista60 = convertToNumeric(lista60)
    valuesLista100 = convertToNumeric(lista100)
    
    loglikeGA = c(valuesGA25, valuesGA60,valuesGA100)
    loglikeLista = c(valuesLista25, valuesLista60, valuesLista100)
    loglikeValues = c(loglikeGA, loglikeLista)
    
    nameGa = c(rep("GAModelWindow",30))
    nameLista = c(rep("ReducedGAModelWindow",30))
    years = c(rep(toString(year+5),60))
    regions = c(rep(region, 60))
    
    depth25 = c(rep('25',10))
    depth60 = c(rep('60',10))
    depth100 = c(rep('100',10))
    depthsAmodel = c(depth25, depth60, depth100)
    model = c(nameGa, nameLista)
    depths = c(depthsAmodel, depthsAmodel)
    data = data.frame(loglikeValues, model,depths, years, regions)
    if (dim(finalData)[1]==0) {
        finalData = merge(finalData, data, all.y=T)  
    }
    else{
        finalData=rbind(finalData, data)
    }
    rm(data)
    
    gaModel25 = loadData(region, year+5, '25', 'clusteredII_gaModel')
    gaModel60 = loadData(region, year+5, '60', 'clusteredII_gaModel')
    gaModel100 = loadData(region, year+5, '100', 'clusteredII_gaModel')
    
    lista25 = loadData(region, year+5, '25', 'clusteredII_listaGA_New')
    lista60 = loadData(region, year+5, '60', 'clusteredII_listaGA_New')
    lista100 = loadData(region, year+5, '100', 'clusteredII_listaGA_New')
    
    valuesGA25 = convertToNumeric(gaModel25)
    valuesGA60 = convertToNumeric(gaModel60)
    valuesGA100 = convertToNumeric(gaModel100)
    
    valuesLista25 = convertToNumeric(lista25)
    valuesLista60 = convertToNumeric(lista60)
    valuesLista100 = convertToNumeric(lista100)
    
    loglikeGA = c(valuesGA25, valuesGA60,valuesGA100)
    loglikeLista = c(valuesLista25, valuesLista60, valuesLista100)
    loglikeValues = c(loglikeGA, loglikeLista)
    
    nameGa = c(rep("GAModelSLC",30))
    nameLista = c(rep("ReducedGAModelSLC",30))
    years = c(rep(toString(year+5),60))
    regions = c(rep(region, 60))
    
    depth25 = c(rep('25',10))
    depth60 = c(rep('60',10))
    depth100 = c(rep('100',10))
    depthsAmodel = c(depth25, depth60, depth100)
    model = c(nameGa, nameLista)
    depths = c(depthsAmodel, depthsAmodel)
    data = data.frame(loglikeValues, model,depths, years, regions)
    if (dim(finalData)[1]==0) {
        finalData = merge(finalData, data, all.y=T)  
    }
    else{
        finalData=rbind(finalData, data)
    }
    rm(data)
        #dadosSC
    if (region == 'Kanto' | region == 'EastJapan'){
        gaModel100 = loadData(region, year+5, '100', 'SCgaModel')
        lista100 = loadData(region, year+5, '100', 'SClistaGA_New')
        
        valuesGA100 = convertToNumeric(gaModel100)
        valuesLista100 = convertToNumeric(lista100)
        
        loglikeGA = c(valuesGA100)
        loglikeLista = c(valuesLista100)
        loglikeValues = c(loglikeGA, loglikeLista)
        
        nameGa = c(rep("GAModelSC",10))
        nameLista = c(rep("ReducedGAModelSC",10))
        years = c(rep(toString(year+5),20))
        regions = c(rep(region, 20))
        
        depth100 = c(rep('100',10))
        depthsAmodel = c(depth100)
        model = c(nameGa, nameLista)
        depths = c(depthsAmodel, depthsAmodel)
        data = data.frame(loglikeValues, model,depths, years, regions)
        if (dim(finalData)[1]==0) {
            finalData = merge(finalData, data, all.y=T)  
        }
        else{
            finalData=rbind(finalData, data)
        }
        rm(data)
        #dadosSC com emp
        gaModel100 = loadData(region, year+5, '100', 'SCsc_hybrid_gaModel')
        lista100 = loadData(region, year+5, '100', 'SCsc_hybrid_ListaGA_New')
        
        valuesGA100 = convertToNumeric(gaModel100)
        valuesLista100 = convertToNumeric(lista100)
        
        loglikeGA = c(valuesGA100)
        loglikeLista = c(valuesLista100)
        loglikeValues = c(loglikeGA, loglikeLista)
        
        nameGa = c(rep("EMP-GAModelSC",10))
        nameLista = c(rep("EMP-ReducedGAModelSC",10))
        years = c(rep(toString(year+5),20))
        regions = c(rep(region, 20))
        
        depth100 = c(rep('100',10))
        depthsAmodel = c(depth100)
        model = c(nameGa, nameLista)
        depths = c(depthsAmodel, depthsAmodel)
        data = data.frame(loglikeValues, model,depths, years, regions)
        if (dim(finalData)[1]==0) {
            finalData = merge(finalData, data, all.y=T)  
        }
        else{
            finalData=rbind(finalData, data)
        }
        rm(data)
    }     
  } 
}

# for (year in 2005:2010){
#     riData = loadRI(year)
#     loglikeRI = as.numeric(as.character(riData[9,9]))
#     model = c("RI")
#     depths= c('RI')
#     years = year
#     regions = region
#     data = data.frame(loglikeValues, model, depths, years, regions, clustered)
#     print(data)
#     finalData=rbind(finalData, data)
#     if (dim(finalData)[1]==0) {
#         finalData = merge(finalData, data, all.y=T)  
#     }
#     else{
#         finalData=rbind(finalData, data)
#     }
#     rm(data)    
# }

save(finalData,file="../DataFromR/newdata.Rda")
summary(finalData)  
which(finalData$model=='GAModel')
which(finalData$model=='ReducedGAModel')
which(finalData$model=='EMP-GAModel')
which(finalData$model=='EMP-ReducedGAModel')
which(finalData$model=='GAModel')
which(finalData$model=='ReducedGAModel')


