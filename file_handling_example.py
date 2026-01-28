import csv

# 1. Create & write user data into a text file
try:
    with open("userdata.txt", "w") as file:  # automatically closes file
        file.write("Name: Varsha\n")
        file.write("Age: 21\n")
        file.write("Email: example@example.com\n")
    print("Text file created and data written successfully.")
except Exception as e:
    print(f"Error writing file: {e}")

# 2. Read file contents
try:
    with open("userdata.txt", "r") as file:
        content = file.read()
        print("\n--- File Contents ---")
        print(content)
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print(f"Error reading file: {e}")

# 3. Append data to file
try:
    with open("userdata.txt", "a") as file:
        file.write("Phone: +91-XXXXXXXXXX\n")
    print("\nData appended successfully.")
except Exception as e:
    print(f"Error appending file: {e}")

# 4. Confirm appended data
try:
    with open("userdata.txt", "r") as file:
        print("\n--- Updated File Contents ---")
        print(file.read())
except Exception as e:
    print(f"Error reading file: {e}")

# 5. Create a CSV file using csv module
csv_data = [
    ["Name", "Age", "Email"],
    ["Varsha", 21, "example@example.com"],
    ["Rohan", 23, "rohan@mail.com"],
    ["Priya", 20, "priya@mail.com"],
]

try:
    with open("userdata.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(csv_data)
    print("\nCSV file created and rows written.")
except Exception as e:
    print(f"Error writing CSV: {e}")

# 6. Read CSV file
try:
    with open("userdata.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        print("\n--- CSV Contents ---")
        for row in reader:
            print(row)
except FileNotFoundError:
    print("CSV file not found!")
except Exception as e:
    print(f"Error reading CSV: {e}")
