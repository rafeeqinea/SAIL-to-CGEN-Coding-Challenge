# SAIL to CGEN – YAML/JSON to S-Expression Converter

This project is a solution to the **SAIL to CGEN Coding Challenge** from the Linux Foundation Mentorship Program.

It reads structured data in YAML or JSON format using a fixed schema and transforms it into an S-expression (LISP-style) representation.

---

## 🧩 Problem Statement

> _"Using any programming language/environment of your choice, make a program that reads in structured data in the form of tables and nested trees (e.g., JSON, YAML) using a fixed format/schema and produces an S-expression representation of the same data."_

Sample Input Format (YAML):  
```yaml
receipt: "Oz-Ware Purchase Invoice"
date: 2012-08-06
customer:
  first_name: Dorothy
  family_name: Gale
items:
  - part_no: A4786
    descrip: Water Bucket (Filled)
    price: 1.47
    quantity: 4
  - part_no: E1628
    descrip: High Heeled "Ruby" Slippers
    size: 8
    price: 133.7
    quantity: 1
```

Sample Output Format (S-expression):

```lisp
((yaml:receipt "Oz-Ware Purchase Invoice")
 (yaml:date (make-date 2012 08 06))
 (yaml:customer (yaml:customer:first_name "Dorothy") (yaml:customer:family_name "Gale"))
 (yaml:items
   (yaml:items:item:part_no 'A4786')
   (yaml:items:item:descrip "Water Bucket (Filled)")
   ...
 ))
```

## 🚀 Features

* ✅ Supports both YAML and JSON input
* ✅ Automatically detects file type
* ✅ Recursively traverses nested trees
* ✅ Handles strings, numbers, lists and dictionaries
* ✅ Outputs clean S-expression syntax
* ✅ Saves output to a `.lisp` file

## 🛠️ How to Run

### 1. Install Dependencies

```bash
pip install pyyaml
```

### 2. Prepare Your Input
Place your `.yaml` or `.json` input file in the project directory. Default filename expected: `data.yaml`

### 3. Run the Script

```bash
python converter.py
```

### 4. Check the Output
The resulting S-expression will be printed to the console and saved in `output.lisp`.

## 📁 Files

* `converter.py` – Main Python script
* `data.yaml` – Sample YAML input
* `output.lisp` – Generated output file
* `README.md` – Project documentation

## 📜 License

This project is licensed under the MIT License.

## 🤝 Acknowledgments

This project was created as part of the **Linux Foundation's LFX Mentorship Program – SAIL to CGEN Track**.
