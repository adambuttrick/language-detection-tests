import csv
import json
import argparse


def parse_json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ror_id', 'name', 'label', 'label_lang', 'country'])
        for obj in data:
            ror_id = obj.get('id', '')
            name = obj.get('name', '')
            country = obj.get('country').get('country_code')
            if 'labels' in obj:
                for label in obj['labels']:
                    label_text = label.get('label', '')
                    label_lang = label.get('iso639', '')
                    writer.writerow([ror_id, name, label_text, label_lang, country])


def parse_args():
    parser = argparse.ArgumentParser(description='Process ROR data dump to CSV containing ID, name, label, and country information.')
    parser.add_argument('-d', '--data_dump', type=str,
                        help='Path to input JSON file')
    parser.add_argument('-o', '--output_csv', type=str,
                        help='Path to output CSV file')
    return parser.parse_args()


def main():
    args = parse_args()
    parse_json_to_csv(args.data_dump, args.output_csv)


if __name__ == "__main__":
    main()
