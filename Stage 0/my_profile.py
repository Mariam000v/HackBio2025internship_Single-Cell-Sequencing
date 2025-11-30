#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
my_profile.py

Simple script printing my profile and a fragment of my favorite gene (OXTR).
"""

my_info = {
    "name": "Mariam Mohamed",
    "slack_username": "Mariam000v",
    "country": "UAE",
    "hobbies": ["watching movies", "learning new things", "cooking"],
    "affiliations": ["AURAK"],
    "favorite_gene": "OXTR (oxytocin receptor)",
    # Reference mRNA fragment from OXTR (Homo sapiens, NM_000916.4)
    "favorite_gene_dna": (
        "ATGGAGGGCGCGCTCGCAGCCAACTGGAGCGCCGAGGCAGCCAACGCCAGCGCCGCGCCG"
        "CCGGGGGCCGAGGGCAACCGCACCGCCGGACCCCCGCGGCGCAACGAGGCCCTGGCGCGC"
        "GTGGAGGTGGCGGTGCTGTGTCTC"  # truncated fragment
    )
}

def print_profile(info):
    print("Name:", info["name"])
    print("Slack Username:", info["slack_username"])
    print("Country:", info["country"])
    print("Hobbies:", ", ".join(info["hobbies"]))
    print("Affiliations:", ", ".join(info["affiliations"]))
    print("Favorite Gene:", info["favorite_gene"])
    print("Favorite Gene DNA Sequence (fragment):", info["favorite_gene_dna"])

if __name__ == "__main__":
    print_profile(my_info)
