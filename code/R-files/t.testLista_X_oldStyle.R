#Antes deve rodar clean.py nos dados da GA

setwd("~/Documents/Estudos/UnB/GA/projeto-ga/simpleGA/simpleGA_v2.0/logBook")
library("Hmisc", lib.loc="/Library/Frameworks/R.framework/Versions/3.1/Resources/library")
# mediaGeracaoOld <- function(file, n){
  raw_data = read.csv2(file, sep='', header=F)
  teste = apply(raw_data, 1, as.character)
  y2000 = apply(teste, 1, as.numeric)
  
  soma = rep(0, 100)
  for (i in 1:50){
    for(j in 1:100){
      soma[j]  = y2000[(n*5000)+((i-1)*100)+j,4] + soma[j]
    }  
  }
  soma = soma/50
  return(soma)
}

# mediaMelhorGeracaoOld <- function(file, n){
  raw_data = read.csv2(file, sep='', header=F)
  teste = apply(raw_data, 1, as.character)
  y2000 = apply(teste, 1, as.numeric)
  
  soma = rep(0, 100)
  for (i in 1:50){
    for(j in 1:100){
      soma[j]  = y2000[(n*5000)+((i-1)*100)+j,5] + soma[j]
    }  
  }
  soma = soma/50
  return(soma)
}

melhorGeracaoOld <- function(file, n){
  raw_data = read.csv2(file, sep='', header=F)
  teste = apply(raw_data, 1, as.character)
  y2000 = apply(teste, 1, as.numeric)
  
  res = rep(0, 10)
  for (i in 1:10){
      res[i]  = y2000[(n*5000)+(i*100),5]
  }
  return(res)
}


uniform2000best = melhorGeracaoOld("2000_Uniform.txt", 0)
uniform2001best = melhorGeracaoOld("2001_Uniform.txt", 1)
uniform2002best = melhorGeracaoOld("2002_Uniform.txt", 2)
uniform2003best = melhorGeracaoOld("2003_Uniform.txt", 3)
uniform2004best = melhorGeracaoOld("2004_Uniform.txt", 4)
uniform2005best = melhorGeracaoOld("2005_Uniform.txt", 5)
uniform2006best = melhorGeracaoOld("2006_Uniform.txt", 6)
uniform2007best = melhorGeracaoOld("2007_Uniform.txt", 7)
uniform2008best = melhorGeracaoOld("2008_Uniform.txt", 8)
uniform2009best = melhorGeracaoOld("2009_Uniform.txt", 9)
uniform2010best = melhorGeracaoOld("2010_Uniform.txt", 10)

setwd("~/Documents/Estudos/Tsukuba/earthquakemodels/Zona/etasGaModel")
mediaGeracaoEtas <- function(file){
  raw_data = read.csv2(file, sep='', header=F)
  
  soma = rep(0, 100)
  for (i in 1:10){
    for(j in 1:100){
      soma[j]  = as.numeric(as.character(
        raw_data[((i-1)*100)+j,1])) + soma[j]
    }  
  }
  soma = soma/10
  return(soma)
}
mediaGeracaoEtasMelhor <- function(file){
  raw_data = read.csv2(file, sep='', header=F)
  
  soma = rep(0, 100)
  for (i in 1:10){
    for(j in 1:100){
      soma[j]  = as.numeric(as.character(
        raw_data[((i-1)*100)+j,3])) + soma[j]
    }  
  }
  soma = soma/10
  return(soma)
}

geracaoEtasMelhor <- function(file){
  raw_data = read.csv2(file, sep='', header=F)
  
  res = rep(0, 10)
  for (i in 1:10){
    res[i]  = as.numeric(as.character(raw_data[(i*100),3]))
  }
  return(res)
}

