#!/usr/bin/R
#
## libraries
#
library(svglite)
#
## data
#

clusters_total <- read.table("clusters_total4all.tsv", header = TRUE, sep = "\t")
avg_depth_total <- read.table("avg_depth_total4all.tsv", header = TRUE, sep = "\t")
filtered_by_maxH <- read.table("filtered_by_maxH4all.tsv", header = TRUE, sep = "\t")
heterozygosity <- read.table("heterozygosity4all.tsv", header = TRUE, sep = "\t")

thresholds <- c(80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99)


graph <- function(){
par(mfrow=c(4,1))
boxplot(clusters_total, names=thresholds, ylab="Cluster Total", xlab="", col="#669966", main="Total Number of Clusters (ISC)")
polygon(c(14.5, 14.5, 17.5, 17.5), c(0, max(clusters_total), max(clusters_total), 0), col="#CCCCCC", border=NA, alpha=0.2, density = 20)

boxplot(avg_depth_total, names=thresholds, ylab="Avg. depth total", xlab="", col="#669966", main="Average Toral Depth (ISC)")
polygon(c(14.5, 14.5, 17.5, 17.5), c(0, max(avg_depth_total), max(avg_depth_total), 0), col="#CCCCCC", border=NA, alpha=0.2, density = 20)


boxplot(filtered_by_maxH, names=thresholds, ylab="Filtered by maxH", xlab="", col="#669966", main="Filtered by Max Heterozygosity (ISC)")
polygon(c(8.5, 8.5, 16.5, 16.5), c(0, max(filtered_by_maxH), max(filtered_by_maxH), 0), col="#CCCCCC", border=NA, alpha=0.2, density = 20)

boxplot(heterozygosity, names=thresholds, ylab="Heterozygozity", xlab="ISC CT", col="#669966", main="Heterozygosity (ISC)")
polygon(c(13.5, 13.5, 16.5, 16.5), c(0, max(heterozygosity), max(heterozygosity), 0), col="#CCCCCC", border=NA, alpha=0.2, density = 20)
}


pdf(file="ipyrad_threshold_stats_ISC.pdf", width=4, height=12)
graph()
dev.off()

svglite(file="ipyrad_threshold_stats_ISC.svg", width=4, height=12)
graph()
dev.off()
