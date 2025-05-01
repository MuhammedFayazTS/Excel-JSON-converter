
# JSON to Excel & Excel to JSON Converter

This project provides two scripts: one to convert JSON data to an Excel file and the other to convert Excel data back to JSON format.

---

## 📂 Project Structure

```
your-folder/
├── json-to-excel.py
├── excel-to-json.py
├── json_data.json
└── README.md
```

---

## 🛠 Requirements

- Python 3.x
- `pandas` library
- `openpyxl` library (for reading and writing Excel files)

---

## 📦 Installation

Install the required Python libraries using pip:

```bash
pip install pandas openpyxl
```

---

## 📁 JSON File Format

The `json-to-excel.py` script expects a JSON file (`json_data.json`) in the same directory. The file should contain key-value pairs like this:

```json
{
  "MENU.NEW": "new",
  "MENU.ACTIONS": "Actions",
  "AUTH.LOGIN.TITLE": "Login Account"
}
```

---

## 📝 JSON to Excel Converter (`json-to-excel.py`)

This script reads translation data from a JSON file and exports it to an Excel file with two columns: `Keys` and `English Words`.

### ▶️ How to Run

To convert your JSON data to Excel, use the following command in the terminal or command prompt:

```bash
python json-to-excel.py
```

If you're using Python 3 on macOS/Linux:

```bash
python3 json-to-excel.py
```

### 📤 Output

The script will generate an Excel file named `translated_words.xlsx`, which will look like this:

| Keys               | English Words    |
|--------------------|------------------|
| MENU.NEW           | new              |
| MENU.ACTIONS       | Actions          |
| AUTH.LOGIN.TITLE   | Login Account    |

### ✅ Success Message

If the script runs successfully, you will see:

```
Excel file 'translated_words.xlsx' has been created successfully.
```

---

## 📝 Excel to JSON Converter (`excel-to-json.py`)

This script reads data from an Excel file and converts it into a JSON file with key-value pairs.

### ▶️ How to Run

To convert your Excel data back to JSON, run the following command in the terminal:

```bash
python excel-to-json.py
```

For macOS/Linux with Python 3:

```bash
python3 excel-to-json.py
```

### 📂 Excel File Format

This script expects an Excel file (`translated_words.xlsx`) with two columns:

| Keys               | English Words    |
|--------------------|------------------|
| MENU.NEW           | new              |
| MENU.ACTIONS       | Actions          |
| AUTH.LOGIN.TITLE   | Login Account    |

### 📤 Output

The script will create a `json_data.json` file with the following format:

```json
{
  "MENU.NEW": "new",
  "MENU.ACTIONS": "Actions",
  "AUTH.LOGIN.TITLE": "Login Account"
}
```

### ✅ Success Message

If successful, the script prints:

```
JSON file 'json_data.json' has been created successfully.
```

---

## 📬 Questions or Issues?

If you encounter any issues, make sure to:

- Verify that the `json_data.json` or `translated_words.xlsx` file is in the correct format.
- Ensure that you have installed the required dependencies using `pip install pandas openpyxl`.