readRI = function (){
  res = rep(0, 11)
  raw_data = read.csv2('ri_2000', sep='', header=F)
  res[1]=as.numeric(as.character(raw_data[9,9]))
  raw_data = read.csv2('ri_2001', sep='', header=F)
  res[2]=as.numeric(as.character(raw_data[9,9]))
  raw_data = read.csv2('ri_2002', sep='', header=F)
  res[3]=as.numeric(as.character(raw_data[9,9]))
  raw_data = read.csv2('ri_2003', sep='', header=F)
  res[4]=as.numeric(as.character(raw_data[9,9]))
  raw_data = read.csv2('ri_2004', sep='', header=F)
  res[5]=as.numeric(as.character(raw_data[9,9]))
  raw_data = read.csv2('ri_2005', sep='', header=F)
  res[6]=as.numeric(as.character(raw_data[9,9]))
  raw_data = read.csv2('ri_2006', sep='', header=F)
  res[7]=as.numeric(as.character(raw_data[9,9]))
  raw_data = read.csv2('ri_2007', sep='', header=F)
  res[8]=as.numeric(as.character(raw_data[9,9]))
  raw_data = read.csv2('ri_2008', sep='', header=F)
  res[9]=as.numeric(as.character(raw_data[9,9]))
  raw_data = read.csv2('ri_2009', sep='', header=F)
  res[10]=as.numeric(as.character(raw_data[9,9]))
  raw_data = read.csv2('ri_2010', sep='', header=F)
  res[11]=as.numeric(as.character(raw_data[9,9]))
  return(res)
}
riLog = readRI()

etasGaModel2000Best = geracaoEtasMelhor("etasGaModelNP_2000_logbook_R.txt")
etasGaModel2001Best = geracaoEtasMelhor("etasGaModelNP_2001_logbook_R.txt")
etasGaModel2002Best = geracaoEtasMelhor("etasGaModelNP_2002_logbook_R.txt")
etasGaModel2003Best = geracaoEtasMelhor("etasGaModelNP_2003_logbook_R.txt")
etasGaModel2004Best = geracaoEtasMelhor("etasGaModelNP_2004_logbook_R.txt")
etasGaModel2005Best = geracaoEtasMelhor("etasGaModelNP_2005_logbook_R.txt")
etasGaModel2006Best = geracaoEtasMelhor("etasGaModelNP_2006_logbook_R.txt")
etasGaModel2007Best = geracaoEtasMelhor("etasGaModelNP_2007_logbook_R.txt")
etasGaModel2008Best = geracaoEtasMelhor("etasGaModelNP_2008_logbook_R.txt")
etasGaModel2009Best = geracaoEtasMelhor("etasGaModelNP_2009_logbook_R.txt")
etasGaModel2010Best = geracaoEtasMelhor("etasGaModelNP_2010_logbook_R.txt")


etasContraGAModel000=t.test(uniform2000best, etasGaModel2000Best)
etasContraGAModel001=t.test(uniform2001best, etasGaModel2001Best)
etasContraGAModel002=t.test(uniform2002best, etasGaModel2002Best)
etasContraGAModel003=t.test(uniform2003best, etasGaModel2003Best)
etasContraGAModel004=t.test(uniform2004best, etasGaModel2004Best)
etasContraGAModel005=t.test(uniform2005best, etasGaModel2005Best)
etasContraGAModel006=t.test(uniform2006best, etasGaModel2006Best)
etasContraGAModel007=t.test(uniform2007best, etasGaModel2007Best)
etasContraGAModel008=t.test(uniform2008best, etasGaModel2008Best)
etasContraGAModel009=t.test(uniform2009best, etasGaModel2009Best)
etasContraGAModel010=t.test(uniform2010best, etasGaModel2010Best)

