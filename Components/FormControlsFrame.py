import customtkinter as ctk
import time

class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Configure Grid Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.label = ctk.CTkLabel(self, text='Form Controls & Input Elements')
        self.label.grid(row=0, column=0, padx=10, pady=20)

        # Create a Frame for Forms
        self.form_frame = ctk.CTkFrame(self)
        self.form_frame.grid(row=1, column=0, padx=20, pady=(0, 20), sticky='nsew')
        self.form_frame.grid_columnconfigure(0, weight=1)
        self.form_frame.grid_columnconfigure(1, weight=3)

        # [Form Elements]
        # Text Inputs
        self.create_form_row(0, 'Name:', ctk.CTkEntry(self.form_frame, placeholder_text='Enter name'))
        self.create_form_row(1, 'Email:', ctk.CTkEntry(self.form_frame, placeholder_text='Enter email'))

        # Text Area
        self.create_form_row(2, 'Message:', ctk.CTkTextbox(self.form_frame, height=100))

        # Combobox
        self.combo_var = ctk.StringVar(value='Option 1')
        self.combo = ctk.CTkComboBox(self.form_frame, values=['Option 1', 'Option 2', 'Option 3'],
                                     variable=self.combo_var)
        self.create_form_row(3, 'Select:', self.combo)

        # Radio Buttons
        self.radio_frame = ctk.CTkFrame(self.form_frame)
        self.radio_var = ctk.IntVar(value=0)

        self.radio1 = ctk.CTkRadioButton(self.radio_frame, text='Option 1', variable=self.radio_var, value=0)
        self.radio1.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.radio2 = ctk.CTkRadioButton(self.radio_frame, text='Option 2', variable=self.radio_var, value=1)
        self.radio2.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        self.radio3 = ctk.CTkRadioButton(self.radio_frame, text='Option 3', variable=self.radio_var, value=2)
        self.radio3.grid(row=0, column=2, padx=10, pady=10, sticky='w')
        
        self.create_form_row(4, 'Choose:', self.radio_frame)

        # Date picker (simplified version, can be expanded)
        date_frame = ctk.CTkFrame(self.form_frame)

        day_label = ctk.CTkLabel(date_frame, text="Day:")
        day_label.grid(row=0, column=0, padx=(0, 5), pady=0)
        self.day_combo = ctk.CTkComboBox(date_frame, values=[str(i) for i in range(1, 32)], width=60)
        self.day_combo.grid(row=0, column=1, padx=5, pady=0)
        
        month_label = ctk.CTkLabel(date_frame, text="Month:")
        month_label.grid(row=0, column=2, padx=5, pady=0)
        self.month_combo = ctk.CTkComboBox(date_frame, values=[str(i) for i in range(1, 13)], width=60)
        self.month_combo.grid(row=0, column=3, padx=5, pady=0)
        
        year_label = ctk.CTkLabel(date_frame, text="Year:")
        year_label.grid(row=0, column=4, padx=5, pady=0)
        self.year_combo = ctk.CTkComboBox(date_frame, values=[str(i) for i in range(2020, 2031)], width=80)
        self.year_combo.grid(row=0, column=5, padx=(5, 0), pady=0)
        
        self.create_form_row(5, "Date:", date_frame)

        # File Browser
        file_frame = ctk.CTkFrame(self.form_frame)
        self.file_path = ctk.StringVar()
        self.file_entry = ctk.CTkEntry(file_frame, textvariable=self.file_path, width=300)
        self.file_entry.grid(row=0, column=0, padx=(0, 10), pady=0, sticky='ew')
        
        self.file_button = ctk.CTkButton(file_frame, text='Browse...', width=100, command=self.browse_file)
        self.file_button.grid(row=0, column=1, padx=0, pady=0)
        
        file_frame.grid_columnconfigure(0, weight=1)
        self.create_form_row(6, 'File:', file_frame)

        # Buttons row
        button_frame = ctk.CTkFrame(self.form_frame)
        
        self.reset_button = ctk.CTkButton(button_frame, text="Reset", fg_color="gray30",
                                       hover_color="gray40", command=self.reset_form)
        self.reset_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.submit_button = ctk.CTkButton(button_frame, text="Submit",
                                        command=self.submit_form)
        self.submit_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.create_form_row(7, "", button_frame)


    def create_form_row(self, row:int, label_text:str, widget)->None:
        """Helper method to create form rows with consistent layout."""
        if label_text:
            label = ctk.CTkLabel(self.form_frame, text=label_text)
            label.grid(row=row, column=0, padx=20, pady=10, sticky='e')

        widget.grid(row=row, column=1, padx=20, pady=10, sticky='ew')

    def browse_file(self):
        """File browser dialog handler."""
        filename = ctk.filedialog.askopenfilename()
        if filename: self.file_path.set(filename)
        else: self.file_path.set("No file selected")

    def reset_form(self):
        """Reset all form fields."""
        for widget in self.form_frame.winfo_children():
            if isinstance(widget, ctk.CTkEntry): widget.delete(0, 'end')
            elif isinstance(widget, ctk.CTkTextbox): widget.delete('0,0', 'end')

        self.combo_var.set('Option 1')
        self.radio_var.set(0)
        self.file_path.set('')
        self.day_combo.set('1')
        self.monty_combo.set('1')
        self.year_combo.set('2025')

    def submit_form(self):
        """Handle form submission."""
        dialog = ctk.CTkInputDialog(text='Form Submitted Successfully!', title='Success')