import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListWidget

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()

        # Window settings
        self.setWindowTitle("To-Do List")
        self.resize(400, 500)

        # Main layout
        layout = QVBoxLayout()

        # Task input field
        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText("Enter a task..")
        layout.addWidget(self.task_input)

        # Task List
        self.task_list = QListWidget(self)
        layout.addWidget(self.task_list)

        # Buttons Layout (to align buttons in a row)
        button_layout = QHBoxLayout()
        
        self.add_button = QPushButton("Add Task", self)
        self.add_button.clicked.connect(self.add_task)
        button_layout.addWidget(self.add_button)

        self.done_button = QPushButton("Mark as Done", self)
        self.done_button.clicked.connect(self.mark_done_task)
        button_layout.addWidget(self.done_button)

        self.delete_button = QPushButton("Delete Task", self)
        self.delete_button.clicked.connect(self.delete_task)
        button_layout.addWidget(self.delete_button)

        layout.addLayout(button_layout)  # Add button row to main layout

        self.setLayout(layout)
        self.set_styles()  # Apply styles first
        self.load_tasks()  # Then load tasks

    def add_task(self):
        """Adds a task to the list and saves it."""
        task = self.task_input.text().strip()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()
            self.save_tasks()
            # Force update
            self.task_list.update()

    def delete_task(self):
        """Deletes the selected task from the list."""
        selected_item = self.task_list.currentRow()
        if selected_item != -1:
            self.task_list.takeItem(selected_item)
            self.save_tasks()
            # Force update
            self.task_list.update()

    def mark_done_task(self):
        """Marks a task as done."""
        selected_item = self.task_list.currentItem()
        if selected_item:
            task_text = selected_item.text()
            if not task_text.startswith("[✔] "):  # Prevent duplicate checkmarks
                selected_item.setText(f"[✔] {task_text}")
                self.save_tasks()
                # Force update
                self.task_list.update()

    def save_tasks(self):
        """Saves all tasks to a file using UTF-8 encoding."""
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for i in range(self.task_list.count()):
                file.write(self.task_list.item(i).text() + "\n")
        print(f"Saved {self.task_list.count()} tasks to file")

    def load_tasks(self):
        """Loads tasks from the file when the app starts."""
        try:
            with open("tasks.txt", "r", encoding="utf-8") as file:
                tasks = file.readlines()
                print(f"Loading {len(tasks)} tasks from file")
                for task in tasks:
                    task_text = task.strip()
                    if task_text:  # Only add non-empty tasks
                        print(f"Adding task: '{task_text}'")
                        self.task_list.addItem(task_text)
                # Force update after loading
                self.task_list.update()
        except FileNotFoundError:
            print("No tasks.txt file found - starting with empty list")
            pass  # No file yet

    def set_styles(self):
        """Apply UI styles."""
        self.setStyleSheet("""
            QWidget {
                background-color: #F5F5F5;
                font-family: 'JetBrains Mono', 'Courier New', 'Consolas', monospace;
            }
            QLineEdit {
                background-color: #FFFFFF;
                border: 2px solid #4F646F;
                border-radius: 5px;
                padding: 8px;
                font-size: 16px;
                color: #000000;
            }
            QPushButton {
                background-color: #4F646F;
                color: white;
                border-radius: 5px;
                padding: 8px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #3B4C50;
            }
            QListWidget {
                background-color: #FFFFFF;
                border: 2px solid #DCDCDC;
                border-radius: 5px;
                font-size: 16px;
                color: #000000; /* Ensures text is black */
            }
            QListWidget::item {
                color: #000000; /* Explicitly set color for list items */
                padding: 4px;
            }
            QListWidget::item:selected {
                background-color: #C0D6DF;
                color: #000000; /* Keep text black when selected */
            }
        """)


# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec())