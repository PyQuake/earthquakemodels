setwd("~/Documents/estudos/master-unb/earthquakemodels/result_exp_benchmark/gaBenchmarksStudy/")
library(knitr)
library(ggplot2)
library(gridExtra)

loadDataBenchmarksF5_F24 = function(type, i){
    filename = paste(type,'_',i,'.txt',sep='')
    data = read.csv(file = filename, header = T, nrows = 200, sep = '\t', skip=2)
    return(data)
}

loadDataBenchmarksF1_F4 = function(type, i){
    filename = paste(type,'_',i,'.txt',sep='')
    data = read.csv(file = filename, header = T, nrows = 200, sep = '\t')
    return(data)
}

# create function to find the mean of the 40 exec
createConvergencyDataBenchmarks = function (name_function, j){
    df = data.frame()
    for (i in 1:40) {
        if(j<4){
            data=loadDataBenchmarksF1_F4(name_function,i-1)    
        }
        else{
            data=loadDataBenchmarksF5_F24(name_function,i-1)    
        }
        
        df <- rbind(df, data)
    }
    minimum = tapply(df$min, INDEX = df$gen, FUN = mean)
    std = tapply(df$std, INDEX = df$gen, FUN = mean)
    std = pmin(std, 200)
    gen = c(1:200)
    df = data.frame(minimum, std, gen)
    df
}

plotforKBenchmarks = function(k){
    # for (j in 2:25){
        j=2
        name_function = paste('F',k,'_',j, sep='')
        print(name_function)
        vectorAuxMax = createConvergencyDataBenchmarks(name_function, k)
        p1<- ggplot(vectorAuxMax, aes(1:nrow(vectorAuxMax), minimum, colour=vectorAuxMax$minimum)) + 
            # geom_errorbar(aes(ymin=vectorAuxMax$minimum-vectorAuxMax$std, ymax=vectorAuxMax$minimum+vectorAuxMax$std), width=.1) +
            geom_line() +
            geom_point() +
            xlab('tournament size') + 
            ylab('function mean value') +
            ggtitle(name_function) #+
        # geom_segment(aes(x = 1:nrow(vectorAuxMax), y = vectorAuxMax$five, xend = 1:nrow(vectorAuxMax), yend=vectorAuxMax$ninetyFive))
        print(p1+ theme(legend.position="none"))    
    # }
    
}


for (i in 1:24){
    plotforKBenchmarks(i)
}


#create function to read data with paste - header problems - GA
loadDataGA_2_10 = function(type, i){
    filename = paste(type,'_',i,'.txt',sep='')
    data = read.csv(file = filename, header = T, nrows = 200, sep = '\t', skip=1)
    return(data)
}

# create function to read data with paste - header problems - GA
loadDataGA_11_25 = function(type, i){
    filename = paste(type,'_',i,'.txt',sep='')
    data = read.csv(file = filename, header = T, nrows = 200, sep = '\t', skip=3)
    return(data)
}


# create function to find the mean of the 40 execs
createConvergencyDataGA = function (name_function, j){
    df = data.frame()
    for (i in 1:40) {
        if (j == 2){
            data=loadDataGA_11_25(name_function,i-1)    
        }
        else if (j<=10) {
            data=loadDataGA_2_10(name_function,i-1)    
        }
        else{
            data=loadDataGA_11_25(name_function,i-1)    
        }
        df <- rbind(df, data)
    }
    minimum = (-1)*tapply(df$max, INDEX = df$gen, FUN = mean)
    std = tapply(df$std, INDEX = df$gen, FUN = mean)
    std = pmin(std, 200)
    gen = c(1:200)
    df = data.frame(minimum, std, gen)
    df
}

plotforKGA = function(){
    for (j in 2:25){
        name_function = paste('GA_',j, sep='')
        print(name_function)
        vectorAuxMax = createConvergencyDataGA(name_function, j)
        p1<- ggplot(vectorAuxMax, aes(1:nrow(vectorAuxMax), minimum, colour=vectorAuxMax$minimum)) + 
            geom_errorbar(aes(ymin=vectorAuxMax$minimum-vectorAuxMax$std, ymax=vectorAuxMax$minimum+vectorAuxMax$std), width=.1) +
            geom_line() +
            geom_point() +
            xlab('tournament size') + 
            ylab('function mean value') +
            ggtitle(name_function) #+
        # geom_segment(aes(x = 1:nrow(vectorAuxMax), y = vectorAuxMax$five, xend = 1:nrow(vectorAuxMax), yend=vectorAuxMax$ninetyFive))
        print(p1+ theme(legend.position="none"))    
    }
    
}

plotforKGA()
