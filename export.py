import csv
def export_csv(data):
  with open("file1.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["date", "from", "to", "value", "fee"])
    for row in data:
      writer.writerow([row["date"], row["from"], row["to"], row["value"], row["fee"]])