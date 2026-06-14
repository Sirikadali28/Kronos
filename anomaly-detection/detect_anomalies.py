#!/usr/bin/env python3
"""
KRONOS Anomaly Detection Pipeline

Detects anomalies in time-series data using multiple statistical methods:
- Z-Score: Identifies statistical outliers (|z| > 3)
- IQR (Interquartile Range): Robust outlier detection
- Moving Average: Detects deviations from trend

Author: KRONOS Project
Date: 2024
"""

import pandas as pd
import numpy as np
import sys
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings('ignore')


class AnomalyDetector:
    """
    Statistical anomaly detection using multiple algorithms.
    """
    
    def __init__(self, data, column_name):
        """
        Initialize the anomaly detector.
        
        Args:
            data: pandas DataFrame with time-series data
            column_name: Column to analyze for anomalies
        """
        self.data = data.copy()
        self.column_name = column_name
        self.anomalies_zscore = []
        self.anomalies_iqr = []
        self.anomalies_ma = []
        self.combined_anomalies = []
        
    def detect_zscore(self, threshold=3):
        """
        Z-Score Anomaly Detection
        
        Identifies values that deviate significantly from mean.
        Formula: z = (x - μ) / σ
        
        Anomaly if |z| > threshold (typically 3, meaning 3 standard deviations)
        
        Args:
            threshold: Standard deviation threshold (default: 3)
            
        Returns:
            List of anomalous indices
        """
        print(f"\n[Z-Score Detection] Starting analysis...")
        
        # Calculate mean and standard deviation
        mean = self.data[self.column_name].mean()
        std = self.data[self.column_name].std()
        
        # Avoid division by zero
        if std == 0:
            print("[Z-Score] Warning: Standard deviation is zero. Skipping this method.")
            return []
        
        # Calculate Z-scores
        z_scores = np.abs((self.data[self.column_name] - mean) / std)
        
        # Identify anomalies
        self.anomalies_zscore = self.data[z_scores > threshold].index.tolist()
        
        print(f"  Mean: {mean:.4f}")
        print(f"  Std Dev: {std:.4f}")
        print(f"  Threshold: {threshold}σ")
        print(f"  Anomalies Found: {len(self.anomalies_zscore)}")
        
        if self.anomalies_zscore:
            print(f"  Z-Score Anomalies at indices: {self.anomalies_zscore[:5]}...")
        
        return self.anomalies_zscore
    
    def detect_iqr(self, multiplier=1.5):
        """
        Interquartile Range (IQR) Anomaly Detection
        
        Robust method that uses quartiles instead of standard deviation.
        Formula:
            IQR = Q3 - Q1
            Lower Bound = Q1 - multiplier × IQR
            Upper Bound = Q3 + multiplier × IQR
        
        Anomaly if value < Lower Bound OR value > Upper Bound
        
        Args:
            multiplier: IQR multiplier (default: 1.5, standard for outlier detection)
            
        Returns:
            List of anomalous indices
        """
        print(f"\n[IQR Detection] Starting analysis...")
        
        # Calculate quartiles
        Q1 = self.data[self.column_name].quantile(0.25)
        Q3 = self.data[self.column_name].quantile(0.75)
        IQR = Q3 - Q1
        
        # Calculate bounds
        lower_bound = Q1 - multiplier * IQR
        upper_bound = Q3 + multiplier * IQR
        
        # Identify anomalies
        anomaly_mask = (self.data[self.column_name] < lower_bound) | \
                       (self.data[self.column_name] > upper_bound)
        self.anomalies_iqr = self.data[anomaly_mask].index.tolist()
        
        print(f"  Q1 (25th percentile): {Q1:.4f}")
        print(f"  Q3 (75th percentile): {Q3:.4f}")
        print(f"  IQR: {IQR:.4f}")
        print(f"  Lower Bound: {lower_bound:.4f}")
        print(f"  Upper Bound: {upper_bound:.4f}")
        print(f"  Anomalies Found: {len(self.anomalies_iqr)}")
        
        if self.anomalies_iqr:
            print(f"  IQR Anomalies at indices: {self.anomalies_iqr[:5]}...")
        
        return self.anomalies_iqr
    
    def detect_moving_average(self, window=7, std_multiplier=2):
        """
        Moving Average Anomaly Detection
        
        Detects deviations from trend line.
        Formula:
            MA = rolling mean over window
            Deviation = |x - MA|
            Anomaly if Deviation > std_multiplier × std(Deviation)
        
        Args:
            window: Rolling window size (default: 7)
            std_multiplier: Standard deviation multiplier for threshold (default: 2)
            
        Returns:
            List of anomalous indices
        """
        print(f"\n[Moving Average Detection] Starting analysis...")
        
        # Calculate moving average
        ma = self.data[self.column_name].rolling(window=window, center=True).mean()
        
        # Calculate deviation from moving average
        deviation = np.abs(self.data[self.column_name] - ma)
        deviation_std = deviation.std()
        
        # Skip initial and final window values
        valid_indices = self.data.index[window:-window]
        
        # Identify anomalies
        threshold = std_multiplier * deviation_std
        anomaly_mask = deviation > threshold
        self.anomalies_ma = self.data[anomaly_mask & self.data.index.isin(valid_indices)].index.tolist()
        
        print(f"  Window Size: {window}")
        print(f"  Deviation Std Dev: {deviation_std:.4f}")
        print(f"  Threshold: {std_multiplier} × {deviation_std:.4f} = {threshold:.4f}")
        print(f"  Anomalies Found: {len(self.anomalies_ma)}")
        
        if self.anomalies_ma:
            print(f"  MA Anomalies at indices: {self.anomalies_ma[:5]}...")
        
        return self.anomalies_ma
    
    def combine_results(self, voting_threshold=2):
        """
        Combine results from all three methods using voting.
        
        An anomaly is confirmed if detected by at least 'voting_threshold' methods.
        
        Args:
            voting_threshold: Minimum number of methods that must flag as anomaly (default: 2)
            
        Returns:
            List of confirmed anomalous indices
        """
        print(f"\n[Ensemble Voting] Combining results from all methods...")
        
        # Combine all anomalies
        all_anomalies = (
            set(self.anomalies_zscore) | 
            set(self.anomalies_iqr) | 
            set(self.anomalies_ma)
        )
        
        # Count votes for each index
        votes = {}
        for idx in all_anomalies:
            count = 0
            if idx in self.anomalies_zscore:
                count += 1
            if idx in self.anomalies_iqr:
                count += 1
            if idx in self.anomalies_ma:
                count += 1
            
            votes[idx] = count
        
        # Select anomalies with sufficient votes
        self.combined_anomalies = [idx for idx, vote_count in votes.items() 
                                   if vote_count >= voting_threshold]
        self.combined_anomalies.sort()
        
        print(f"  Z-Score Anomalies: {len(self.anomalies_zscore)}")
        print(f"  IQR Anomalies: {len(self.anomalies_iqr)}")
        print(f"  MA Anomalies: {len(self.anomalies_ma)}")
        print(f"  Voting Threshold: {voting_threshold}")
        print(f"  Confirmed Anomalies: {len(self.combined_anomalies)}")
        
        return self.combined_anomalies
    
    def generate_report(self, output_file=None):
        """
        Generate anomaly detection report and save to CSV.
        
        Args:
            output_file: Output CSV filename (default: anomaly-report.csv)
            
        Returns:
            pandas DataFrame with results
        """
        if output_file is None:
            output_file = 'anomaly-report.csv'
        
        print(f"\n[Report Generation] Creating detailed report...")
        
        # Create report dataframe
        report = self.data.copy()
        report['zscore_anomaly'] = report.index.isin(self.anomalies_zscore)
        report['iqr_anomaly'] = report.index.isin(self.anomalies_iqr)
        report['ma_anomaly'] = report.index.isin(self.anomalies_ma)
        report['confirmed_anomaly'] = report.index.isin(self.combined_anomalies)
        
        # Add anomaly severity score
        report['anomaly_score'] = (
            report['zscore_anomaly'].astype(int) +
            report['iqr_anomaly'].astype(int) +
            report['ma_anomaly'].astype(int)
        ) / 3.0
        
        # Save to CSV
        report.to_csv(output_file, index=True)
        print(f"  Report saved to: {output_file}")
        
        return report
    
    def print_summary(self):
        """Print summary statistics of detection results."""
        print("\n" + "="*60)
        print("ANOMALY DETECTION SUMMARY")
        print("="*60)
        
        print(f"\nDataset Information:")
        print(f"  Total Records: {len(self.data)}")
        print(f"  Column Analyzed: {self.column_name}")
        print(f"  Date Range: {self.data.index.min()} to {self.data.index.max()}")
        print(f"  Value Range: {self.data[self.column_name].min():.4f} to {self.data[self.column_name].max():.4f}")
        
        print(f"\nDetection Results:")
        print(f"  Z-Score Method: {len(self.anomalies_zscore)} anomalies")
        print(f"  IQR Method: {len(self.anomalies_iqr)} anomalies")
        print(f"  Moving Average: {len(self.anomalies_ma)} anomalies")
        print(f"  Combined (Voting): {len(self.combined_anomalies)} anomalies")
        
        anomaly_percentage = (len(self.combined_anomalies) / len(self.data)) * 100
        print(f"  Anomaly Rate: {anomaly_percentage:.2f}%")
        
        print("\n" + "="*60)


