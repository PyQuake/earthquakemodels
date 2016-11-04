setwd("~/Documents/estudos/unb/earthquakemodels/zechar_sw/")
gaEtas2005=read.csv2("gaModels2005/molchan2005GaEtas.txt", sep="", header = F)
gaModel2005=read.csv2("gaModels2005/molchanGaModel2005.txt", sep="", header = F)
gaEtas2006=read.csv2("gaModels2006/molchan2006GaEtas.txt", sep="", header = F)
gaModel2006=read.csv2("gaModels2006/molchanGaModel2006.txt", sep="", header = F)
gaEtas2007=read.csv2("gaModels2007/molchan2007GaEtas.txt", sep="", header = F)
gaModel2007=read.csv2("gaModels2007/molchanGaModel2007.txt", sep="", header = F)
gaEtas2008=read.csv2("gaModels2008/molchan2008GaEtas.txt", sep="", header = F)
gaModel2008=read.csv2("gaModels2008/molchanGaModel2008.txt", sep="", header = F)
gaEtas2009=read.csv2("gaModels2009/molchan2009GaEtas.txt", sep="", header = F)
gaModel2009=read.csv2("gaModels2009/molchanGaModel2009.txt", sep="", header = F)
gaEtas2010=read.csv2("gaModels2010/molchan2010GaEtas.txt", sep="", header = F)
gaModel2010=read.csv2("gaModels2010/molchanGaModel2010.txt", sep="", header = F)

plotMolchanModels <- function(model,string,year){
  aux=list()
  for (i in 1:nrow(model[1])){
    value = as.numeric(levels(model[i,1]))[model[i,1]]
    if(value<0.2){
      aux[[i]]=0
    }
    else if(value<0.4){
      aux[[i]]=0.2
    }
    else if(value<0.6){
      aux[[i]]=0.4
    }
    else if(value<0.8){
      aux[[i]]=0.6
    }
    else if(value<1){
      aux[[i]]=0.8
    }
    else{
      aux[[i]]=1
    }
  }
  # aux[[i+1]]=1
  molchan = rep(0,rep(length(aux)))  
  for (i in 1:length(aux)){
    molchan[i]=aux[[i]]  
  }
  op2 <- par(mar = c(5,4,4,4) + 0.1)
  plot(1-molchan, type="l",xaxt = 'n', xlab="fraction of space-time occupied by alarm",
       ylab="miss rate", main =paste(string,"Molchan diagram",year))
  axis(1, at=c(0,length(molchan)*0.2,length(molchan)*0.4, length(molchan)*0.6,
               length(molchan)*0.8, length(molchan)), labels=c(0.0,0.2, 0.4,0.6,0.8,1))
  axis(4, at=c(1,0.8,0.6,0.4,0.2,0),labels=c(0,as.integer(length(molchan)*0.2),as.integer(length(molchan)*0.4),
                                             as.integer(length(molchan)*0.6),as.integer(length(molchan)*0.8),
                                             as.integer(length(molchan))))
  mtext("hits", side = 4, line = 3)
}



plotMolchanModels(gaModel2005, "gaModel Published",2005)
plotMolchanModels(gaEtas2005, "New gaModel",2005)
plotMolchanModels(gaModel2006, "gaModel Published",2006)
plotMolchanModels(gaEtas2006, "New gaModel",2006)
plotMolchanModels(gaModel2007, "gaModel Published",2007)
plotMolchanModels(gaEtas2007, "New gaModel",2007)
plotMolchanModels(gaModel2008, "gaModel Published",2008)
plotMolchanModels(gaEtas2008, "New gaModel",2008)
plotMolchanModels(gaModel2009, "gaModel Published",2009)
plotMolchanModels(gaEtas2009, "New gaModel",2009)
plotMolchanModels(gaModel2010, "gaModel Published",2010)
plotMolchanModels(gaEtas2010, "New gaModel",2010)





