# DTA to Excel Converter (v2.2)

**Author:** Zidane Syukri  
**Version:** 2.2  
**Description:** Converts large Stata `.dta` files to Excel `.xlsx` safely using Python.  
Handles files that may exceed Excel’s row limits by automatically splitting them into multiple sheets.

---

## Features

- Convert `.dta` files to `.xlsx` format.
- Supports large datasets (splits into multiple sheets if necessary).
- Minimal GUI with progress indicator.
- Safe export using `pandas` and `openpyxl`.
- Windows executable (`.exe`) available for users without Python.

---

## Requirements

- Python 3.13.5+
- pandas
- pyreadstat
- openpyxl
- tkinter (standard with Python)

Install dependencies via:

```bash
pip install -r requirements.txt
