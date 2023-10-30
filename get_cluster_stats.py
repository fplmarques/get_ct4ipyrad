#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:29:37 2020
"""
import argparse
import glob
import os

import numpy as np
import pandas as pd


def get_data(file):
    # getting the threshold value from the file name
    threshold = file.split("_")[-1].split(".")[0]

    # reading the file
    data = pd.read_csv(file, sep="\s+")
    clusters_total = data[["clusters_total"]]
    clusters_total = clusters_total.rename(
        columns={"clusters_total": f"clusters_total_{threshold}"}
    )
    avg_depth_total = data[["avg_depth_total"]]
    avg_depth_total = avg_depth_total.rename(
        columns={"avg_depth_total": f"avg_depth_total_{threshold}"}
    )
    return clusters_total, avg_depth_total


def get_list_of_files(directory, file_pattern):
    files = glob.glob(f"{directory_path}/{file_pattern}")
    return files


# Get the current directory path
directory_path = os.getcwd()

# Parse command-line arguments
parser = argparse.ArgumentParser(
    description="Process cluster stats (s3) iPYRAD output files."
)
parser.add_argument(
    "-p",
    "--pattern",
    type=str,
    default="s3_cluster_stats_*.txt",
    help="File pattern to match (default: s3_cluster_stats_*.txt). Example usage: ./get_cluster_stats.py -p 's3_cluster_stats_*.txt'",
)
args = parser.parse_args()

s3_files = get_list_of_files(directory_path, args.pattern)
s3_files.sort()


#
## Main fucntion
#
def main():
    print(f"Starting compiling information from {len(s3_files)} files:")
    print(f"    Parsing first file: {s3_files[0].split('/')[-1]}")
    clusters_total4all, avg_depth_total4all = get_data(s3_files[0])

    for file in s3_files[1:]:
        print(f"    Parsing: {file.split('/')[-1]}")
        clusters_total, avg_depth_total = get_data(file)

        clusters_total4all = clusters_total4all.merge(
            clusters_total, left_index=True, right_index=True
        )

        avg_depth_total4all = avg_depth_total4all.merge(
            avg_depth_total, left_index=True, right_index=True
        )

    # Writing the dataframes to csv files
    print()
    print(
        "Writing the dataframes to tsv files:clusters_total4all.tsv and avg_depth_total4all.tsv"
    )
    clusters_total4all.to_csv("clusters_total4all.tsv", sep="\t", index=False)
    avg_depth_total4all.to_csv("avg_depth_total4all.tsv", sep="\t", index=False)


if __name__ == "__main__":
    # Get the current directory path
    directory_path = os.getcwd()

    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="Process cluster stats (s3) iPYRAD output files."
    )
    parser.add_argument(
        "-p",
        "--pattern",
        type=str,
        default="s3_cluster_stats_*.txt",
        help="File pattern to match (default: s3_cluster_stats_*.txt). Example usage: ./get_cluster_stats.py -p 's3_cluster_stats_*.txt'",
    )
    args = parser.parse_args()

    s3_files = get_list_of_files(directory_path, args.pattern)
    s3_files.sort()

    main()
