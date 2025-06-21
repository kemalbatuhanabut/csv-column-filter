# CSV Column Filter & Extractor 🗂️

A simple and lightning-fast Python CLI tool to **extract specific columns** from a CSV file and optionally filter rows by a keyword — perfect for cleaning and preparing your CSV data.

---

## Why Use This Tool? 🚀

- Extract only the columns you need, no more, no less.
- Filter rows by keyword anywhere in the row.
- Works with large CSV files effortlessly.
- Zero dependencies, easy to install and use.
- Ideal for data scientists, analysts, developers, and anyone working with CSV data.

---

## Features ⭐

- Select columns by **name** or **zero-based index**.
- Optional keyword filter to keep rows containing specific text.
- Outputs a clean CSV file with only the desired columns.
- Fast and memory-efficient.
- Easy CLI usage with meaningful error messages.

---

## Installation

Just download the script:

```bash
wget https://github.com/kemalbatuhanabut/csv-column-filter/raw/main/csv_filter.py
````

Make sure you have Python 3 installed (no extra packages needed).

---

## Usage

```bash
python csv_filter.py -i input.csv -o output.csv -c name,email,age
```

or

```bash
python csv_filter.py --input data.csv --output filtered.csv --columns 0,2,5 --filter keyword
```

### Arguments:

| Argument            | Description                                                           |
| ------------------- | --------------------------------------------------------------------- |
| `-i` or `--input`   | Path to input CSV file (required)                                     |
| `-o` or `--output`  | Path to output CSV file (required)                                    |
| `-c` or `--columns` | Comma separated list of column names or zero-based indices (required) |
| `-f` or `--filter`  | Optional keyword to filter rows that contain this text                |

---

## Examples

* Extract columns "name", "email", and "age":

```bash
python csv_filter.py -i users.csv -o filtered.csv -c name,email,age
```

* Extract columns by index and filter rows containing "California":

```bash
python csv_filter.py -i data.csv -o ca_data.csv -c 0,2,5 -f California
```

---

## How It Works 🔧

* Reads the CSV header to map columns.
* Selects columns by name or index.
* Writes a new CSV with only selected columns.
* If a filter keyword is given, includes only rows containing that keyword (case-insensitive).

---

## License

MIT License — free to use and modify.

---

## Contributing

Feel free to open issues or submit pull requests for improvements!

---

Made with ❤️ by \Kemal Batuhan ABUT
