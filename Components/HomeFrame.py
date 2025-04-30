import customtkinter as ctk

class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configure Grid Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.welcome_label = ctk.CTkLabel(self, text='Welcome to My Flexible UI Application',
                                          font=ctk.CTkFont(size=20, weight="bold"))
        self.welcome_label.grid(row=0, column=0, padx=20, pady=(20, 0), sticky='nsew')

        self.dashboard_frame = ctk.CTkFrame(self)
        self.dashboard_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')
        self.dashboard_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.dashboard_frame.grid_rowconfigure((0, 1, 2), weight=1)

        # First row of cards
        self.create_dashboard_card(0, 0, 'Quick Start',
                                   'Click on the navigation items to explore the application.')
        self.create_dashboard_card(0, 1, 'Widgets',
                                    'Explore various widgets available in the application.')
        self.create_dashboard_card(0, 2, 'Form Controls',
                                    'Learn about different form controls and their usage.')
        
        # Second row of cards
        self.create_dashboard_card(1, 0, 'Data Tables',
                                    'View and manage data in tabular format.')
        self.create_dashboard_card(1, 1, 'Settings',
                                    'Configure application settings and preferences.')
        self.create_dashboard_card(1, 2, 'Exit',
                                    'Exit the application safely.')
        
    def create_dashboard_card(self, row, column, title, description):
        """Helper function to create dashboard cards."""
        card = ctk.CTkFrame(self.dashboard_frame)
        card.grid(row=row, column=column, padx=10, pady=10, sticky='nsew')
        
        card_title = ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=18, weight='bold'))
        card_title.grid(row=0, column=0, padx=10, pady=(10, 5), sticky='nsew')

        card_desc = ctk.CTkLabel(card, text=description, wraplength=200)
        card_desc.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='w')
            