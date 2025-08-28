

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from faker import Faker
import threading
from faker_fields.field_types import (
    FullNameField, PhoneField, EmailField, DepartmentField, ISBNField, AddressField, CityField, CountryField, DateField, CompanyField, IntegerField, TextField
)
from faker_fields.csv_generator import CSVGenerator

FIELD_TYPE_CLASSES = {
    'Full Name': FullNameField(),
    'Phone': PhoneField(),
    'Email Address': EmailField(),
    'Department (Corporate)': DepartmentField(),
    'ISBN': ISBNField(),
    'Address': AddressField(),
    'City': CityField(),
    'Country': CountryField(),
    'Date': DateField(),
    'Company': CompanyField(),
    'Integer': IntegerField(),
    'Text': TextField(),
}

DEFAULT_FIELDS = [
    ('USER_ID', 'ISBN'),
    ('NAME', 'Full Name'),
    ('MOBILE_NUMBER', 'Phone'),
    ('DESIGNATION', 'Department (Corporate)'),
    ('EMAIL_ID', 'Email Address'),
]

class DataFakerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Data Faker CSV Generator')
        self.geometry('800x450')
        self.fake = Faker()
        self.fields = []
        self.create_widgets()

    def create_widgets(self):
        self.frame = ttk.Frame(self)
        self.frame.pack(padx=20, pady=20, fill='x', expand=True)

        ttk.Label(self.frame, text='Field Name').grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.frame, text='Type').grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(self.frame, text='').grid(row=0, column=2, padx=5, pady=5)  # For remove button

        self.field_vars = []
        self.type_vars = []
        self.row_widgets = []
        for field, ftype in DEFAULT_FIELDS:
            self.add_field_row(field, ftype)

        self.rows_var = tk.IntVar(value=100000)
        ttk.Label(self.frame, text='Rows:').grid(row=100, column=0, padx=5, pady=5, sticky='e')
        ttk.Entry(self.frame, textvariable=self.rows_var, width=10).grid(row=100, column=1, padx=5, pady=5, sticky='w')

        add_btn = ttk.Button(self.frame, text='+', width=3, command=self.add_field_row)
        add_btn.grid(row=101, column=0, padx=5, pady=5, sticky='w')

        self.progress_var = tk.IntVar(value=0)
        self.progress_bar = ttk.Progressbar(self, variable=self.progress_var, maximum=100, length=400)
        self.progress_bar.pack(pady=10)
        self.progress_label = ttk.Label(self, text='Progress: 0%')
        self.progress_label.pack()

        generate_btn = ttk.Button(self, text='Generate CSV', command=self.on_generate_csv)
        generate_btn.pack(pady=10)

    def add_field_row(self, field_val='', type_val='Full Name'):
        row = len(self.field_vars) + 1
        field_var = tk.StringVar(value=field_val)
        type_var = tk.StringVar(value=type_val)
        self.field_vars.append(field_var)
        self.type_vars.append(type_var)
        entry = ttk.Entry(self.frame, textvariable=field_var, width=20)
        entry.grid(row=row, column=0, padx=5, pady=5)
        type_menu = ttk.Combobox(self.frame, textvariable=type_var, values=list(FIELD_TYPE_CLASSES.keys()), state='readonly', width=25)
        type_menu.grid(row=row, column=1, padx=5, pady=5)
        remove_btn = ttk.Button(self.frame, text='-', width=3, command=lambda: self.remove_field_row(row-1))
        remove_btn.grid(row=row, column=2, padx=5, pady=5)
        self.row_widgets.append((entry, type_menu, remove_btn))
        self.update_field_rows()

    def remove_field_row(self, idx):
        if len(self.field_vars) <= 1:
            messagebox.showwarning('Warning', 'At least one field is required.')
            return
        self.field_vars.pop(idx)
        self.type_vars.pop(idx)
        widgets = self.row_widgets.pop(idx)
        for w in widgets:
            w.destroy()
        self.update_field_rows()

    def update_field_rows(self):
        # Re-grid all widgets to maintain order
        for i, widgets in enumerate(self.row_widgets):
            for j, w in enumerate(widgets):
                w.grid(row=i+1, column=j, padx=5, pady=5)

    def on_generate_csv(self):
        num_rows = self.rows_var.get()
        if num_rows <= 0:
            messagebox.showerror('Error', 'Number of rows must be positive.')
            return
        fields = [var.get() for var in self.field_vars]
        types = [var.get() for var in self.type_vars]
        for t in types:
            if t not in FIELD_TYPE_CLASSES:
                messagebox.showerror('Error', f'Unsupported type: {t}')
                return
        file_path = filedialog.asksaveasfilename(defaultextension='.csv', filetypes=[('CSV files', '*.csv')])
        if not file_path:
            return
        self.progress_var.set(0)
        self.progress_label.config(text='Progress: 0%')

        # Map type names to class instances for CSVGenerator
        type_instances = [FIELD_TYPE_CLASSES[t] for t in types]
        thread = threading.Thread(target=self.generate_csv_thread, args=(fields, type_instances, num_rows, file_path))
        thread.start()

    def update_progress(self, percent):
        self.progress_var.set(percent)
        self.progress_label.config(text=f'Progress: {percent}%')
        self.update_idletasks()

    def generate_csv_thread(self, fields, type_instances, num_rows, file_path):
        try:
            generator = CSVGenerator(self.fake, fields, type_instances, num_rows, file_path, self.update_progress)
            generator.generate()
            messagebox.showinfo('Success', f'CSV file with {num_rows} rows generated!')
        except Exception as e:
            messagebox.showerror('Error', str(e))

if __name__ == '__main__':
    app = DataFakerApp()
    app.mainloop()
