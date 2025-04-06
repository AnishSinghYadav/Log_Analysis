# 📊 Flask Observability with Prometheus, Loki, Grafana & Postman

This project demonstrates how to monitor a Flask server using Prometheus for metrics, Loki for logs, and Grafana for visualization. It includes real-time logging, metrics tracking, and API testing using Postman.

---

## 📌 Requirements

- Real-time monitoring of a Flask application
- Logging and error tracking
- Visualization of metrics and logs
- Simulated latency and failures in requests
- Exportable Prometheus metrics
- Grafana dashboard for unified observability
- API testing using Postman

---

## ⚙️ Technologies Used

| Tool         | Purpose                                      |
|--------------|----------------------------------------------|
| Flask        | Web server for simulating endpoints          |
| Prometheus   | Collects and stores time-series metrics      |
| Loki         | Collects and indexes logs                   |
| Promtail     | Reads logs and ships them to Loki            |
| Grafana      | Visualizes metrics and logs in dashboards    |
| Postman      | Used to test API endpoints                   |

---

## 📚 Python Libraries Used

| Library             | One-liner Explanation                               |
|---------------------|-----------------------------------------------------|
| `Flask`             | Lightweight web framework for Python                |
| `random`            | Generates random values for simulation              |
| `time`              | Measures request latency and delays                 |
| `logging`           | Python's built-in logging library                   |
| `prometheus_client` | Exposes app metrics to Prometheus                   |

---

## 🔄 System Architecture / Workflow

1. Flask exposes `/process` and `/generate_logs` endpoints.
2. Logs are written to `server.log` using Python logging.
3. Prometheus scrapes metrics from the `/metrics` endpoint.
4. Promtail reads `server.log` and pushes logs to Loki.
5. Grafana reads:
   - Prometheus for metrics.
   - Loki for logs.
6. Postman is used to trigger and test the Flask endpoints.

---

## 📊 Flow Diagram

![Flow Diagram](A_flowchart_digital_illustration_displays_an_obser.png)

---

## 🖼️ Screenshot Placement Guide

| Section                        | Suggested Screenshot                             |
|-------------------------------|--------------------------------------------------|
| Grafana Dashboard              | Real-time metrics & logs                         |
| Prometheus `/targets`         | Confirm targets are scraped                      |
| Flask `/metrics` endpoint     | Output of Prometheus client                      |
| Grafana Loki Log Explorer     | Logs collected from Promtail                     |
| Terminal Setup                | Running Flask, Promtail, Loki                    |
| Postman API Tests             | Request/response for `/process`, `/generate_logs`|

---

## 🚀 Running the Project

1. **Start Flask Server**
   ```bash
   python server.py
   ```

2. **Start Loki & Promtail**
   ```bash
   loki -config.file=loki.yml
   promtail -config.file=promtail.yml
   ```

3. **Start Prometheus**
   ```bash
   prometheus --config.file=prometheus.yml
   ```

4. **Access Grafana**
   - URL: `http://localhost:3000`
   - Default login: `admin / admin`

5. **Use Postman**
   - Send GET requests to:
     - `http://localhost:5002/process`
     - `http://localhost:5002/generate_logs`

---

## ✅ Output Expectations

- Prometheus dashboard shows latency, error rates, and request counts.
- Logs visible in Grafana via Loki.
- Logs and metrics can be correlated per request.
- Postman can simulate multiple user/API scenarios.

---

## 📦 Directory Structure (Simplified)

```
.
├── server.py
├── promtail.yml
├── loki.yml
├── prometheus.yml
├── server.log
├── README.md
├── A_flowchart_digital_illustration_displays_an_obser.png
```

---

## 📃 License

MIT License