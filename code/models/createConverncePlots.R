gaModel25 = read.csv2("EastJapan_2000_Media25gaModel.txt", sep='\n', header=F)
gen = 1:length(gaModel25$V1)
model25 = c(rep("gaModel25",length(gaModel25$V1)))
loglikeValues25 = rep(0, length(gaModel25$V1))
for (k in 1:length(gaModel25$V1)){
  loglikeValues25[k] = as.numeric(levels(gaModel25$V1[k]))[gaModel25$V1[k]]
}

gaModel60 = read.csv2("EastJapan_2000_Media25listaGA_New.txt", sep='\n', header=F)
model60 = c(rep("gaModel60",length(gaModel60$V1)))
loglikeValues60 = rep(0, length(gaModel60$V1))
for (k in 1:length(gaModel60$V1)){
  loglikeValues60[k] = as.numeric(levels(gaModel60$V1[k]))[gaModel60$V1[k]]
}

gen1 = 1:length(gaModel25$V1)
gen2 = 1:length(gaModel60$V1)
gen=c(gen1, gen2)
model = c(model25, model60)
loglikeValues = c(loglikeValues25, loglikeValues60)
c=data.frame(gen, loglikeValues, model)

interaction.plot(c$gen, c$model, c$loglikeValues, col=c('red','blue'), main=paste(region,year))
