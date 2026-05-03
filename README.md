  # 📊 Student Performance Analysis using NumPy

> Analyzing student marks using Python and NumPy — Mean, Max, Min and more!

A data analysis project built with **NumPy** that takes student marks across multiple subjects and performs statistical analysis — totals, averages, topper detection, subject-wise performance, and more.

---

## 📌 Table of Contents

- [About](#about)
- [Features](#features)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Project Tasks](#project-tasks)
- [Sample Output](#sample-output)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Author](#author)

---

## 📖 About

This project was built to practice **NumPy** for real-world data analysis. Instead of using loops manually, NumPy functions like `np.sum()`, `np.mean()`, `np.argmax()`, `np.any()`, and `np.where()` are used to analyze student performance efficiently.

The dataset contains marks of **4 students** across **4 subjects** — Math, Science, English, and Computer.

---

## ✨ Features

- 📝 Total and average marks per student
- 🏆 Topper and lowest scorer detection
- 🎯 Students scoring above 90 in any subject
- 📚 Subject-wise average marks
- ⚡ Uses NumPy — fast, clean, and efficient
- 🐍 Pure Python — no extra libraries except NumPy

---

## ✅ Requirements

- **Python 3.x**
- **NumPy**

Install NumPy:
```bash
pip install numpy
```

---

## 🚀 How to Run

**Step 1 — Clone the repository**

```bash
git clone https://github.com/MaheshChaudhari7/Student_Performance_Analysis_using_Numpy.git
cd Student_Performance_Analysis_using_Numpy
```

**Step 2 — Install NumPy (if not already installed)**

```bash
pip install numpy
```

**Step 3 — Run the file**

```bash
python student_analysis.py
```

---

## 🧠 Project Tasks

### Task 1 — Total & Average Marks Per Student
- Calculate total marks of each student across all subjects
- Calculate average marks for each student

### Task 2 — Topper & Lowest Scorer
- Find the student with the **highest** total marks
- Find the student with the **lowest** total marks

### Task 3 — Students Scoring Above 90
- Find which students scored **above 90** in at least one subject
- Display which subjects they scored above 90 in

### Task 4 — Subject-wise Average
- Calculate average marks for each subject
- Find the subject with **highest** and **lowest** average

---

## 📸 Sample Output

```
==================================================
   Student Performance Analysis
==================================================

📝 Total & Average Marks Per Student:
Student 1: Total = 343, Average = 85.75
Student 2: Total = 340, Average = 85.0
Student 3: Total = 369, Average = 92.25
Student 4: Total = 375, Average = 93.75

--------------------------------------------------

🏆 Topper: Student 4 with total marks 375
📉 Lowest Scorer: Student 2 with total marks 340

--------------------------------------------------

🎯 Students who scored above 90 in any subject:
Student 1 - Science (92)
Student 2 - English (90)
Student 3 - Math (92), English (95), Computer (94)
Student 4 - Math (90), Science (95), English (91), Computer (99)

--------------------------------------------------

📚 Subject-wise Average Marks:
Math    : 86.5
Science : 90.0
English : 90.25
Computer: 90.0

✅ Highest Average Subject: English (90.25)
❌ Lowest Average Subject: Math (86.5)
==================================================
```

---

## 📁 Project Structure

```
Student_Performance_Analysis_using_Numpy/
│
├── student_analysis.py     ← Main Python file (run this)
└── README.md               ← You are reading this
```

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| **Python 3.x** | Programming Language |
| **NumPy** | Array operations & statistics |
| **VS Code** | Code Editor |
| **Git & GitHub** | Version Control |

### NumPy Functions Used:
- `np.array()` — Create 2D marks array
- `np.sum()` — Total marks per student
- `np.mean()` — Average marks
- `np.argmax()` — Find topper
- `np.argmin()` — Find lowest scorer
- `np.any()` — Check if any mark > 90
- `np.where()` — Get student indices

---

## 🔮 Future Improvements

- [ ] Load student data from a CSV file
- [ ] Add grade system (A, B, C, D, F)
- [ ] Plot bar charts using Matplotlib
- [ ] Add pass/fail detection per subject
- [ ] Support for more students and subjects

---

## 👨‍💻 Author

**Mahesh Chaudhari**
- GitHub: [@MaheshChaudhari7](https://github.com/MaheshChaudhari7)

> Python & NumPy Beginner Project — Learning Data Analysis 🚀

---

## 📄 License

This project is open source and free to use for learning purposes.

---

