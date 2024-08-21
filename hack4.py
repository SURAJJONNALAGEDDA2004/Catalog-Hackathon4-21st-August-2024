import csv
from datetime import datetime, timedelta
VACCINE_FILE = 'vaccination_records.csv'
def add_vaccination_record(child_name, birth_date, vaccine_name, vaccination_date):
    with open(VACCINE_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([child_name, birth_date, vaccine_name, vaccination_date])
        print(f"Vaccination record added for {child_name}.")
def view_vaccination_records():
    with open(VACCINE_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Child Name: {row[0]}, Birth Date: {row[1]}, Vaccine: {row[2]}, Vaccination Date: {row[3]}")
def find_upcoming_vaccinations():
    today = datetime.now().date()
    with open(VACCINE_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            vaccination_date = datetime.strptime(row[3], '%Y-%m-%d').date()
            if today <= vaccination_date <= (today + timedelta(days=30)):
                print(f"Reminder: {row[0]} is scheduled for {row[2]} on {row[3]}")
add_vaccination_record('Alice', '2020-05-15', 'Polio', '2024-09-20')
add_vaccination_record('Bob', '2019-03-22', 'MMR', '2024-09-15')

print("\nViewing all records:")
view_vaccination_records()

print("\nUpcoming vaccinations in the next 30 days:")
find_upcoming_vaccinations()
