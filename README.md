## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python 3.10 or higher
- Flask
- Flask-SQLAlchemy

### Installation

1. *Clone the repository*:
    sh
    git clone https://github.com/your-username/task-manager-priority-queue.git
    cd task-manager-priority-queue/MyApp
    

2. *Create a virtual environment*:
    sh
    python -m venv venv
    

3. *Activate the virtual environment*:
    - On Windows:
        sh
        venv\Scripts\activate
        
    - On macOS/Linux:
        sh
        source venv/bin/activate
        

4. *Install the required packages*:
    sh
    pip install -r requirements.txt
    

### Running the Application

1. *Initialize the database*:
    sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    

2. *Run the Flask application*:
    sh
    flask run
    

3. *Open your web browser* and navigate to http://127.0.0.1:5000 to access the Task Manager application.

## Usage

- *Home Page*: View all tasks sorted by priority. Add new tasks, edit, delete, and toggle the status of existing tasks.
- *Add Task*: Fill in the task details and select the priority level to create a new task.
- *Edit Task*: Update the title, description, and priority level of an existing task.
- *Delete Task*: Remove tasks that are no longer needed.
- *Toggle Task Status*: Mark tasks as complete or pending.

## Screenshots

![Home Page]
![Add Task]
![Edit Task]

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Thank you for using the Task Manager with Priority Queue! If you have any questions or feedback, feel free to open an issue or contact us.
