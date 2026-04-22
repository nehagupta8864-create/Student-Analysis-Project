🎓 Student Report & Dashboard System

📌 Project Overview

This project is a simple Student Data Processing and Dashboard system built using Python, Pandas, and Streamlit.

It takes raw student marks data from an Excel file, processes it, and generates:

- Total marks
- Percentage
- Grade
- Pass/Fail result

It also creates a beautiful dashboard to visualize student performance.

---

🚀 Features

✅ Automatic Report Generation
✅ Grade Calculation System
✅ Pass/Fail Identification
✅ Topper Detection
✅ Top 5 Students List
✅ Fail Students List
✅ Interactive Dashboard (Streamlit)
✅ Download Reports as CSV

---

🛠 Technologies Used

- Python
- Pandas
- Streamlit
- Excel (Input Data)

---

📂 Project Structure

student project/
│
├── student_raw_data.xlsx
├── student_report4.xlsx
├── main.py
├── app.py
├── README.md
├── requirements.txt

---

⚙️ How It Works

1. Load Excel file using Pandas
2. Calculate Total Marks
3. Calculate Percentage
4. Assign Grade (A, B, C, D, Fail)
5. Generate:
   - Full Report
   - Top 5 Students
   - Fail Students
6. Display everything in Streamlit Dashboard

---

▶️ How to Run Project

Step 1: Install Requirements

pip install -r requirements.txt

Step 2: Run Data Processing Script

python main.py

Step 3: Run Dashboard

streamlit run app.py

---

📊 Dashboard Preview

- Total Students
- Average Percentage
- Top Score
- Topper
- Top 5 Students
- Fail Students
- Bar Chart

---

📥 Output Files

- student_report.csv
- top5_students.csv
- fail_students.csv

---

💡 Future Improvements

- Add subject-wise analysis
- Add student search filter
- Add login system
- Add PDF report export

---

🙌 Author

Created by Neha Gupta

---

⭐ If you like this project

Give it a star ⭐ on GitHub
