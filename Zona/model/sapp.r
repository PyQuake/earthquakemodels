library("SAPP", lib.loc="/Library/Frameworks/R.framework/Versions/3.2/Resources/library")
setwd("~/Documents/estudos/unb/earthquakemodels/code")
options(scipen=999)

a=etasim1(1.0, 2588, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/etasim1.txt")

