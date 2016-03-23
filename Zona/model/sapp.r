library("SAPP", lib.loc="/Library/Frameworks/R.framework/Versions/3.2/Resources/library")
setwd("~/Documents/estudos/unb/earthquakemodels/code")
options(scipen=999)

a=etasim1(1.0, 25880, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/etasim1.txt")


a=etasim1(1.0, 2588, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KantoNP2006etasim1.txt")
a=etasim1(1.0, 2268, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KantoModel2006oetasim1.txt")
a=etasim1(1.0, 3973, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KantoNP2007etasim1.txt")
a=etasim1(1.0, 2303, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KantoModel2007oetasim1.txt")
a=etasim1(1.0, 2583, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KantoNP2008etasim1.txt")
a=etasim1(1.0, 2330, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KantoModel2008oetasim1.txt")
a=etasim1(1.0, 2702, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KantoNP2009etasim1.txt")
a=etasim1(1.0, 2290, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KantoModel2009oetasim1.txt")
a=etasim1(1.0, 2663, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KantoNP2010etasim1.txt")
a=etasim1(1.0, 2353, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KantoModel2010oetasim1.txt")

a=etasim1(1.0, 1802, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KansaiNP2006etasim1.txt")
a=etasim1(1.0, 1618, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KansaiModel2006oetasim1.txt")
a=etasim1(1.0, 1782, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KansaiNP2007etasim1.txt")
a=etasim1(1.0, 1608, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KansaiModel2007oetasim1.txt")
a=etasim1(1.0, 1744, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KansaiNP2008etasim1.txt")
a=etasim1(1.0, 1614, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KansaiModel2008oetasim1.txt")
a=etasim1(1.0, 1695, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KansaiNP2009etasim1.txt")
a=etasim1(1.0, 1615, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KansaiModel2009oetasim1.txt")
a=etasim1(1.0, 1878, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KansaiNP2010etasim1.txt")
a=etasim1(1.0, 1624, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/KansaiModel2010oetasim1.txt")

a=etasim1(1.0, 2938, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/EastJapanNP2006etasim1.txt")
a=etasim1(1.0, 2815, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/EastJapanModel2006oetasim1.txt")
a=etasim1(1.0, 2930, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/EastJapanNP2007etasim1.txt")
a=etasim1(1.0, 2749, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/EastJapanModel2007oetasim1.txt")
a=etasim1(1.0, 11368, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/EastJapanNP2008etasim1.txt")
a=etasim1(1.0, 2988, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/EastJapanModel2008oetasim1.txt")
a=etasim1(1.0, 8694, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/EastJapanNP2009etasim1.txt")
a=etasim1(1.0, 2799, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/EastJapanModel2009oetasim1.txt")
a=etasim1(1.0, 4375, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/EastJapanNP2010etasim1.txt")
a=etasim1(1.0, 2910, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/EastJapanModel2010oetasim1.txt")

a=etasim1(1.0, 2815, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/TohokuNP2006etasim1.txt")
a=etasim1(1.0, 975, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/TohokuModel2006oetasim1.txt")
a=etasim1(1.0, 2749, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/TohokuNP2007etasim1.txt")
a=etasim1(1.0, 975, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/TohokuModel2007oetasim1.txt")
a=etasim1(1.0, 2988, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/TohokuNP2008etasim1.txt")
a=etasim1(1.0, 1034, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/TohokuModel2008oetasim1.txt")
a=etasim1(1.0, 2799, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/TohokuNP2009etasim1.txt")
a=etasim1(1.0, 969, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/TohokuModel2009oetasim1.txt")
a=etasim1(1.0, 2910, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/TohokuNP2010etasim1.txt")
a=etasim1(1.0, 1003, 3.0, 3.0, c(0.2e-02, 0.4e-02, 0.3e-02, 0.24e+01, 0.13e+01))
write.csv(a, file = "../Zona/paper_exp/TohokuModel2010oetasim1.txt")

