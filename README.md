# DTA to Excel Converter (v2.2)

An efficient, production-ready Python utility designed to safely parse and convert large Stata (`.dta`) datasets into compressed Excel spreadsheets (`.xlsx`) without data loss or memory leaks.

## 🚀 Key Features
* **Automated Chunking & Splitting:** Gracefully handles massive datasets that exceed Excel’s native row limitations by automatically partitioning data across multiple sheets.
* **Robust File I/O Pipeline:** Built using optimized `pandas` and `pyreadstat` routines to extract heavy statistical data blocks securely.
* **Cross-Platform Delivery:** Features a standalone Windows executable (`.exe`) compiled layer, allowing non-technical stakeholders to run the utility without a local Python environment.
* **User-Centric Feedback:** Implements a lightweight GUI built with `tkinter` to provide operational progress states during heavy data transformations.

## 🛠️ Tech Stack
* **Language:** Python 3.13+
* **Data Processing:** Pandas, Pyreadstat
* **Excel Infrastructure:** OpenPyXL
* **Interface Layer:** Tkinter GUI

## 📦 Installation & Setup
Install the necessary system and data processing dependencies via:
```bash
pip install -r requirement.txt
```

Author: Zidane Syukri | License: MIT
