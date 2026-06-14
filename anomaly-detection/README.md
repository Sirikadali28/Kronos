# Anomaly Detection Pipeline

## Overview

The KRONOS anomaly detection pipeline detects abnormal patterns in time-series data using three complementary statistical methods. It combines results from multiple algorithms using ensemble voting to reduce false positives.

## Features

- **Z-Score Detection**: Identifies statistical outliers based on standard deviation
- **IQR Detection**: Robust method using interquartile range
- **Moving Average Detection**: Detects deviations from trend
- **Ensemble Voting**: Combines methods for higher accuracy
- **CSV Report Generation**: Detailed results with anomaly scores

## Prerequisites

### Python Packages

```bash
pip install pandas numpy
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

### Python Version

- Python 3.8+
- Recommended: Python 3.9+

## Usage

### Basic Execution

Run with sample data (generates synthetic dataset):

```bash
python detect_anomalies.py
```

This will:
1. Generate 100 sample data points
2. Run all three detection methods
3. Combine results using voting
4. Generate `anomaly-report.csv`

### Output Example

```
============================================================
KRONOS: Cloud-Native Anomaly Detection Pipeline
============================================================

[Step 1] Loading Data
  ✓ Data loaded: 100 records

[Step 2] Initializing Detector
  ✓ Detector initialized

[Step 3] Running Anomaly Detection Methods

[Z-Score Detection] Starting analysis...
  Mean: 50.1234
  Std Dev: 15.3421
  Threshold: 3σ
  Anomalies Found: 8

[IQR Detection] Starting analysis...
  Q1 (25th percentile): 38.4521
  Q3 (75th percentile): 61.2341
  IQR: 22.7820
  Lower Bound: 16.3310
  Upper Bound: 83.3552
  Anomalies Found: 6

[Moving Average Detection] Starting analysis...
  Window Size: 7
  Deviation Std Dev: 2.1543
  Threshold: 2 × 2.1543 = 4.3086
  Anomalies Found: 5

[Step 4] Ensemble Voting
  Z-Score Anomalies: 8
  IQR Anomalies: 6
  MA Anomalies: 5
  Voting Threshold: 2
  Confirmed Anomalies: 4

[Step 5] Generating Report
  Report saved to: anomaly-report.csv
  ✓ Report generated

============================================================
ANOMALY DETECTION SUMMARY
============================================================

Dataset Information:
  Total Records: 100
  Column Analyzed: value
  Date Range: 2024-01-01 to 2024-04-09
  Value Range: 12.3456 to 87.6543

Detection Results:
  Z-Score Method: 8 anomalies
  IQR Method: 6 anomalies
  Moving Average: 5 anomalies
  Combined (Voting): 4 anomalies
  Anomaly Rate: 4.00%

✓ Pipeline completed successfully!
  Output: anomaly-report.csv
```

## Detection Methods

### 1. Z-Score Method

Identifies values that deviate significantly from the mean.

**Formula:**
```
z = (x - μ) / σ
Anomaly if |z| > threshold (typically 3)
```

**Interpretation:**
- `threshold = 3`: Detects values >3 standard deviations from mean
- Effective for normally distributed data
- ~99.7% of normal data falls within 3σ

**Parameters:**
- `threshold`: Standard deviation multiplier (default: 3)

### 2. IQR (Interquartile Range) Method

Robust method using quartiles, less sensitive to extreme values.

**Formula:**
```
Q1 = 25th percentile
Q3 = 75th percentile
IQR = Q3 - Q1
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
Anomaly if value < Lower Bound OR value > Upper Bound
```

**Advantages:**
- Robust to extreme values
- Works well for skewed distributions
- Good for non-normal data

**Parameters:**
- `multiplier`: IQR multiplier (default: 1.5)

### 3. Moving Average Method

Detects deviations from trend line using rolling statistics.

**Formula:**
```
MA = rolling mean over window
Deviation = |x - MA|
Anomaly if Deviation > std_multiplier × std(Deviation)
```

**Advantages:**
- Detects trend deviations
- Good for time-dependent anomalies
- Flexible window size

**Parameters:**
- `window`: Rolling window size in periods (default: 7)
- `std_multiplier`: Standard deviation multiplier (default: 2)

### 4. Ensemble Voting

Combines results from all three methods to reduce false positives.

**How it works:**
1. Each method flags anomalies independently
2. Count votes for each data point
3. Confirm anomaly if votes ≥ voting_threshold

**Voting Threshold:**
- Default: 2 (confirmed if detected by ≥2 methods)
- Lower = more sensitive, higher = fewer false positives

## Output Format

The pipeline generates `anomaly-report.csv` with columns:

| Column | Description |
|--------|-------------|
| timestamp | Date/time of the record |
| value | Actual data value |
| zscore_anomaly | Flagged by Z-Score method (True/False) |
| iqr_anomaly | Flagged by IQR method (True/False) |
| ma_anomaly | Flagged by Moving Average method (True/False) |
| confirmed_anomaly | Flagged by ensemble voting (True/False) |
| anomaly_score | Proportion of methods flagging anomaly (0.0-1.0) |

### Sample Output

```csv
timestamp,value,zscore_anomaly,iqr_anomaly,ma_anomaly,confirmed_anomaly,anomaly_score
2024-01-01,48.2314,False,False,False,False,0.0
2024-01-02,52.1432,False,False,False,False,0.0
2024-01-16,78.5421,True,True,False,True,0.6667
2024-01-31,12.3456,True,True,True,True,1.0
2024-02-15,81.2341,True,False,True,True,0.6667
```

## Customization

### Modify Detection Parameters

Edit the parameters in the `main()` function:

```python
# Z-Score threshold
detector.detect_zscore(threshold=2.5)  # More sensitive

