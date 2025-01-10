# Algorithm Visualizer

Algorithm Visualizer is a web application built with Flask that allows users to visualize sorting algorithms and check if a given text is a palindrome. The application provides an interactive interface to explore different algorithms and understand their workings.

## Features

- **Sorting Algorithms**: Visualize the steps of Bubble Sort, Selection Sort, and Insertion Sort.
- **Palindrome Checker**: Check if a given text is a palindrome with a simple interface.
- **Responsive Design**: The application is designed to be responsive and user-friendly.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jester003/algorithm-visualizer.git
   cd algorithm-visualizer
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Set the Flask application environment variables**:
   ```bash
   export FLASK_APP=run.py
   export FLASK_ENV=development
   ```

2. **Run the Flask application**:
   ```bash
   flask run
   ```

3. **Open your web browser** and go to `http://127.0.0.1:5000/` to access the application.

## Project Structure

- `app/`: Contains the main application code.
  - `templates/`: HTML templates for the application.
    - `base.html`: Base template with common layout.
    - `index.html`: Main page for sorting and palindrome functionalities.
    - `about.html`: About page with additional information.
  - `static/`: Static files such as CSS and JavaScript.
    - `css/styles.css`: Custom styles for the application.
  - `routes.py`: Defines the routes and logic for sorting and palindrome checking.

- `run.py`: Entry point for running the Flask application.

## Usage

- **Sorting Algorithms**: Click on the "Sortings" button to access the sorting algorithms. Enter a comma-separated list of numbers and select an algorithm to visualize the sorting process.
- **Palindrome Checker**: Click on the "Palindrome Checker" button to check if a given text is a palindrome.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
