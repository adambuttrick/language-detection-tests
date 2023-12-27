import csv
import argparse
import fasttext


MODEL_PATH = "lid.176.bin"
detector = fasttext.load_model(MODEL_PATH)


def detect_language(label):
    try:
        predictions = detector.predict(label, k=1)
        detected_language = predictions[0][0].split("__label__")[1]
        return detected_language
    except Exception as e:
        return 'DetectionError'


def process_csv(input_csv, output_csv):
    with open(input_csv, 'r', encoding='utf-8') as infile, open(output_csv, 'w', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['detected_language']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            label = row['label']
            detected_language = detect_language(label)
            row['detected_language'] = detected_language
            writer.writerow(row)


def parse_arguments():
    parser = argparse.ArgumentParser(description='CSV Language Detection Tool')
    parser.add_argument('-i', '--input_csv', type=str,
                        help='Input CSV file path')
    parser.add_argument('-o', '--output_csv', type=str,
                        help='Output CSV file path')
    return parser.parse_args()


def main():
    args = parse_arguments()
    process_csv(args.input_csv, args.output_csv)


if __name__ == '__main__':
    main()
