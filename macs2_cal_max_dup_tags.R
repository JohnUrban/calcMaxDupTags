## Read in arguments
args <- commandArgs(trailingOnly=TRUE)

## 
genome_size <- as.numeric(args[1])
numTags <- as.numeric(args[2])
p <- as.numeric(args[3])

cal_max_dup_tags <- function(genome_size, numTags, p){
  for (x in 1:numTags){
    if (p > pbinom(x, numTags, 1/genome_size, lower.tail=FALSE)){
      return(x)
   }
  }
return(numTags)
}

maxTags <- cal_max_dup_tags(genome_size, numTags, p)

cmd <- paste0("echo ", maxTags)
system(cmd)
