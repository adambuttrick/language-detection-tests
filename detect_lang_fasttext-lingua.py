import csv
import argparse
from lingua import LanguageDetectorBuilder, Language
import fasttext

MODEL_PATH = "lid.176.bin"
fasttext_detector = fasttext.load_model(MODEL_PATH)
lingua_detector = LanguageDetectorBuilder.from_all_languages(
).with_preloaded_language_models().build()


def detect_language_lingua(label):
    try:
        detected_language = lingua_detector.detect_language_of(label)
        return str(detected_language.iso_code_639_1.name).lower()
    except Exception:
        return None


def detect_language_fasttext(label):
    try:
        predictions = fasttext_detector.predict(label, k=1)
        detected_language =  predictions[0][0].split("__label__")[1]
        return detected_language
    except Exception:
        return None


def detect_language_consensus(label):
    lang_fasttext = detect_language_fasttext(label)
    lang_lingua = detect_language_lingua(label)
    if lang_fasttext == lang_lingua:
        return lang_fasttext
    return None


def process_csv(input_csv, output_csv):
    with open(input_csv, 'r', encoding='utf-8') as infile, open(output_csv, 'w', encoding='utf-8') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + ['consensus_detected_language']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            label = row['label']
            consensus_language = detect_language_consensus(label)
            row['consensus_detected_language'] = consensus_language
            writer.writerow(row)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='CSV Language Consensus Language Detection Tool')
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
