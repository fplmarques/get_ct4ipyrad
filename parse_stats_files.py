#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Apr  2 15:29:37 2020
"""

import argparse
import glob
import os
import re
from time import process_time_ns

import pandas as pd
from numpy import poly

# Get the current directory path
directory_path = os.getcwd()


def extract_retained_loci(file_path):
    retained_loci = None

    with open(file_path, "r") as file:
        for line in file:
            # Use a regular expression to match the pattern
            get_retained_loci = re.match(
                r"^total_filtered_loci\s+\d+\s+\d+\s+(\d+)", line
            )
            if get_retained_loci:
                retained_loci = int(
                    get_retained_loci.group(1)
                )  # Extract and convert to an integer

            get_var_0 = re.match(r"^0\s+(\d+)\s+\d+\s+\d+\s+\d+", line)
            if get_var_0:
                var_0 = int(get_var_0.group(1))

            get_sum_var = re.match(r"^\d+\s+\d+\s+(\d+)\s+\d+\s+\d+", line)
            if get_sum_var:
                sum_var = int(get_sum_var.group(1))

            get_missing_snps = re.match(
                r"^snps matrix size: \(\d+, \d+\), (\d+\.\d+)% missing sites.", line
            )
            if get_missing_snps:
                missing_snps = float(get_missing_snps.group(1))

    return [retained_loci, var_0, sum_var, missing_snps]


def get_list_of_files(directory, file_pattern):
    files = glob.glob(f"{directory_path}/{file_pattern}")
    return files


# Example usage:


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process iPYRAD output files.")
    parser.add_argument(
        "-p",
        "--pattern",
        type=str,
        default="steatogenys_ISC_95_231027_stats_*.txt",
        help="File pattern to match (default: anything_ISC_stats_*.txt). Example usage: ./parse_stats_files.py -p 'steatogenys_ISC_95_231027_stats_*.txt'",
    )
    args = parser.parse_args()

    stats_files = get_list_of_files(directory_path, args.pattern)
    stats_files.sort()
    print(f"Starting compiling information from {len(stats_files)} files:")

    bsc = {
        "threshold": [],
        "retained_loci": [],
        "polymorphic_loci": [],
        "sum_var": [],
        "missing_snps": [],
        "new_polymorphic_loci": [],
    }

    for file in stats_files:
        print(f"    Parsing: {file.split('/')[-1]} ...", end="")
        print("Done!")
        threshold = int(file.split("_")[-1].split(".")[0])
        retained_loci, var_0, sum_var, missing_snps = extract_retained_loci(file)
        polymorphic_loci = retained_loci - var_0

        # addint info to dictionary
        bsc["threshold"].append(threshold)
        bsc["retained_loci"].append(retained_loci)
        bsc["polymorphic_loci"].append(polymorphic_loci)
        bsc["sum_var"].append(sum_var)
        bsc["missing_snps"].append(missing_snps)

        # print(f"{retained_loci}\t{polymorphic_loci}\t{sum_var}\t{missing_snps}")

    for n in range(len(bsc["polymorphic_loci"])):
        if n == 0:
            bsc["new_polymorphic_loci"].append("NA")
        else:
            bsc["new_polymorphic_loci"].append(
                bsc["polymorphic_loci"][n - 1] - bsc["polymorphic_loci"][n]
            )

    # converting to dataframe
    bsc = pd.DataFrame(bsc)

    # Export the data frame to a TSV file
    bsc.to_csv("bsc_dataframe.tsv", sep="\t", index=False)
    print()
    print(f'Dataframe saved to "bsc_dataframe.tsv" file.')


if __name__ == "__main__":
    main()
