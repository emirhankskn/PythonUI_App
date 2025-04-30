import customtkinter as ctk
from Utils.helper_functions import load_image

class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configure Grid Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.label = ctk.CTkLabel(self, text='Widgets Demonstration',
                                  font=ctk.CTkFont(size=20, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Create scrollable frame for widgets
        self.scrollable_frame = ctk.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=1, column=0, padx=20, pady=(10, 20), sticky='nsew')
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Add Various Widgets to the Scrollable Frame
        # [Section]:Buttons
        self.__add_section_title(0, 'Buttons')
        self.button_frame = ctk.CTkFrame(self.scrollable_frame)
        self.button_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='ew')

        self.button_normal = ctk.CTkButton(self.button_frame, text='Standart Button')
        self.button_normal.grid(row=0, column=0, padx=10, pady=10)
        
        self.btn_image = load_image("Images/button_image.png", (20, 20))        
        self.button_with_image = ctk.CTkButton(self.button_frame, text='Image Button', image=self.btn_image)
        self.button_with_image.grid(row=0, column=1, padx=10, pady=10)

        self.button_disabled = ctk.CTkButton(self.button_frame, text='Disabled Button', state='disabled')
        self.button_disabled.grid(row=0, column=2, padx=10, pady=10)

        # [Section]:Switches and Checkboxes
        self.__add_section_title(2, 'Switches & Checkboxes')
        self.toggle_frame = ctk.CTkFrame(self.scrollable_frame)
        self.toggle_frame.grid(row=3, column=0, padx=10, pady=(0, 10), sticky='ew')

        self.chkbox1 = ctk.CTkCheckBox(self.toggle_frame, text='Option 1')
        self.chkbox1.grid(row=0, column=0, padx=20, pady=10)

        self.chkbox2 = ctk.CTkCheckBox(self.toggle_frame, text='Option 2')
        self.chkbox2.grid(row=0, column=1, padx=20, pady=10)

        self.chkbox3 = ctk.CTkCheckBox(self.toggle_frame, text='Option 3')
        self.chkbox3.grid(row=0, column=2, padx=20, pady=10)

        # [Section]:Sliders
        self.__add_section_title(4, 'Sliders')
        self.slider_frame = ctk.CTkFrame(self.scrollable_frame)
        self.slider_frame.grid(row=5, column=0, padx=10, pady=(0, 10), sticky='ew')
        
        self.slider1 = ctk.CTkSlider(self.slider_frame, from_=0, to=100) # number_of_steps
        self.slider1.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky='ew')
        
        self.slider2 = ctk.CTkSlider(self.slider_frame, from_=0, to=100, orientation='vertical', height=100)
        self.slider2.grid(row=0, column=2, padx=20, pady=10)

        self.progress_bar = ctk.CTkProgressBar(self.slider_frame)
        self.progress_bar.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky='ew')
        self.progress_bar.set(0.75) # Set to 75%


        # [Section]:Tabs
        self.__add_section_title(6, 'Tabs')
        self.tabview = ctk.CTkTabview(self.scrollable_frame)
        self.tabview.grid(row=7, column=0, padx=10, pady=(0, 10), sticky='nsew')

        tab1 = self.tabview.add('Tab 1')
        tab2 = self.tabview.add('Tab 2')
        tab3 = self.tabview.add('Tab 3')

        tab1_label = ctk.CTkLabel(tab1, text='This is Tab 1')
        tab1_label.pack(padx=20, pady=20)

        tab2_label = ctk.CTkLabel(tab2, text='This is Tab 2')
        tab2_label.pack(padx=20, pady=20)

        tab3_label = ctk.CTkLabel(tab3, text='This is Tab 3')
        tab3_label.pack(padx=20, pady=20)    

    def __add_section_title(self, row:int, title:str)->None:
        """Function to add a section title to the scrollable frame."""
        section_title = ctk.CTkLabel(self.scrollable_frame, text=title, 
                                     font=ctk.CTkFont(size=16, weight="bold"))
        section_title.grid(row=row, column=0, padx=10, pady=(20, 5), sticky='w')
