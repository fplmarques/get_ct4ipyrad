# get_ct4ipyrad
## To get Inter-sample Cluster Thresholds

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
./parse_stats_files.py -p 'steatogenys_ISC_95_231027_stats_*.txt'
plot_BSC_graphs.r
```

<p align="center" width="100%">
    <img src="/figures/ipyrad_threshold_stats_BSC.jpg" alt="Local Image" width="40%" height="50%">
</p>
