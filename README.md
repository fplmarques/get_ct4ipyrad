# get_ct4ipyrad
## To get Inter sample cluster thresholds

```bash
./get_cluster_stats.py -p 's3_cluster_stats_*.txt'
./get_consens_stats.py -p 's5_consens_stats_*.txt'
./plot_ISC_graphs.r
```

This code should generate the following PDF file:

![Local Image](/figures/ipyrad_threshold_stats_ISC.jpg)
