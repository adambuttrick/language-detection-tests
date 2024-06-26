import csv
import sys
import os
import argparse


def load_results_set(f):
    with open(f, 'r+', encoding='utf-8-sig') as f_in:
        reader = csv.DictReader(f_in)
        results_set = [row for row in reader]
        for row in results_set:
            row['match'] = calculate_match(row)
    return results_set


def calculate_match(row):
    if not row['detected_language']:
        return 'NP'
    elif row['label_lang'] and row['detected_language'] in row['label_lang']:
        return 'Y'
    elif row['detected_language'] and row['detected_language'] not in row['label_lang']:
        return 'N'


def calculate_counts(results_set):
    true_pos = sum(1 for row in results_set if row['match'] == 'Y')
    false_pos = sum(1 for row in results_set if row['match'] == 'N')
    false_neg = sum(1 for row in results_set if row['match'] == 'NP')
    print(true_pos, false_pos, false_neg)
    return true_pos, false_pos, false_neg


def safe_div(n, d, default_ret=0):
    return n / d if d != 0 else default_ret


def calculate_metrics(true_pos, false_pos, false_neg):
    precision = safe_div(true_pos, true_pos + false_pos)
    recall = safe_div(true_pos, true_pos + false_neg)
    f1_score = safe_div(2 * precision * recall, precision + recall)
    beta = 0.5
    f0_5_score = safe_div((1 + beta**2) * (precision * recall),
                          (beta**2 * precision) + recall)
    return precision, recall, f1_score, f0_5_score


def write_to_csv(filename, precision, recall, f1_score, f0_5_score):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Precision", "Recall", "F1 Score",
                         "F0.5 Score"])
        writer.writerow([precision, recall, f1_score, f0_5_score])


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Calculate f-scores for a given CSV file.')
    parser.add_argument('-i', '--input', help='Input CSV file', required=True)
    parser.add_argument('-o', '--output', help='Output CSV file', default=None)
    args = parser.parse_args()
    if args.output is None:
        args.output = f'{args.input}_metrics.csv'
    return args


def main():
    args = parse_arguments()
    results_set = load_results_set(args.input)
    true_pos, false_pos, false_neg = calculate_counts(results_set)
    precision, recall, f1_score, f0_5_score = calculate_metrics(
        true_pos, false_pos, false_neg)
    print(f"Precision: {precision}\nRecall: {recall}\nF1 Score: {f1_score}\nF0.5 Score: {f0_5_score}")
    write_to_csv(args.output, precision, recall,
                 f1_score, f0_5_score)


if __name__ == "__main__":
    main()
