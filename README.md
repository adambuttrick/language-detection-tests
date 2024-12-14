# Language Detection Testing for ROR Labels

Evaluates different language detection libraries for identifying languages in ROR label metadata. 

## Language Detection Libraries

- Lingua
- Langdetect
- FastText
- Consensus approaches (combining multiple detectors)

## Tools and Scripts

### Data Processing
- `sample_csv/`: Tools for sampling rows from large CSV files
- `labels_from_data_dump/`: Converts ROR JSON data dump to a CSV format, extracting the relevant label metadata

### Language Detection Scripts
- `detect_lang_lingua.py`: Detection using the Lingua library
- `detect_lang_langdetect.py`: Detection using the Langdetect library
- `detect_lang_fasttext.py`: Detection using FastText
- `detect_lang_consensus.py`: Combines results from all three detectors
- `detect_lang_fasttext-lingua.py`: Consensus approach using only FastText and Lingua

### Evaluation Tools
- `f-scores/`: Scripts for calculating precision, recall, F1, and F0.5 scores
- Supports both single-file and directory-wide metric calculations

## Results

Performance metrics for 5K sample dataset:

| Detector | Precision | Recall | F1 Score | F0.5 Score |
|----------|-----------|---------|-----------|------------|
| Consensus | 0.940 | 0.876 | 0.907 | 0.926 |
| Lingua | 0.813 | 1.000 | 0.897 | 0.845 |
| Lingua-FastText | 0.978 | 0.794 | 0.876 | 0.934 |
| Langdetect | 0.647 | 1.000 | 0.786 | 0.696 |
| FastText | 0.935 | 1.000 | 0.966 | 0.947 |


## Usage

### Sampling Data
```bash
python sample_csv/sample.py -i input.csv -o output.csv -s 5000
```

### Converting ROR Data
```bash
python labels_from_data_dump/labels_from_data_dump.py -d data_dump.json -o output.csv
```

### Running Language Detection
```bash
python detect_lang_[method].py -i input.csv -o output.csv
```

### Calculating Metrics
For deriving metrics from a single file:
```bash
python f-scores/calculate_f_score.py -i results.csv -o metrics.csv
```

For deriving metrics from a directory:
```bash
python f-scores/calculate_f_score_dir.py -i results_directory -o metrics.csv
```
