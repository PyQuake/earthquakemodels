setwd("~/Documents/Estudos/UnB/GA/projeto-ga/simpleGA/simpleGA_v2.0/logBook")
library("Hmisc", lib.loc="/Library/Frameworks/R.framework/Versions/3.1/Resources/library")
mediaGeracaoOld <- function(file, n){
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

mediaMelhorGeracaoOld <- function(file, n){
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

uniform2000 = mediaGeracaoOld("2000_Uniform.txt", 0)
uniform2001 = mediaGeracaoOld("2001_Uniform.txt", 1)
uniform2002 = mediaGeracaoOld("2002_Uniform.txt", 2)
uniform2003 = mediaGeracaoOld("2003_Uniform.txt", 3)
uniform2004 = mediaGeracaoOld("2004_Uniform.txt", 4)
uniform2005 = mediaGeracaoOld("2005_Uniform.txt", 5)
uniform2006 = mediaGeracaoOld("2006_Uniform.txt", 6)
uniform2007 = mediaGeracaoOld("2007_Uniform.txt", 7)
uniform2008 = mediaGeracaoOld("2008_Uniform.txt", 8)
uniform2009 = mediaGeracaoOld("2009_Uniform.txt", 9)
uniform2010 = mediaGeracaoOld("2010_Uniform.txt", 10)

uniform2000best = mediaMelhorGeracaoOld("2000_Uniform.txt", 0)
uniform2001best = mediaMelhorGeracaoOld("2001_Uniform.txt", 1)
uniform2002best = mediaMelhorGeracaoOld("2002_Uniform.txt", 2)
uniform2003best = mediaMelhorGeracaoOld("2003_Uniform.txt", 3)
uniform2004best = mediaMelhorGeracaoOld("2004_Uniform.txt", 4)
uniform2005best = mediaMelhorGeracaoOld("2005_Uniform.txt", 5)
uniform2006best = mediaMelhorGeracaoOld("2006_Uniform.txt", 6)
uniform2007best = mediaMelhorGeracaoOld("2007_Uniform.txt", 7)
uniform2008best = mediaMelhorGeracaoOld("2008_Uniform.txt", 8)
uniform2009best = mediaMelhorGeracaoOld("2009_Uniform.txt", 9)
uniform2010best = mediaMelhorGeracaoOld("2010_Uniform.txt", 10)

setwd("~/Documents/Estudos/Tsukuba/earthquakemodels/Zona/etasGaModel")
mediaGeracaoEtas <- function(file){
  raw_data = read.csv2(file, sep='', header=F)
  
  soma = rep(0, 100)
  for (i in 1:10){
    for(j in 1:100){
      soma[j]  = as.numeric(as.character(
        raw_data[((i-1)*100)+j,4])) + soma[j]
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
        raw_data[((i-1)*100)+j,5])) + soma[j]
    }  
  }
  soma = soma/10
  return(soma)
}
etasGaModel2000 = mediaGeracaoEtas("gaWithMag_2000_logbook_R.txt")
etasGaModel2001 = mediaGeracaoEtas("gaWithMag_2001_logbook_R.txt")
etasGaModel2002 = mediaGeracaoEtas("gaWithMag_2002_logbook_R.txt")
etasGaModel2003 = mediaGeracaoEtas("gaWithMag_2003_logbook_R.txt")
etasGaModel2004 = mediaGeracaoEtas("gaWithMag_2004_logbook_R.txt")
etasGaModel2005 = mediaGeracaoEtas("gaWithMag_2005_logbook_R.txt")
etasGaModel2006 = mediaGeracaoEtas("gaWithMag_2006_logbook_R.txt")
etasGaModel2007 = mediaGeracaoEtas("gaWithMag_2007_logbook_R.txt")
etasGaModel2008 = mediaGeracaoEtas("gaWithMag_2008_logbook_R.txt")
etasGaModel2009 = mediaGeracaoEtas("gaWithMag_2009_logbook_R.txt")
etasGaModel2010 = mediaGeracaoEtas("gaWithMag_2010_logbook_R.txt")

etasGaModel2000Best = mediaGeracaoEtasMelhor("gaWithMag_2000_logbook_R.txt")
etasGaModel2001Best = mediaGeracaoEtasMelhor("gaWithMag_2001_logbook_R.txt")
etasGaModel2002Best = mediaGeracaoEtasMelhor("gaWithMag_2002_logbook_R.txt")
etasGaModel2003Best = mediaGeracaoEtasMelhor("gaWithMag_2003_logbook_R.txt")
etasGaModel2004Best = mediaGeracaoEtasMelhor("gaWithMag_2004_logbook_R.txt")
etasGaModel2005Best = mediaGeracaoEtasMelhor("gaWithMag_2005_logbook_R.txt")
etasGaModel2006Best = mediaGeracaoEtasMelhor("gaWithMag_2006_logbook_R.txt")
etasGaModel2007Best = mediaGeracaoEtasMelhor("gaWithMag_2007_logbook_R.txt")
etasGaModel2008Best = mediaGeracaoEtasMelhor("gaWithMag_2008_logbook_R.txt")
etasGaModel2009Best = mediaGeracaoEtasMelhor("gaWithMag_2009_logbook_R.txt")
etasGaModel2010Best = mediaGeracaoEtasMelhor("gaWithMag_2010_logbook_R.txt")

ger2000=t.test(uniform2000, etasGaModel2000)
ger2001=t.test(uniform2001, etasGaModel2001)
ger2002=t.test(uniform2002, etasGaModel2002)
ger2003=t.test(uniform2003, etasGaModel2003)
ger2004=t.test(uniform2004, etasGaModel2004)
ger2005=t.test(uniform2005, etasGaModel2005)
ger2006=t.test(uniform2006, etasGaModel2006)
ger2007=t.test(uniform2007, etasGaModel2007)
ger2008=t.test(uniform2008, etasGaModel2008)
ger2009=t.test(uniform2009, etasGaModel2009)
ger2010=t.test(uniform2010, etasGaModel2010)

best2000=t.test(uniform2000best, etasGaModel2000Best)
best2001=t.test(uniform2001best, etasGaModel2001Best)
best2002=t.test(uniform2002best, etasGaModel2002Best)
best2003=t.test(uniform2003best, etasGaModel2003Best)
best2004=t.test(uniform2004best, etasGaModel2004Best)
best2005=t.test(uniform2005best, etasGaModel2005Best)
best2006=t.test(uniform2006best, etasGaModel2006Best)
best2007=t.test(uniform2007best, etasGaModel2007Best)
best2008=t.test(uniform2008best, etasGaModel2008Best)
best2009=t.test(uniform2009best, etasGaModel2009Best)
best2010=t.test(uniform2010best, etasGaModel2010Best)