def generate_sample_data(n_points=100):
    """
    Generate sample time-series data with anomalies for testing.
    
    Args:
        n_points: Number of data points to generate
        
    Returns:
        pandas DataFrame with sample data
    """
    print("\n[Data Generation] Creating sample dataset...")
    
    # Generate base trend
    base = np.sin(np.linspace(0, 4*np.pi, n_points)) * 10 + 50
    
    # Add noise
    noise = np.random.normal(0, 2, n_points)
    values = base + noise
    
    # Inject synthetic anomalies
    anomaly_indices = [15, 30, 45, 60, 75, 88]
    for idx in anomaly_indices:
        if idx < len(values):
            values[idx] += np.random.choice([-1, 1]) * 20  # Add ±20 spike
    
    # Create DataFrame
    dates = pd.date_range(start='2024-01-01', periods=n_points, freq='D')
    data = pd.DataFrame({
        'timestamp': dates,
        'value': values
    })
    data.set_index('timestamp', inplace=True)
    
    print(f"  Generated {n_points} data points with {len(anomaly_indices)} synthetic anomalies")
    print(f"  Date range: {data.index.min().date()} to {data.index.max().date()}")
    
    return data


def main():
    """
    Main execution function.
    """
    print("\n" + "="*60)
    print("KRONOS: Cloud-Native Anomaly Detection Pipeline")
    print("="*60)
    
    try:
        # Generate sample data (in production, load from S3 or CSV)
        print("\n[Step 1] Loading Data")
        data = generate_sample_data(n_points=100)
        print(f"  ✓ Data loaded: {len(data)} records")
        
        # Initialize detector
        print("\n[Step 2] Initializing Detector")
        detector = AnomalyDetector(data, 'value')
        print("  ✓ Detector initialized")
        
        # Run detections
        print("\n[Step 3] Running Anomaly Detection Methods")
        detector.detect_zscore(threshold=3)
        detector.detect_iqr(multiplier=1.5)
        detector.detect_moving_average(window=7, std_multiplier=2)
        
        # Combine results
        print("\n[Step 4] Ensemble Voting")
        detector.combine_results(voting_threshold=2)
        
        # Generate report
        print("\n[Step 5] Generating Report")
        report = detector.generate_report(output_file='anomaly-report.csv')
        print("  ✓ Report generated")
        
        # Print summary
        detector.print_summary()
        
        # Display sample anomalies
        if detector.combined_anomalies:
            print(f"\nConfirmed Anomalies (First 10):")
            for idx in detector.combined_anomalies[:10]:
                timestamp = data.index[data.index.get_loc(idx)]
                value = data.loc[idx, 'value']
                print(f"  {timestamp.date()}: {value:.4f}")
        
        print("\n✓ Pipeline completed successfully!")
        print(f"  Output: anomaly-report.csv")
        
        return 0
        
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
