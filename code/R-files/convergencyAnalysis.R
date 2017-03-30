library(ggplot2)
library(gridExtra)
loadData = function(type,region, year, i){
    setwd("~/Documents/estudos/master-unb/earthquakemodels/Zona4/")
    file = paste(type,'/',region, type,year,'_',i,'logbook.txt',sep="")
    data = read.csv2(file, sep='\t', header=T)
    data$std = as.numeric(levels(data$std))[data$std]
    data$max = as.numeric(levels(data$max))[data$max]   
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

createData = function(modelName, region, year){
    
    data1 = loadData(modelName, region, year, 0)
    data2 = loadData(modelName, region, year, 1)
    data3 = loadData(modelName, region, year, 2)
    data4 = loadData(modelName, region, year, 3)
    data5 = loadData(modelName, region, year, 4)
    data6 = loadData(modelName, region, year, 5)
    data7 = loadData(modelName, region, year, 6)
    data8 = loadData(modelName, region, year, 7)
    data9 = loadData(modelName, region, year, 8)
    data10 = loadData(modelName, region, year, 9)
    
    maxs = c(rep(0,length(data1$max)))
    for (i in 1:length(data1$max)){
        maxs[i] = ((data1$max[i] + data2$max[i] + data3$max[i] + data4$max[i] + data5$max[i] + 
                        data6$max[i] + data7$max[i] + data8$max[i] + data9$max[i] + data10$max[i])/10)
    }
    
    stds = c(rep(0,length(data1$std)))
    for (i in 1:length(data1$std)){
        stds[i] = ((data1$std[i] + data2$std[i] + data3$std[i] + data4$std[i] + data5$std[i] + 
                        data6$std[i] + data7$std[i] + data8$std[i] + data9$std[i] + data10$std[i])/10)
    }
    
    gen = c(1:100)
    data = data.frame(
        setNames(replicate(3,numeric(0), simplify = F),
                 c("maxs", "stds", "gen")))
    
    data = data.frame(maxs, stds, gen)
    
    return (data)
}


plotConvergencyData = function(data, type, region, year){

    saveFile = paste("../Zona4/heatMap/", type, region,"_",year,".png",sep="")
    png(saveFile, width = 800, height = 800)
    if (type == 'GAModel'){
        p1<- ggplot(data, aes(x=gen, y=maxs, group=1)) + 
            geom_line(color='orange') +
            geom_point(color='orange')+
            # coord_cartesian(ylim = c(min(data$maxs), max(data$maxs))) + 
            geom_errorbar(aes(ymin=data$maxs+data$stds, ymax=data$maxs-data$stds), width=0.2, color='black')
        grid.arrange(p1,ncol=1, top = paste("Convergency Analysis in ",region,"year of", year, "(ReducedGAModel - GAModel)"))
        dev.off()    
    }
    else{
        p1<- ggplot(data, aes(x=gen, y=maxs, group=1)) + 
            geom_line(color='orange') +
            geom_point(color='orange')+
            coord_cartesian(ylim = c(min(data$maxs), max(data$maxs))) + 
            geom_errorbar(aes(ymin=data$maxs+data$stds, ymax=data$maxs-data$stds), width=0.2, color='black')
        grid.arrange(p1,ncol=1, top = paste("Convergency Analysis in ",region,"year of", year, "(ReducedGAModel - GAModel)"))
        dev.off()
    }
    
}

for (i in 1:4){
    region = chooseRegion(i)
    for (year in 2005:2009){
        plotConvergencyData(createData(modelName = 'ReducedGAModel',region,year),'ReducedGAModel', region, year)
        plotConvergencyData(createData(modelName = 'GAModel',region,year),'GAModel', region, year)
    }    
}





