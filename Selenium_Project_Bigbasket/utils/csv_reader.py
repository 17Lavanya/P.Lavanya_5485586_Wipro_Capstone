import csv
def read_csv_data(file_path):

    data = []

    try:

        with open(
            file_path,
            newline='',
            encoding='utf-8'
        ) as csvfile:

            reader = csv.DictReader(csvfile)

            for row in reader:
                data.append(row)

    except FileNotFoundError:
        print(f"CSV File Not Found: {file_path}")

    return data