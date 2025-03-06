from flask import Flask, jsonify, request
import logging
import random
import time
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='server.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Prometheus Metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'http_status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'Request latency in seconds', ['endpoint'])
ERROR_COUNT = Counter('http_request_errors_total', 'Total HTTP Errors', ['endpoint'])

# List of possible delays (converted to milliseconds)
delays = [0.05, 0.2, 0.5, 0.8]

@app.route('/process', methods=['GET'])
def process_request():
    request_id = random.randint(1000, 9999)
    start_time = time.time()
    logging.info(f"Received request ID: {request_id} from {request.remote_addr}")

    # Simulate failure (increased to 50%)
    if random.random() < 0.5:
        ERROR_COUNT.labels(endpoint="/process").inc()
        REQUEST_COUNT.labels(method="GET", endpoint="/process", http_status="500").inc()
        logging.error(f"Request ID: {request_id} failed with a server error.")
        return jsonify({"error": "Server error occurred"}), 500

    # Simulate delay
    delay = random.choice(delays)
    time.sleep(delay)

    # Track latency
    REQUEST_LATENCY.labels(endpoint="/process").observe(time.time() - start_time)
    REQUEST_COUNT.labels(method="GET", endpoint="/process", http_status="200").inc()

    logging.info(f"Request ID: {request_id} processed successfully in {delay} seconds.")
    return jsonify({"message": "Request processed", "request_id": request_id, "delay": delay})

@app.route('/generate_logs', methods=['GET'])
def generate_logs():
    log_types = ['info', 'warning', 'error', 'debug']
    for _ in range(10):  # Generate 10 log entries
        log_type = random.choice(log_types)
        message = f"Generated {log_type} log entry."

        if log_type == 'info':
            logging.info(message)
        elif log_type == 'warning':
            logging.warning(message)
        elif log_type == 'error':
            logging.error(message)
        elif log_type == 'debug':
            logging.debug(message)

    REQUEST_COUNT.labels(method="GET", endpoint="/generate_logs", http_status="200").inc()
    return jsonify({"message": "Logs generated successfully"})

# New endpoint to generate only error logs
@app.route('/generate_error_logs', methods=['GET'])
def generate_error_logs():
    for _ in range(5):  # Generate 5 error log entries
        message = f"Generated error log entry at {time.strftime('%Y-%m-%d %H:%M:%S')}."
        logging.error(message)

    ERROR_COUNT.labels(endpoint="/generate_error_logs").inc()
    REQUEST_COUNT.labels(method="GET", endpoint="/generate_error_logs", http_status="200").inc()
    
    return jsonify({"message": "Error logs generated successfully"})

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
