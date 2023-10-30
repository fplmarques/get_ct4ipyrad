# get_ct4ipyrad

The scripts can be used to select in-sample-clustering (ISC) and Between-sample-clustering (BSC) thresholds in iPYRAD studies according to the protocol suggested by **Hühn *et al*. (2022)**.

## iPYRAD should be run in two stages:

1. Run your dataset using multiple values for parameter [14] ([clust_threshold]: Clustering threshold for de novo assembly) for steps 1 to 5 (-s 12345). Following, identify the optimal in-sample clustering threshold (see below);
2. For the selected in-sample clustering threshold run iPYRAD for multiple values of the clustering threshold for steps 6 and 7 (-s 67). Following identify the optimal between-sample clustering threshold (see below).

## To get In-sample Cluster Thresholds

```bash
./get_cluster_stats.py -p 's3_cluster_stats_*.txt'
./get_consens_stats.py -p 's5_consens_stats_*.txt'
./plot_ISC_graphs.r
```

This code should generate the following PDF file:

<p align="center" width="100%">
    <img src="/figures/ipyrad_threshold_stats_ISC.jpg" alt="Local Image" width="40%" height="50%">
</p>


## To get Between-sample Cluster Thresholds

```bash
./parse_stats_files.py -p 'any_prefix_stats_*.txt'
plot_BSC_graphs.r
```

<p align="center" width="100%">
    <img src="/figures/ipyrad_threshold_stats_BSC.jpg" alt="Local Image" width="40%" height="50%">
</p>

## References
- **Hühn *et al*. (2022)** How challenging RADseq data turned out to favor coalescent-based species tree inference. A case study in Aichryson (Crassulaceae). Molecular Phylogenetics and Evolution 167: e107342 [DOI](https://doi.org/10.1016/j.ympev.2021.107342)
