# README for JSON to CSV Converter

## Overview
Converts ROR data dump into a CSV format for testing language detection on ROR labels. Specifically, it extracts the ID, name, labels, language of labels, and country information from every ROR record with a label value.

## Usage
```
python labels_from_data_dump.py -d <input_json_file> -o <output_csv_file>
```

### Arguments
- `-d`, `--data_dump` : Path to the data dump file.
- `-o`, `--output_csv` : Path to the output CSV file.


### Output CSV Format
The output CSV file will have the following headers:
- `ror_id`
- `name`
- `label`
- `label_lang`
- `country`