etascontraRI2000=t.test(mu=riLog[1], etasGaModel2000Best)
etascontraRI2001=t.test(mu=riLog[2], etasGaModel2001Best)
etascontraRI2002=t.test(mu=riLog[3], etasGaModel2002Best)
etascontraRI2003=t.test(mu=riLog[4], etasGaModel2003Best)
etascontraRI2004=t.test(mu=riLog[5], etasGaModel2004Best)
etascontraRI2005=t.test(mu=riLog[6], etasGaModel2005Best)
etascontraRI2006=t.test(mu=riLog[7], etasGaModel2006Best)
etascontraRI2007=t.test(mu=riLog[8], etasGaModel2007Best)
etascontraRI2008=t.test(mu=riLog[9], etasGaModel2008Best)
etascontraRI2009=t.test(mu=riLog[10], etasGaModel2009Best)
etascontraRI2010=t.test(mu=riLog[11], etasGaModel2010Best)

gaModelcontraRI2000=t.test(mu=riLog[1], uniform2000best)
gaModelcontraRI2001=t.test(mu=riLog[2], uniform2001best)
gaModelcontraRI2002=t.test(mu=riLog[3], uniform2002best)
gaModelcontraRI2003=t.test(mu=riLog[4], uniform2003best)
gaModelcontraRI2004=t.test(mu=riLog[5], uniform2004best)
gaModelcontraRI2005=t.test(mu=riLog[6], uniform2005best)
gaModelcontraRI2006=t.test(mu=riLog[7], uniform2006best)
gaModelcontraRI2007=t.test(mu=riLog[8], uniform2007best)
gaModelcontraRI2008=t.test(mu=riLog[9], uniform2008best)
gaModelcontraRI2009=t.test(mu=riLog[10], uniform2009best)
gaModelcontraRI2010=t.test(mu=riLog[11], uniform2010best)

readRandom = function (){
  res = rep(0, 11)
  raw_data = read.csv2('ri_2000', sep='', header=F)
  res[1]=as.numeric(as.character(raw_data[4,9]))
  raw_data = read.csv2('ri_2001', sep='', header=F)
  res[2]=as.numeric(as.character(raw_data[4,9]))
  raw_data = read.csv2('ri_2002', sep='', header=F)
  res[3]=as.numeric(as.character(raw_data[4,9]))
  raw_data = read.csv2('ri_2003', sep='', header=F)
  res[4]=as.numeric(as.character(raw_data[4,9]))
  raw_data = read.csv2('ri_2004', sep='', header=F)
  res[5]=as.numeric(as.character(raw_data[4,9]))
  raw_data = read.csv2('ri_2005', sep='', header=F)
  res[6]=as.numeric(as.character(raw_data[4,9]))
  raw_data = read.csv2('ri_2006', sep='', header=F)
  res[7]=as.numeric(as.character(raw_data[4,9]))
  raw_data = read.csv2('ri_2007', sep='', header=F)
  res[8]=as.numeric(as.character(raw_data[4,9]))
  raw_data = read.csv2('ri_2008', sep='', header=F)
  res[9]=as.numeric(as.character(raw_data[4,9]))
  raw_data = read.csv2('ri_2009', sep='', header=F)
  res[10]=as.numeric(as.character(raw_data[4,9]))
  raw_data = read.csv2('ri_2010', sep='', header=F)
  res[11]=as.numeric(as.character(raw_data[4,9]))
  return(res)
}

randomLog = readRandom()

plotarBoxPlots = function(){
#   year=2000
  for (year in 2000:2010){
    nameOld=parse(text=paste("uniform",year,"best", sep=''))
    dataOld=eval(nameOld)
    #nameEtas=parse(text=paste("etasGaModel",year,"Best", sep=''))
    #dataEtas=eval(nameEtas)
    boxplot(dataOld,riLog[year%%2000+1], randomLog[year%%2000+1], main=year, 
            names=c("GAModel", "RI", "randomModel"), ylab="Valores de log-likelihood")
  }
}
plotarBoxPlots()

calcPowerTest = function(){
  for (year in 2000:2010){
    print(year)
    nameOld=parse(text=paste("uniform",year,"best", sep=''))
    dataOld=eval(nameOld)
    power=power.t.test(delta=50, sd = sd(dataOld),power = .95,
                 type = c("one.sample"), alternative = "two.sided")
    print(power)
  }
}
calcPowerTest()

