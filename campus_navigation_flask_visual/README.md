# Campus Navigation with Visual Map

## Features
- Web-based map visualization of campus
- Pathfinding using Dijkstra's Algorithm
- Flask backend API
- Dockerized setup

## Usage
1. Run backend with Docker:
```bash
docker build -t campus-nav .
docker run -p 5000:5000 campus-nav
```
2. Open `frontend/index.html` in your browser.