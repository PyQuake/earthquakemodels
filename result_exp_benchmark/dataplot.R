# Loading all data into a huge data frame:
require(data.table)
require(ggplot2)
require(ggthemes)
require(scales) 
require(gridExtra)
require(grid)

# setwd
setwd("~/Documents/estudos/earthquakemodels/result_exp_benchmark/")

# load data
loadDimension <- function(dim){
  workdir <- paste0("results_UniformGaussian",dim,"D/")
  ddd <- NULL
  for (j in 1:24) {
    dd <- NULL
    
    for (i in 2:25) {
      d <- read.csv(paste0(workdir,"f",j,"_",i,".txt"),header = FALSE)
      names(d) <- c("gen","min","mean","max","sd","rep")
      k <- rep(i,nrow(d))
      d <- cbind(d,k)
      dd <- rbind(dd,d)
    }
    f <- rep(j,nrow(dd))
    dd <- cbind(dd,f)
    ddd <- rbind(ddd,dd)
   
    }
  return (ddd)
}

k_subsetting <- function(data, k_interval = NULL){
  if (!is.null(k_interval)){
    data <- data[k %in% c(k_interval)]
  }
  else{
    data <- data
  } 
}

f_subsetting <- function(data, f_interval = NULL){
  if (!is.null(f_interval)){
    data <- data[f %in% c(f_interval)]
  }
  else{
    data <- data
  } 
}

#function to plot k versus min value given an interval (function goes in graph)
k_min_plot <- function(data10, data20, data40, k_interval = NULL, f_interval = NULL, log = FALSE){
  means10 <- k_subsetting(data10, k_interval)
  means20 <- k_subsetting(data20, k_interval)
  means40 <- k_subsetting(data40, k_interval)
  
  means10 <- f_subsetting(means10, f_interval)
  means20 <- f_subsetting(means20, f_interval)
  means40 <- f_subsetting(means40, f_interval)
  
  if (log == TRUE){
    means10$min <- as.numeric(lapply(X = means10$min, FUN = function(X){ if (X>0){log(X)} else{X}}))
    means20$min <- as.numeric(lapply(X = means20$min, FUN = function(X){ if (X>0){log(X)} else{X}}))
    means40$min <- as.numeric(lapply(X = means40$min, FUN = function(X){ if (X>0){log(X)} else{X}}))
  }
  
  p10<- ggplot(means10, aes(k, min, color = f, group = means10$f))+
    geom_point(col = 'red')+
    geom_line()+
    scale_color_gradient()
  p10$labels$colour <- "Function"
  p20<- ggplot(means10, aes(k, min, color = f, group = means20$f))+
    geom_point(col = 'red')+
    geom_line()+
    scale_color_gradient()
  p20$labels$colour <- "Function"
  p40<- ggplot(means40, aes(k, min, color = f, group = means40$f))+
    # geom_ribbon(aes(ymin = 0, ymax = means40$min, fill = means40$f), alpha = 0.3)+
    geom_point(col = 'red')+
    geom_line()+
    scale_color_gradient()
  p40$labels$colour <- "Function"
  grid.arrange(arrangeGrob(p10+theme(axis.title.y = element_blank(),axis.title.x = element_blank()),
                           p20+theme(axis.title.y = element_blank(),axis.title.x = element_blank()),
                           p40+theme(axis.title.y = element_blank(),axis.title.x = element_blank()),
                           nrow=3,
                           left = textGrob("Optimum Value found", rot = 90),
                           # top  = textGrob("Function!"),
                           bottom = textGrob("Tournament size")
  )
  )
}
k_min_plot(means10, means20, means40, k_interval = c(2,3))
k_min_plot(means10, means20, means40, log = TRUE)

#function to plot f versus min value given an interval (k goes in graph)
f_min_plot <- function(data10, data20, data40, k_interval = NULL, f_interval = NULL, log = FALSE){
  means10 <- k_subsetting(data10, k_interval)
  means20 <- k_subsetting(data20, k_interval)
  means40 <- k_subsetting(data40, k_interval)
  
  means10 <- f_subsetting(means10, f_interval)
  means20 <- f_subsetting(means20, f_interval)
  means40 <- f_subsetting(means40, f_interval)
  
  if (log == TRUE){
    means10$min <- as.numeric(lapply(X = means10$min, FUN = function(X){ if (X>0){log(X)} else{X}}))
    means20$min <- as.numeric(lapply(X = means20$min, FUN = function(X){ if (X>0){log(X)} else{X}}))
    means40$min <- as.numeric(lapply(X = means40$min, FUN = function(X){ if (X>0){log(X)} else{X}}))
  }
  
  p10<- ggplot(means10, aes(f, min, color = k, group = means10$k))+
    geom_point(col = 'red')+
    geom_line()+
    scale_color_gradient()
  p10$labels$colour <- "Tour. size"
  p20<- ggplot(means10, aes(f, min, color = k, group = means20$k))+
    geom_point(col = 'red')+
    geom_line()+
    scale_color_gradient()
  p20$labels$colour <- "Tour. size"
  p40<- ggplot(means40, aes(f, min, color = k, group = means40$k))+
    geom_point(col = 'red')+
    geom_line()+
    scale_color_gradient()
  p40$labels$colour <- "Tour. size"
  grid.arrange(arrangeGrob(p10+
                            theme(axis.title.y = element_blank(),
                                  axis.title.x = element_blank(),),
                           p20+
                             theme(axis.title.y = element_blank(),
                                   axis.title.x = element_blank()),
                           p40+
                             theme(axis.title.y = element_blank(),
                                   axis.title.x = element_blank()),
                           nrow=3,
                           left = textGrob("Optimum Value found", rot = 90),
                           # top  = textGrob(" Tournament size"),
                           bottom = textGrob("Function")))
}
f_min_plot(means10, means20, means40, k_interval = c(2,5,10), f_interval = c(2,5,10))

# processing data
## getting data of only the last gen
ddd10 <- loadDimension(10)
ddd20 <- loadDimension(20)
ddd40 <- loadDimension(40)
  
group <- as.data.table(ddd10)
ddd10 <- group[group[, .I[gen == max(gen)], by=list(rep, k, f)]$V1]

group <- as.data.table(ddd20)
ddd20 <- group[group[, .I[gen == max(gen)], by=list(rep, k, f)]$V1]

group <- as.data.table(ddd40)
ddd40 <- group[group[, .I[gen == max(gen)], by=list(rep, k, f)]$V1]

# max(aux[aux$f == 5 & aux$rep == 10, ]$gen)
# unique(aux[aux$f == 4, ]$gen)
# unique(aux[aux$f == 5, ]$gen)


# get the means of the last gen
means10 <- aggregate(ddd10, list(k = ddd10$k, f = ddd10$f), mean)
means10 <- as.data.table(means10)

means20 <- aggregate(ddd20, list(k = ddd20$k, f = ddd20$f), mean)
means20 <- as.data.table(means20)

means40 <- aggregate(ddd40, list(k = ddd40$k, f = ddd40$f), mean)
means40 <- as.data.table(means40)


#plot data
k_min_plot(means10, means20, means40, k_interval = c(2,5,10), f_interval = c(2,5,10))
f_min_plot(means10, means20, means40, f_interval = c(2,5,10, 22,24))
k_min_plot(means10, means20, means40, log = TRUE)
k_min_plot(means10, means20, means40, log = FALSE)

f_min_plot(means10, means20, means40, log = TRUE)
f_min_plot(means10, means20, means40, log = FALSE)

   

