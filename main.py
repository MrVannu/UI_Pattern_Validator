##############################################################
# Project:       Thesis - Fifteen Patterns To Help Developers To Overcome The Visualisation Impedance Mismatch
# Author:        Vannuccini Luca
# Last Updated:  2025-09-16
# Version:       1.0
# Description:   Main script to run the pattern detectors
##############################################################

import argparse
from utils import (
    detect_immediate_visual_feedback_pattern,
    detect_autocomplete_pattern,
    detect_customization_pattern
)

def main(csv_file=None):
    if csv_file:
        print(f"Running all detectors on provided CSV: {csv_file}\n")
        detect_immediate_visual_feedback_pattern(csv_file)
        detect_autocomplete_pattern(csv_file)
        detect_customization_pattern(csv_file)
    else:
        print("No CSV provided. Running default test datasets.\n")
        # DETECTOR FOR "IMMEDIATE VISUAL FEEDBACK" PATTERN
        detect_immediate_visual_feedback_pattern('res/pattern1.csv')
        detect_immediate_visual_feedback_pattern('res/pattern1NO.csv')

        # DETECTOR FOR "AUTOCOMPLETE" PATTERN
        detect_autocomplete_pattern("res/pattern2.csv")
        detect_autocomplete_pattern("res/pattern2NO.csv")

        # DETECTOR FOR "CUSTOMISATION" PATTERN
        detect_customization_pattern("res/pattern3.csv")
        detect_customization_pattern("res/pattern3NO.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run UI Pattern Detectors on a CSV file or default test datasets."
    )
    parser.add_argument(
        "csv_file",
        nargs="?",
        default=None,
        help="Optional path to a CSV file with user interaction data"
    )
    args = parser.parse_args()
    main(args.csv_file)