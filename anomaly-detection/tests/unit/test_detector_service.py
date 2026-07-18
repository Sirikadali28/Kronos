import pandas as pd

from app.services.detector_service import DetectorService


def test_create_detector():
    df = pd.DataFrame({"value": [10, 20, 30, 100]})

    service = DetectorService()

    detector = service.create_detector(
        dataframe=df,
        column_name="value",
    )

    assert detector is not None


def test_run_detection_returns_dictionary():
    df = pd.DataFrame({"value": [10, 20, 30, 100]})

    service = DetectorService()

    result = service.run_detection(
        dataframe=df,
        column_name="value",
    )

    assert isinstance(result, dict)


def test_detection_contains_required_keys():
    df = pd.DataFrame({"value": [10, 20, 30, 100]})

    service = DetectorService()

    result = service.run_detection(
        dataframe=df,
        column_name="value",
    )

    assert "detector" in result
    assert "report" in result
    assert "confirmed_anomalies" in result
    assert "total_anomalies" in result


def test_total_anomalies_is_integer():
    df = pd.DataFrame({"value": [10, 20, 30, 100]})

    service = DetectorService()

    result = service.run_detection(
        dataframe=df,
        column_name="value",
    )

    assert isinstance(result["total_anomalies"], int)