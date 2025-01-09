from flask import Flask, jsonify, request
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

def bubble_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps.append(arr.copy())
    return steps

def selection_sort(arr):
    steps = []
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append(arr.copy())
    return steps

@app.route('/get-array')
def get_array():
    array = [random.randint(1, 50) for _ in range(10)]
    return jsonify({"array": array})

@app.route('/sort', methods=['POST'])
def sort():
    data = request.get_json()
    array = data['array']
    sort_type = data['type']
    
    if sort_type == 'bubble':
        steps = bubble_sort(array.copy())
    else:
        steps = selection_sort(array.copy())
        
    return jsonify({"steps": steps})

if __name__ == '__main__':
    app.run(debug=True)