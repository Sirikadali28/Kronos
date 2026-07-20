from prometheus_client import (
    Counter,
    Gauge,
    Histogram,
)

# Total HTTP requests
REQUEST_COUNT = Counter(
    "kronos_http_requests_total",
    "Total HTTP requests",
    ["method", "endpoint", "status"],
)

# Request latency
REQUEST_LATENCY = Histogram(
    "kronos_http_request_duration_seconds",
    "HTTP request latency",
    ["method", "endpoint"],
)

# Active requests
ACTIVE_REQUESTS = Gauge(
    "kronos_active_requests",
    "Current active HTTP requests",
)

# Total errors
ERROR_COUNT = Counter(
    "kronos_http_errors_total",
    "Total HTTP errors",
    ["method", "endpoint"],
)
