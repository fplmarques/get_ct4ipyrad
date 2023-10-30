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
    filtered_by_maxH = data[["filtered_by_maxH"]]
    filtered_by_maxH = filtered_by_maxH.rename(
        columns={"filtered_by_maxH": f"filtered_by_maxH_{threshold}"}
    )
    heterozygosity = data[["heterozygosity"]]
    heterozygosity = heterozygosity.rename(
        columns={"heterozygosity": f"heterozygosity_{threshold}"}
    )
    return filtered_by_maxH, heterozygosity


def get_list_of_files(directory, file_pattern):
    files = glob.glob(f"{directory_path}/{file_pattern}")
    return files


# Get the current directory path
directory_path = os.getcwd()

# Parse command-line arguments
parser = argparse.ArgumentParser(
    description="Process consensus stats (s5) iPYRAD output files."
)
parser.add_argument(
    "-p",
    "--pattern",
    type=str,
    default="s5_consens_stats_*.txt",
    help="File pattern to match (default: s5_consens_stats_*.txt). Example usage: ./get_consens_stats.py -p 's5_consens_stats_*.txt'",
)
args = parser.parse_args()

s5_files = get_list_of_files(directory_path, args.pattern)
s5_files.sort()


#
## Main fucntion
#
def main():
    print(f"Starting compiling information from {len(s5_files)} files:")
    print(f"    Parsing first file: {s5_files[0].split('/')[-1]}")
    filtered_by_maxH4all, heterozygosity4all = get_data(s5_files[0])

    for file in s5_files[1:]:
        print(f"    Parsing: {file.split('/')[-1]}")
        filtered_by_maxH, heterozygosity = get_data(file)

        filtered_by_maxH4all = filtered_by_maxH4all.merge(
            filtered_by_maxH, left_index=True, right_index=True
        )

        heterozygosity4all = heterozygosity4all.merge(
            heterozygosity, left_index=True, right_index=True
        )

    # Writing the dataframes to csv files
    print()
    print(
        "Writing the dataframes to tsv files:filtered_by_maxH4all.tsv and heterozygosity4all.tsv"
    )
    filtered_by_maxH4all.to_csv("filtered_by_maxH4all.tsv", sep="\t", index=False)
    heterozygosity4all.to_csv("heterozygosity4all.tsv", sep="\t", index=False)


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
        default="s5_consens_stats_*.txt",
        help="File pattern to match (default: s5_consens_stats_*.txt). Example usage: ./get_cluster_stats.py -p 's5_consens_stats_*.txt'",
    )
    args = parser.parse_args()

    s5_files = get_list_of_files(directory_path, args.pattern)
    s5_files.sort()

    main()
