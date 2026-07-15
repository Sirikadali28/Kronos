import pandas as pd

from services.detector_service import DetectorService

data = pd.DataFrame(
    {
        "value": [10, 11, 10, 12, 11, 50, 10, 9, 11]
    }
)

service = DetectorService()

result = service.run_detection(
    dataframe=data,
    column_name="value",
)

print("\nDetector executed successfully!")

print(f"Confirmed anomalies: {result['total_anomalies']}")