import csv
import tkinter as tk
from tkinter import ttk

def search_records():
    reg_number = reg_entry.get()
    records = []

    with open('2023-24 Final Years.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Reg Number'] == reg_number:
                records.append(row)

    display_records(records)

def display_records(records):
    output_text.delete(1.0, tk.END)
    
    if records:
        for record in records:
            output_text.insert(tk.END, f"Sl.No: {record['Sl.No']}\n")
            output_text.insert(tk.END, f"Name: {record['Name']}\n")
            output_text.insert(tk.END, f"Reg Number: {record['Reg Number']}\n")
            output_text.insert(tk.END, f"Mobile Number: {record['Mobile Number']}\n")
            output_text.insert(tk.END, f"Email: {record['Email']}\n")
            output_text.insert(tk.END, f"SSLC: {record['SSLC']}\n")
            output_text.insert(tk.END, f"HSC: {record['HSC']}\n")
            output_text.insert(tk.END, f"UG: {record['UG ']}\n")
            output_text.insert(tk.END, f"No Of Standing Arrears: {record['No Of Standing Arrears']}\n")
            output_text.insert(tk.END, "\n")
    else:
        output_text.insert(tk.END, "No records found\n")

# Create tkinter window
window = tk.Tk()
window.title("Search Records")

# Create a frame
frame = ttk.Frame(window)
frame.pack(padx=20, pady=20)

# Create an entry for Reg Number
reg_label = ttk.Label(frame, text="Enter Reg Number:")
reg_label.grid(row=0, column=0, padx=5, pady=5)
reg_entry = ttk.Entry(frame)
reg_entry.grid(row=0, column=1, padx=5, pady=5)

# Create a search button
search_button = ttk.Button(frame, text="Search", command=search_records)
search_button.grid(row=0, column=2, padx=5, pady=5)

# Create text widget to display records
output_text = tk.Text(frame, height=10, width=50)
output_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

window.mainloop()
