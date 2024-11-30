import csv

inputFile = 'hourly_data.csv'
outputFile = 'GYG_minute.csv'

with open(inputFile, mode="r", newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)

    # Ensure 'Datetime' and 'Close' exist in the headers
    if 'Datetime' not in reader.fieldnames or 'Close' not in reader.fieldnames:
        raise ValueError(
            "Input CSV must contain 'Datetime' and 'Close' columns.")

    # Open the output file and write only the selected columns
    with open(outputFile, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["date", "close"])
        writer.writeheader()  # Write the header row

        # Iterate through the input file and write selected columns to the output file
        for row in reader:
            writer.writerow(
                {"date": row["Datetime"], "close": row["Close"]})
