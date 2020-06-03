args <- commandArgs(trailingOnly=TRUE)

genome_size = as.numeric(args[1])
numTags = as.numeric(args[2])

## writes to Rplots.pdf by default
hist(rbinom(10000,numTags,1/genome_size), breaks=1000)
