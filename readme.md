# JSON to Excel Converter

This script reads translation data from a JSON file and exports it to an Excel file with two columns: `Keys` and `English Words`.

## 📂 Project Structure

```
your-folder/
├── json-to-excel.py
├── json_data.json
└── README.md
```

## 🛠 Requirements

- Python 3.x
- `pandas` library
- `openpyxl` library (used by pandas to write Excel files)

## 📦 Installation

Install the required Python libraries using pip:

```bash
pip install pandas openpyxl
```

## 📁 JSON File Format

The script expects a JSON file (`json_data.json`) in the same directory. The file should be a flat JSON object, with key-value pairs like this:

```json
{
  "MENU.NEW": "new",
  "MENU.ACTIONS": "Actions",
  "AUTH.LOGIN.TITLE": "Login Account"
}
```

## ▶️ How to Run

Run the script using the terminal or command prompt:

```bash
python json-to-excel.py
```

If you're on macOS/Linux and using Python 3:

```bash
python3 json-to-excel.py
```

## 📤 Output

The script generates an Excel file named `translated_words.xlsx` in the same directory. This file will contain:

| Keys               | English Words    |
|--------------------|------------------|
| MENU.NEW           | new              |
| MENU.ACTIONS       | Actions          |
| AUTH.LOGIN.TITLE   | Login Account    |

## ✅ Success Message

If successful, the script prints:

```
Excel file 'translated_words.xlsx' has been created successfully.
```

## 📬 Questions or Issues?

If you run into any issues, double-check:
- You have valid JSON in `json_data.json`
- You’ve installed the required dependencies

