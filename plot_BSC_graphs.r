#!/usr/bin/Rscript
#
## libraries
#
library(svglite)
#
## data
#

bsc_data <- read.table("bsc_dataframe.tsv", header = TRUE, sep = "\t")

graph <- function(){
par(mfrow=c(4,1))
plot(bsc_data$threshold,bsc_data$retained_loci, xlab="", ylab="Retained loci", pch = 19, col="#CC6600", type = "b", lty = 1, lwd = 2, xaxt='n', main="Retained loci across samples")
polygon(c(95.5, 95.5, 96.5, 96.5), c(0, max(bsc_data$retained_loci+50), max(bsc_data$retained_loci+50), 0), col="#CCCCCC", border=NA, alpha=0.2, density = 20)
axis(side=1, at=seq(80, 99, by=1))

plot(bsc_data$threshold,bsc_data$sum_var, xlab="", ylab="Sum VAR", pch = 19, col="#CC6600", type = "b", lty = 1, lwd = 2, xaxt='n', main="Number of variable sites across samples")
polygon(c(92.5, 92.5, 93.5, 93.5), c(0, max(bsc_data$sum_var+50), max(bsc_data$sum_var+50), 0), col="#CCCCCC", border=NA, alpha=0.2, density = 20)
axis(side=1, at=seq(80, 99, by=1))

plot(bsc_data$threshold,bsc_data$missing_snps, xlab="", ylab="% missing SNPs", pch = 19, col="#CC6600", type = "b", lty = 1, lwd = 2, xaxt='n', main="Percentage of missing SNPs across samples")
polygon(c(94.5, 94.5, 95.5, 95.5), c(0, max(bsc_data$missing_snps+1), max(bsc_data$missing_snps+1), 0), col="#CCCCCC", border=NA, alpha=0.2, density = 20)
axis(side=1, at=seq(80, 99, by=1))

plot(bsc_data$threshold,bsc_data$new_polymorphic_loci, xaxt = "n", ylab="New polimorphoc loci", xlab="BSC CT", pch = 19, col="#CC6600", type = "b", lty = 1, lwd = 2, main="Number of new polymorphic sites") 

polygon(c(98.5, 98.5, 99.5, 99.5), c(-1400, 14000, 14000, -1200), col="#CCCCCC", border=NA, alpha=0.2, density = 20)
# vector of labels
labels <- c("","81-80","82-81","83-82","84-83","85-84","86-85","87-86","88-87","89-88","90-89","91-90","92-91","93-92","94-93","95-94","96-95","97-96","98-97","99-98")
# Set custom X-axis labels
axis(side = 1, at = bsc_data$threshold, labels = labels, cex.axis = 0.8, las = 2)
}



pdf(file="ipyrad_threshold_stats_BSC.pdf", width=4, height=12)
graph()
dev.off()

svglite(file="ipyrad_threshold_stats_BSC.svg", width=4, height=12)
graph()
dev.off()

