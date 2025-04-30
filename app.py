import customtkinter as ctk
from PIL import Image
from Components import HomeFrame, WidgetsFrame, FormControlsFrame, DataTablesFrame, SettingsFrame
from Utils.helper_functions import load_image 
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("Flexible UI Application")
        self.geometry("1000x750")
        self.minsize(800, 500)

        # Grid layout configuration
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        try:
            self.logo_image = load_image("Images/logo.png", (30, 30))
            self.home_image = load_image("Images/home.png", (20, 20))
            self.widgets_image = load_image("Images/widgets.png", (20, 20))
            self.form_controls_image = load_image("Images/form_control.png", (20, 20))
            self.data_tables_image = load_image("Images/database.png", (20, 20))
            self.settings_image = load_image("Images/settings.png", (20, 20))
            self.exit_image = load_image("Images/exit.png", (20, 20))
        except FileNotFoundError as e:
            print(f"[Error Loading Image]: {e}")
            self.logo_image = None
            self.home_image = None
            self.settings_image = None

        # Create Navigation Frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=10)
        self.navigation_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
        self.navigation_frame.grid_rowconfigure(4, weight=0)
        self.navigation_frame.grid_rowconfigure(5, weight=1)
        self.navigation_frame.grid_rowconfigure(6, weight=0)
        self.navigation_frame.grid_rowconfigure(7, weight=0)

        # Create Navigation Frame Elements
        self.navigation_title = ctk.CTkLabel(self.navigation_frame, text="Navigation",
                                             compound="left", font=ctk.CTkFont(size=15, weight="bold"),
                                             image=self.logo_image)
        self.navigation_title.grid(row=0, column=0, padx=10, pady=(10, 5))

        # Home Button
        self.home_button = ctk.CTkButton(self.navigation_frame, text='Home', corner_radius=5, height=30,
                                         compound='left', font=ctk.CTkFont(size=12),
                                         hover_color=('gray70', 'gray30'), anchor='w',
                                         command=self.home_button_event, image=self.home_image)
        self.home_button.grid(row=1, column=0, padx=5, pady=(20, 5), sticky='ew')

        # Widgets Button
        self.widgets_button = ctk.CTkButton(self.navigation_frame, text='Widgets', corner_radius=5, height=30,
                                             compound='left', font=ctk.CTkFont(size=12),
                                             hover_color=('gray70', 'gray30'), anchor='w',
                                             command=self.widgets_button_event, image=self.widgets_image)
        self.widgets_button.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

        # Form Controls Button
        self.form_controls_button = ctk.CTkButton(self.navigation_frame, text='Form Controls', corner_radius=5,
                                                   height=30, compound='left', font=ctk.CTkFont(size=12),
                                                   hover_color=('gray70', 'gray30'), anchor='w',
                                                   command=self.form_controls_button_event, image=self.form_controls_image)
        self.form_controls_button.grid(row=3, column=0, padx=5, pady=5, sticky='ew')

        # Data Table Button
        self.data_tables_button = ctk.CTkButton(self.navigation_frame, text='Data Tables', corner_radius=5, height=30,
                                                 compound='left', font=ctk.CTkFont(size=12),
                                                 hover_color=('gray70', 'gray30'), anchor='w',
                                                 command=self.data_tables_button_event, image=self.data_tables_image)
        self.data_tables_button.grid(row=4, column=0, padx=5, pady=5, sticky='ew')

        # Row 5 is a space...

        # Bottom Buttons 1 : Settings
        self.settings_button = ctk.CTkButton(self.navigation_frame, text='Settings', corner_radius=5, height=30,
                                              compound='left', font=ctk.CTkFont(size=12),
                                              hover_color=('gray70', 'gray30'), anchor='w',
                                              command=self.settings_button_event, image=self.settings_image)
        self.settings_button.grid(row=6, column=0, padx=5, pady=5, sticky='ew')

        # Bottom Buttons 2 : Exit
        self.exit_button = ctk.CTkButton(self.navigation_frame, text='Exit', corner_radius=5, height=30,
                                          compound='left', font=ctk.CTkFont(size=12),
                                          hover_color=('gray70', 'gray30'), anchor='w',
                                          command=self.quit, image=self.exit_image)
        self.exit_button.grid(row=7, column=0, padx=5, pady=5, sticky='ew')


        # Create Main Content Frames
        self.home_frame = HomeFrame.MainFrame(self, corner_radius=0, fg_color='transparent')
        self.widgets_frame = WidgetsFrame.MainFrame(self, corner_radius=0, fg_color='transparent')
        self.form_controls_frame = FormControlsFrame.MainFrame(self, corner_radius=0, fg_color='transparent')
        self.data_tables_frame = DataTablesFrame.MainFrame(self, corner_radius=0, fg_color='transparent')
        self.settings_frame = SettingsFrame.MainFrame(self, corner_radius=0, fg_color='transparent')

        # Default Frame
        self.select_frame_by_name('data_tables')

        
    def select_frame_by_name(self, frame_name:str):
        """Show the selected frame and hide others."""
        
        # Set Button for Selected Button
        fg_color = ('gray75', 'gray25')
        self.home_button.configure(fg_color=fg_color if frame_name=='home' else 'gray25')
        self.widgets_button.configure(fg_color=fg_color if frame_name=='widgets' else 'gray25')
        self.form_controls_button.configure(fg_color=fg_color if frame_name=='form_controls' else 'gray25')
        self.data_tables_button.configure(fg_color=fg_color if frame_name=='data_tables' else 'gray25')
        self.settings_button.configure(fg_color=fg_color if frame_name=='settings' else 'gray25')
        

        # Show Selected Frame using match-case
        match frame_name:
            case "home": self.home_frame.grid(row=0, column=1, sticky="nsew")
            case "widgets": self.widgets_frame.grid(row=0, column=1, sticky="nsew")
            case "form_controls": self.form_controls_frame.grid(row=0, column=1, sticky="nsew")
            case "data_tables": self.data_tables_frame.grid(row=0, column=1, sticky="nsew")
            case "settings": self.settings_frame.grid(row=0, column=1, sticky="nsew")
            case _: pass

        # Hide all frames except the selected one
        if frame_name != "home": self.home_frame.grid_forget()
        if frame_name != "widgets": self.widgets_frame.grid_forget()
        if frame_name != "form_controls": self.form_controls_frame.grid_forget()
        if frame_name != "data_tables": self.data_tables_frame.grid_forget()
        if frame_name != "settings": self.settings_frame.grid_forget()


    def home_button_event(self): self.select_frame_by_name('home')
    def widgets_button_event(self): self.select_frame_by_name('widgets')
    def form_controls_button_event(self): self.select_frame_by_name('form_controls')
    def data_tables_button_event(self): self.select_frame_by_name('data_tables')
    def settings_button_event(self): self.select_frame_by_name('settings')