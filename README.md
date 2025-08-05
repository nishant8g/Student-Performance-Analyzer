# Student-Performance-Analyzer
A Python script to automate the calculation of student marks, grades, and class performance summaries.
# Automated Student Performance Analyzer

A command-line Python application to automate the calculation and summarization of student marks and grades. This tool processes a list of students, calculates their total and average scores, assigns a grade, and provides a summary of the entire class's performance, including the class average and topper.

## Features

-   **Automated Calculations**: Automatically computes the total and average marks for each student.
-   **Grade Assignment**: Assigns a letter grade (A+, A, B, C, D, F) based on a predefined grading scale.
-   **Individual Reports**: Displays a detailed report for each student.
-   **Class Summary**: Generates a summary for the entire class, including:
    -   Total number of students.
    -   Overall class average score.
    -   The name and score of the class topper.
-   **Clean & Readable Output**: Presents all results in a formatted and easy-to-read layout.

## Requirements

This project is built with standard Python libraries and does not require any external packages.

-   Python 3.x

## Project Setup & Installation

To set up and run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/](https://github.com/)[YOUR_GITHUB_USERNAME]/Student-Performance-Analyzer.git
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd Student-Performance-Analyzer
    ```

3.  **Create a virtual environment (Optional but recommended):**
    ```sh
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

4.  **Install requirements:**
    *(This project has no external libraries, but this is a standard practice.)*
    ```sh
    pip install -r requirements.txt
    ```

## How to Run the Project

Once the setup is complete, run the main script from the terminal:

```sh
python grade_calculator.py

##Expected Output
---------------------------------------------
        Student Marks and Grade Summary
---------------------------------------------
Student: Priya Singh
  - Marks: [95, 88, 91]
  - Total: 274
  - Average: 91.33
  - Grade: A+
-------------------------
... (output for other students) ...

---------------------------------------------
              Class Summary
---------------------------------------------
Total Number of Students: 5
Class Average Score: 70.00
Class Topper: Priya Singh with Total Marks: 274
---------------------------------------------
