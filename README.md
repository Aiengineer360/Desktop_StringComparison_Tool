# 🚀 String Comparison Tool

---

## 📖 Overview
The **String Comparison Tool** is a Python application featuring a PyQt5-based GUI to compare two text strings using multiple techniques:
- **Word-by-word comparison** (split method)
- **String interning comparison** (memory optimization)
- **Word frequency analysis**

It also benchmarks the performance of different comparison methods and includes text preprocessing to clean the inputs.

---

## ✨ Features
- **Text Preprocessing:** Remove numbers, symbols, and extra spaces.
- **Split Comparison:** Compare strings by splitting into words.
- **Interning Comparison:** Memory-efficient comparison using `sys.intern()`.
- **Word Count Analysis:** Generate word frequency dictionaries for each string.
- **Performance Benchmarking:** Measure and compare the execution time of methods.

---

## 🛠️ Installation
Make sure you have Python 3 installed. Then install the dependencies:

```bash
pip install pyqt5
```

---

## 🖥️ Usage
1. **Launch the application.**
2. **Input Strings:** Paste your two texts into the provided text areas.
3. **Preprocess:** Click *Preprocess Strings* to clean the input.
4. **Compare:** Choose either split comparison or interning comparison.
5. **Analyze:** View the word frequency analysis for deeper insights.

---

## 🧩 Project Structure
- **Input Tab:**  
  Enter and preprocess strings.

- **Comparison Tab:**  
  - Word-by-word comparison
  - Interning comparison
  - Benchmarking execution time

- **Word Analysis Tab:**  
  Word frequency generation and comparison.

---

## 🔥 Example Output

### Word-by-word Split Comparison
```
-------- Word Comparison Using Split --------
String 1 == String 2
Comparison took 0.000456 seconds
```

### Word Count Analysis
```
'Streptomyces': 12
'bingchenggensis': 18
'produced': 2
...
```

---

## 🛠️ Technologies Used
- **Python 3**
- **PyQt5** (for GUI)
- **sys**, **string**, **time** libraries (for internal processing)

---

## 🐛 Troubleshooting
| Issue                        | Solution                          |
|-------------------------------|-----------------------------------|
| GUI crashes on startup        | Ensure PyQt5 is installed         |
| No results after preprocessing | Check for non-empty input strings |
| Slow performance              | Reduce input size                 |

---

## Workflow

![image](https://github.com/user-attachments/assets/a80eb023-9df8-47b3-9890-cdf8d1ae8b85)

---

## GUIs
![image](https://github.com/user-attachments/assets/61c5b5c0-3e4c-4467-afe5-d00919adaca5)
![image](https://github.com/user-attachments/assets/3f935e5e-1023-4e4d-ad2c-c9bb5978b26d)



## 📄 License
This project is licensed under the **MIT License**.

---

## 🙌 Contributing
Feel free to fork this repository, open issues, or submit pull requests to contribute!

---
