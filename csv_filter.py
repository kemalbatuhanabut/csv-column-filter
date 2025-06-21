import csv
import argparse
import sys

def filter_csv(input_path, output_path, columns, filter_keyword=None):
    with open(input_path, newline='', encoding='utf-8') as infile, \
         open(output_path, 'w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        header = next(reader)
        col_indices = []

        # Determine columns to extract by name or index
        for col in columns:
            if col.isdigit():
                idx = int(col)
                if idx < 0 or idx >= len(header):
                    print(f"Column index {idx} out of range", file=sys.stderr)
                    sys.exit(1)
                col_indices.append(idx)
            else:
                if col not in header:
                    print(f"Column name '{col}' not found in CSV header", file=sys.stderr)
                    sys.exit(1)
                col_indices.append(header.index(col))

        # Write new header with selected columns
        new_header = [header[i] for i in col_indices]
        writer.writerow(new_header)

        # Write filtered rows
        for row in reader:
            # If filtering keyword is given, check if present in any cell
            if filter_keyword and filter_keyword.lower() not in (cell.lower() for cell in row):
                continue

            new_row = [row[i] for i in col_indices]
            writer.writerow(new_row)

def main():
    parser = argparse.ArgumentParser(description="CSV Column Filter & Extractor CLI Tool")
    parser.add_argument('-i', '--input', required=True, help="Input CSV file path")
    parser.add_argument('-o', '--output', required=True, help="Output CSV file path")
    parser.add_argument('-c', '--columns', required=True, help="Comma separated column names or indices (e.g. name,email,age or 0,2,5)")
    parser.add_argument('-f', '--filter', help="Optional filter keyword to keep only rows containing this keyword")

    args = parser.parse_args()
    columns = [c.strip() for c in args.columns.split(',')]

    filter_csv(args.input, args.output, columns, args.filter)

if __name__ == "__main__":
    main()
