import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load the exam data using Pandas
def load_exam_data(file_path):
    return pd.read_csv(file_path)

# Step 2: Calculate key statistics using Numpy
def calculate_statistics(data):
    # Calculating average score
    average_score = np.mean(data['Score'])
    # Calculating maximum and minimum scores
    max_score = np.max(data['Score'])
    min_score = np.min(data['Score'])
    # Calculating number of students
    num_students = len(data)
    return average_score, max_score, min_score, num_students

# Step 3: Visualize the exam scores using matplotlib
def create_visualizations(data):
    # Histogram of exam scores
    plt.figure(figsize=(8, 6))
    plt.hist(data['Score'], bins=10, edgecolor='black')
    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.title('Exam Score Distribution')
    plt.show()

    # Bar chart for top-performing students
    top_students = data[data['Score'] >= 90]
    plt.figure(figsize=(8, 6))
    plt.bar(top_students['Name'], top_students['Score'], color='green')
    plt.xlabel('Student Name')
    plt.ylabel('Score')
    plt.title('Top-performing Students')
    plt.xticks(rotation=45)
    plt.show()

# Main function to execute the program
def main():
    # Step 1: Load the exam data
    exam_data=pd.read_csv("ExamScores.csv")

    # Step 2: Calculate key statistics
    avg_score, max_score, min_score, num_students = calculate_statistics(exam_data)
    print("Average Score:", avg_score)
    print("Maximum Score:", max_score)
    print("Minimum Score:", min_score)
    print("Number of Students:", num_students)
    create_visualizations(exam_data)

if __name__ == "__main__":
    main()