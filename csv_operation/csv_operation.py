# csvに解凍結果を書き込む
import csv
path = "csv_operation/thawing.csv"
def csv_operation_a(date, week_day, loaf, bread):
    with open(path, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writerow([date, week_day, loaf, bread])

def csv_operation_r():
    with open(path, 'r', newline='') as file:
        for row in csv.reader(file, delimiter=','):
            print(row)


if __name__ == "__main__":
    csv_operation_a(path, 1, 2, 3)
