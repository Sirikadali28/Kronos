from pathlib import Path
import sys

import pandas as pd

# Make the project root importable
PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from detect_anomalies import AnomalyDetector


class DetectorService:
    """
    Service layer responsible for interacting with the existing
    anomaly detection engine.

    NOTE:
    This class does NOT modify the anomaly detection logic.
    It simply orchestrates the existing implementation.
    """

    def create_detector(
        self,
        dataframe: pd.DataFrame,
        column_name: str,
    ) -> AnomalyDetector:
        """
        Create an AnomalyDetector instance.
        """

        return AnomalyDetector(
            dataframe,
            column_name,
        )

    def run_detection(
        self,
        dataframe: pd.DataFrame,
        column_name: str,
    ):
        """
        Execute the complete anomaly detection pipeline.
        """

        detector = self.create_detector(
            dataframe=dataframe,
            column_name=column_name,
        )

        detector.detect_zscore()
        detector.detect_iqr()
        detector.detect_moving_average()

        detector.combine_results()

        report = detector.generate_report()

        return {
            "detector": detector,
            "report": report,
            "confirmed_anomalies": detector.combined_anomalies,
            "total_anomalies": len(detector.combined_anomalies),
        }