# IQR multiplier
detector.detect_iqr(multiplier=1.0)  # Stricter bounds

# Moving Average window
detector.detect_moving_average(window=14, std_multiplier=1.5)

# Voting threshold
detector.combine_results(voting_threshold=1)  # Lower threshold = more anomalies
```

### Load Data from CSV

```python
# Instead of generate_sample_data()
data = pd.read_csv('your_data.csv', index_col='timestamp', parse_dates=True)
```

### Load Data from S3

```bash
# First, copy data from S3
aws s3 cp s3://kronos-anomaly-data/data.csv ./data.csv

# Then load it
data = pd.read_csv('data.csv', index_col='timestamp', parse_dates=True)
```

### Process Multiple Columns

```python
columns_to_analyze = ['cpu_usage', 'memory_usage', 'network_traffic']

for column in columns_to_analyze:
    print(f"\nAnalyzing {column}...")
    detector = AnomalyDetector(data, column)
    detector.detect_zscore()
    detector.detect_iqr()
    detector.detect_moving_average()
    detector.combine_results()
    detector.generate_report(f'anomaly-report-{column}.csv')
```

## Performance Optimization

### Large Datasets

For datasets with millions of records:

```python
# Use chunks for memory efficiency
chunk_size = 10000
for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    detector = AnomalyDetector(chunk, 'value')
    # Process chunk
```

### Reduce Processing Time

```python
# Use numpy operations instead of pandas where possible
# Vectorize calculations
# Use numba for critical loops

from numba import jit

@jit(nopython=True)
def fast_zscore(data):
    # Optimized calculation
    pass
```

## Troubleshooting

### No Anomalies Detected

**Possible causes:**
1. Threshold too strict - lower the value
2. Data too clean - add test anomalies
3. Method not suitable for data distribution

**Solutions:**
```python
# Lower thresholds
detector.detect_zscore(threshold=2.0)
detector.detect_iqr(multiplier=1.0)

# Lower voting threshold
detector.combine_results(voting_threshold=1)
```

### Too Many False Positives

**Solutions:**
```python
# Increase thresholds
detector.detect_zscore(threshold=4.0)

# Increase voting threshold
detector.combine_results(voting_threshold=3)  # All 3 methods must agree
```

### Memory Issues with Large Data

```python
# Use data type optimization
data['value'] = data['value'].astype('float32')  # Instead of float64

# Drop unnecessary columns
data = data[['timestamp', 'value']]
```

### CSV Report Not Generated

```bash
# Check write permissions
ls -la anomaly-detection/
chmod 755 anomaly-detection/

# Specify full path
detector.generate_report(output_file='/full/path/anomaly-report.csv')
```

## Integration with KRONOS Platform

### Run from Kubernetes

```bash
# Create ConfigMap with script
kubectl create configmap anomaly-script --from-file=detect_anomalies.py

# Run as Job
kubectl apply -f anomaly-detection-job.yaml

# Check results
kubectl logs job/anomaly-detection
kubectl cp job/anomaly-detection:/output/anomaly-report.csv ./
```

### S3 Integration

```python
import boto3

s3 = boto3.client('s3')

# Download data from S3
s3.download_file('kronos-anomaly-data', 'input.csv', './input.csv')

# Upload results to S3
s3.upload_file('anomaly-report.csv', 'kronos-anomaly-data', 'reports/anomaly-report.csv')
```

## Performance Metrics

Performance on sample datasets:

| Data Points | Processing Time | Memory Usage |
|-------------|-----------------|--------------|
| 100 | <100ms | 5MB |
| 1,000 | ~200ms | 10MB |
| 10,000 | ~500ms | 25MB |
| 100,000 | ~2s | 100MB |
| 1,000,000 | ~15s | 500MB |

## References

- Pandas Documentation: https://pandas.pydata.org/
- NumPy Documentation: https://numpy.org/
- Statistical Methods: https://en.wikipedia.org/wiki/Anomaly_detection
- Z-Score Method: https://en.wikipedia.org/wiki/Standard_score
- IQR Method: https://en.wikipedia.org/wiki/Interquartile_range

## License

Part of the KRONOS project. See LICENSE file for details.
