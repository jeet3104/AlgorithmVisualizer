from flask import Blueprint, render_template, request, jsonify
# Ensure that User is used somewhere or remove the import if not needed
# from app.models import User

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', title='Algorithm Visualizer')

@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/visualize', methods=['POST'])
def visualize():
    array = request.form.get('array')
    algorithm = request.form.get('algorithm')
    
    # Convert the input string to a list of integers
    array = list(map(int, array.split(',')))
    
    # Perform sorting based on the selected algorithm
    if algorithm == 'bubble':
        steps = bubble_sort(array)
    elif algorithm == 'selection':
        steps = selection_sort(array)
    elif algorithm == 'insertion':
        steps = insertion_sort(array)
    else:
        steps = []

    return jsonify(steps)

@main.route('/check_palindrome', methods=['POST'])
def check_palindrome():
    text = request.form.get('text')
    is_palindrome = text == text[::-1]
    return jsonify({'is_palindrome': is_palindrome, 'text': text})

def bubble_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            explanation = f"Comparing {arr[j]} and {arr[j+1]}"
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                explanation += f" and swapping them"
            steps.append((arr.copy(), explanation))
    return steps

def selection_sort(arr):
    steps = []
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            explanation = f"Comparing {arr[j]} with current minimum {arr[min_idx]}"
            if arr[j] < arr[min_idx]:
                min_idx = j
                explanation += f" and updating minimum to {arr[min_idx]}"
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        explanation += f". Swapping {arr[i]} with {arr[min_idx]}"
        steps.append((arr.copy(), explanation))
    return steps

def insertion_sort(arr):
    steps = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        explanation = f"Inserting {key} into sorted portion"
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            explanation += f", moving {arr[j+1]} to the right"
        arr[j + 1] = key
        steps.append((arr.copy(), explanation))
    return steps