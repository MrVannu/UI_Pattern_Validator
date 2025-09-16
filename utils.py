##############################################################
# Project:       Thesis - Fifteen Patterns To Help Developers To Overcome The Visualisation Impedance Mismatch
# Author:        Vannuccini Luca
# Last Updated:  2025-09-16
# Version:       1.0
# Description:   Utility functions to detect UI patterns in user interaction data
##############################################################

import pandas as pd
import pandas as pd
import numpy as np
from collections import Counter


def detect_immediate_visual_feedback_pattern(csv_file):
    df = pd.read_csv(csv_file, parse_dates=['timestamp'])
    print(f"Reviewed file: {csv_file}")
    df = df.sort_values(by=['user_id', 'interaction_id', 'timestamp'])
    
    df['time_diff'] = df.groupby(['user_id', 'interaction_id'])['timestamp'].diff().dt.total_seconds()
    
    impatience = df[df['time_diff'] < 0.5]
    pattern_missing = df[df['time_diff'] < 1]
    
    if not pattern_missing.empty:
        print("❗ Missing pattern: no visual feedback detected (<1s)")
        print(pattern_missing)
        print("\n")    
    if not impatience.empty:
        print("❗ Missing pattern: impatience detected (<500 ms)")
        print(impatience)
    else:
        print("✔ Pattern is impelmented.")

def shannon_entropy(values):
    total = len(values)
    counts = Counter(values)
    probs = [count/total for count in counts.values()]
    H = -sum(p * np.log2(p) for p in probs)
    H_norm = H / np.log2(len(counts)) if len(counts) > 1 else 0
    return H, H_norm, counts

def detect_autocomplete_pattern(csv_file):
    df = pd.read_csv(csv_file)
    print(f"Reviewed file: {csv_file}")
    
    for field_id, group in df.groupby("field_id"):
        values = group["input_value"].tolist()
        H, H_norm, counts = shannon_entropy(values)
        
        total = len(values)
        most_common_val, most_common_count = counts.most_common(1)[0]
        coverage = most_common_count / total
        
        print(f"Analysed Field(s): {field_id}")
        print(f"- Distinct values: {len(counts)}")
        print(f"- Max coverage: {coverage*100:.1f}% ({most_common_val})")
        print(f"- Normalized Entropy: {H_norm:.3f}")
        
        if coverage >= 0.7:
            print("❗ Cadidate for AUTOCOMPLETE (coverage ≥70%)")
        if H_norm < 0.3:
            print("❗ Low variety (H_norm <0.3) → Missing pattern")
        if coverage < 0.7 and H_norm >= 0.3:
            print("✔ Pattern is impelmented")

def detect_customization_pattern(csv_file):
    df = pd.read_csv(csv_file)
    print(f"Reviewed file: {csv_file}")
    
    results = []
    
    for (user, screen, key), group in df.groupby(["user_id", "screen_id", "config_key"]):
        counts = Counter(group["config_value"])
        total = len(group)
        most_common_val, most_common_count = counts.most_common(1)[0]
        coverage = most_common_count / total
        
        # No per-user warning (until needed)
        #if total >= 2 and coverage >= 0.8:
        #   results.append((user, screen, key, most_common_val, coverage, "❗ Repeated configuration (≥80%)"))
    
    for (screen, key), group in df.groupby(["screen_id", "config_key"]):
        user_pref = {}
        for user, user_group in group.groupby("user_id"):
            val, _ = Counter(user_group["config_value"]).most_common(1)[0]
            user_pref[user] = val
        
        counts = Counter(user_pref.values())
        most_common_val, most_common_count = counts.most_common(1)[0]
        coverage = most_common_count / len(user_pref)
        
        if coverage > 0.51:
            results.append(("ALL", screen, key, most_common_val, coverage, "❗ Preset global candidate (≥51% users)"))
    
    # Report
    if results:
        for r in results:
            user, screen, key, val, cov, msg = r
            # ALL means global preset candidate          
            print(f"{msg}: user={user}, screen={screen}, key={key}, val={val}, coverage={cov:.2f}")
    else:
        print("✔ Pattern is impelmented")

