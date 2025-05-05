from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

graph = {
    "Entrance 🚪": {"Reception 🛎️": 10, "Cafeteria ☕": 8},
    "Reception 🛎️": {"Entrance 🚪": 10, "OPD 🩺": 12, "Lab 🧪": 10},
    "OPD 🩺": {"Reception 🛎️": 12, "ICU 🧠": 6, "Pharmacy 💊": 8},
    "ICU 🧠": {"OPD 🩺": 6, "Wards 🛏️": 7},
    "Pharmacy 💊": {"OPD 🩺": 8, "Wards 🛏️": 5},
    "Lab 🧪": {"Reception 🛎️": 10, "Cafeteria ☕": 6},
    "Cafeteria ☕": {"Entrance 🚪": 8, "Lab 🧪": 6},
    "Wards 🛏️": {"ICU 🧠": 7, "Pharmacy 💊": 5}
}

def dijkstra(graph, start, end):
    import heapq
    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        if node == end:
            return {"path": path, "cost": cost}
        visited.add(node)
        for neighbor, weight in graph.get(node, {}).items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    return {"path": [], "cost": float("inf")}

@app.route('/api/path', methods=['POST'])
def get_path():
    data = request.get_json()
    start = data.get("start")
    end = data.get("end")
    result = dijkstra(graph, start, end)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


"""from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

graph = {
    "Main Gate": {"Library": 5, "Admin Block": 10},
    "Library": {"Main Gate": 5, "CSE Dept": 3},
    "Admin Block": {"Main Gate": 10, "Canteen": 2},
    "CSE Dept": {"Library": 3, "Canteen": 4},
    "Canteen": {"CSE Dept": 4, "Admin Block": 2}
}

def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        queue.sort()
        (cost, node, path) = queue.pop(0)
        if node in visited:
            continue
        path = path + [node]
        if node == end:
            return {"path": path, "cost": cost}
        visited.add(node)
        for neighbor, weight in graph.get(node, {}).items():
            if neighbor not in visited:
                queue.append((cost + weight, neighbor, path))
    return {"path": [], "cost": float("inf")}

@app.route('/api/path', methods=['POST'])
def get_path():
    data = request.get_json()
    start = data.get("start")
    end = data.get("end")
    result = dijkstra(graph, start, end)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)"""