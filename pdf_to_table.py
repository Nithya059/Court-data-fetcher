import pdfplumber
import csv

pdf_path = "CaseFile.pdf"  # Change this if your file name is different
csv_output_path = "output.csv"

all_data = []

# Open the PDF file
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        # Try to extract a table from each page
        table = page.extract_table()
        if table:
            print(f"✅ Table found on page {i + 1}")
            # Skip the header (first row) and add rest
            all_data.extend(table[1:])
        else:
            print(f"❌ No table found on page {i + 1}")

# After reading all pages, save to CSV if any data found
if not all_data:
    print("❌ No data to save.")
else:
    print(f"✅ Extracted {len(all_data)} rows. Saving to CSV...")

    # Save to CSV
    with open(csv_output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Optional: Add your column headers if known
        writer.writerow(["Index", "Court", "Law Manager #", "Case/Project Name", "Attorney", "Description"])
        writer.writerows(all_data)

    print(f"✅ Data saved to {csv_output_path}")