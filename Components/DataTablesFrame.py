import customtkinter as ctk
from Utils import data_tables

class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # Configure Grid Layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.label = ctk.CTkLabel(self, text='Data Display Components', font=ctk.CTkFont(size=20, weight="bold"))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        # Create tabs for different data display options
        self.display_tabview = ctk.CTkTabview(self)
        self.display_tabview.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

        # Add Tabs
        self.table_tab = self.display_tabview.add('Table View')
        self.list_tab = self.display_tabview.add('List View')
        self.chart_tab = self.display_tabview.add('Chart Example')

        # Configure Tab Layouts
        for tab in [self.table_tab, self.list_tab, self.chart_tab]:
            tab.grid_columnconfigure(0, weight=1)
            tab.grid_rowconfigure(1, weight=1)

        self.setup_table_view()
        self.setup_list_view()
        self.setup_chart_view()

    def setup_table_view(self):
        """Setup the table view with a sample data table."""
        # Table Header
        table_header = ctk.CTkFrame(self.table_tab)
        table_header.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nsew')

        headers = ["ID", "Name", "Department", "Position", "Status"]
        for i, header in enumerate(headers):
            label = ctk.CTkLabel(table_header, text=header, font=ctk.CTkFont(weight='bold'))
            label.grid(row=0, column=i, padx=5, pady=5, sticky='ew')
            table_header.grid_columnconfigure(i, weight=1, uniform='column')

        # Table content in a scrollable frame
        table_content = ctk.CTkScrollableFrame(self.table_tab)
        table_content.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='nsew')
        
        # Sample Data Rows
        sample_data = [
            ["1001", "Ahmet Emirhan Keskin", "Mühendislik", "Kıdemli Yazılım Geliştirici", "Aktif"],
            ["1002", "Nehir Böbir", "Pazarlama", "Pazarlama Müdürü", "Aktif"],
            ["1003", "İrfan Sarıca", "İK", "İK Uzmanı", "İzinli"],
            ["1004", "Abdullah Akyol", "Mühendislik", "QA Mühendisi", "Aktif"],
            ["1005", "Mehmet Dikmen", "Finans", "Muhasebeci", "Aktif"],
            ["1006", "Sertan Balta", "Ürün", "Ürün Müdürü", "Aktif"],
            ["1007", "Kerim Polat", "Mühendislik", "Genç Yazılım Geliştirici", "Aktif"],
            ["1008", "Cem Ali Ün", "Pazarlama", "İçerik Yazarı", "Pasif"],
            ["1009", "Uğur Topel", "İK", "İşe Alım Uzmanı", "Aktif"],
            ["1010", "Hakan Hicret Vural", "Finans", "Finansal Analist", "Aktif"],
        ]

        # Add Data to Rows
        for row_idx, row_data in enumerate(sample_data):
            row_bg = 'gray90' if row_idx % 2 == 0 else 'gray80'
            if ctk.get_appearance_mode() == 'dark': 
                row_bg = 'gray30' if row_idx % 2 == 0 else 'gray40'
            
            row_frame = ctk.CTkFrame(table_content, fg_color=row_bg)
            row_frame.grid(row=row_idx, column=0, padx=0, pady=2, sticky='ew')

            for col_idx, cell_data in enumerate(row_data):
                cell = ctk.CTkLabel(row_frame, text=cell_data)
                cell.grid(row=0, column=col_idx, padx=10, pady=5, sticky='ew')
                row_frame.grid_columnconfigure(col_idx, weight=1, uniform='column')

            # Make the Row Fill the Width of the Container
            table_content.grid_columnconfigure(0, weight=1)

        # Add Control Buttons
        control_frame = ctk.CTkFrame(self.table_tab)
        control_frame.grid(row=2, column=0, padx=10, pady=10, sticky='ew')
        
        add_btn = ctk.CTkButton(control_frame, text='Add Row', command=lambda: self.add_row(table_content))
        add_btn.grid(row=0, column=0, padx=10, pady=10)

        edit_btn = ctk.CTkButton(control_frame, text='Edit Selected', command=lambda: self.edit_row(table_content))
        edit_btn.grid(row=0, column=1, padx=10, pady=10)

        delete_btn = ctk.CTkButton(control_frame, text='Delete Selected', command=lambda: self.delete_row(table_content),
                                   fg_color='darkred', hover_color='red')
        delete_btn.grid(row=0, column=2, padx=10, pady=10)

    def add_row(self, table_content): print("Add Row button clicked")
    def edit_row(self, table_content): print("Edit Selected button clicked")
    def delete_row(self, table_content): print("Delete Selected button clicked")


    def setup_list_view(self):
        """Setup the list view tab with a sample list."""
        filter_frame = ctk.CTkFrame(self.list_tab)
        filter_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        search_label = ctk.CTkLabel(filter_frame, text='Search:')
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        search_entry = ctk.CTkEntry(filter_frame)
        search_entry.grid(row=0, column=1, padx=10, pady=10, sticky='ew')
        filter_frame.grid_columnconfigure(1, weight=1)
        
        search_button = ctk.CTkButton(filter_frame, text='Search', command=lambda: self.search_list(search_entry.get()))
        search_button.grid(row=0, column=2, padx=10, pady=10)

        # List items in a scrollable frame
        list_content = ctk.CTkScrollableFrame(self.list_tab)
        list_content.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        list_content.grid_columnconfigure(0, weight=1)

        list_items = [
            {"title": "Proje A", "description": "Müşteri X için ana geliştirme projesi", "status": "Completed"},
            {"title": "Pazarlama Kampanyası", "description": "3. Çeyrek dijital pazarlama girişimi", "status": "Planning"},
            {"title": "Hata Düzeltmeleri", "description": "Sürüm 2.1'deki kritik sorunları giderme", "status": "Completed"},
            {"title": "Ekip Toplantısı", "description": "Geliştirme ekibi ile haftalık toplantı", "status": "Scheduled"},
            {"title": "Müşteri Sunumu", "description": "Prototipleri paydaşlara sunma", "status": "Pending"},
            {"title": "API Entegrasyonu", "description": "Üçüncü parti ödeme sistemi ile bağlantı", "status": "In Progress"},
            {"title": "Dokümantasyon", "description": "v2.0 için kullanıcı kılavuzlarını güncelleme", "status": "Not Started"},
            {"title": "Performans Testi", "description": "Yük altında uygulama stres testi", "status": "Pending"}
        ]

        # Add Items in to List
        for i, item in enumerate(list_items):
            self.create_list_item(list_content, i, item)

    def search_list(self, query):
        print(f"Search button clicked with query: {query}")


    def create_list_item(self, parent, idx, item_data):
        """Helper method to create a list item."""
        # Create item frame with alternating background
        bg_color = 'gray90' if idx % 2 == 0 else 'gray85'
        if ctk.get_appearance_mode() == 'dark': bg_color = 'gray20' if idx % 2 == 0 else 'gray15'

        item_frame = ctk.CTkFrame(parent, fg_color=bg_color)
        item_frame.grid(row=idx, column=0, padx=5, pady=5, sticky='ew')
        item_frame.grid_columnconfigure(0, weight=1)

        # Item Content
        title_label = ctk.CTkLabel(item_frame, text=item_data['title'], font=ctk.CTkFont(size=14, weight='bold'))
        title_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky='w')
        
        desc_label = ctk.CTkLabel(item_frame, text=item_data['description'])
        desc_label.grid(row=1, column=0, padx=10, pady=(0, 10), sticky='w')
        
        # Status Label
        status_colors = {
            'Completed':'green',
            'In Progress':'blue',
            'Pending':'orange',
            'Not Started':'gray',
            'Planning':'purple',
            'Scheduled':'teal'
        }

        status_color = status_colors.get(item_data['status'], 'gray')
        status_label = ctk.CTkLabel(item_frame, text=item_data['status'],
                                    font=ctk.CTkFont(size=12),
                                    fg_color=status_color, corner_radius=8,
                                    text_color='white', padx=8, pady=2)
        status_label.grid(row=0, column=1, padx=10, pady=10, sticky='e')

    def setup_chart_view(self):
        """Setup the chart view tab with a sample chart."""
        chart_placeholder_frame = ctk.CTkFrame(self.chart_tab, fg_color='transparent')
        chart_placeholder_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

        title = ctk.CTkLabel(chart_placeholder_frame, text='Chart Visualization', font=ctk.CTkFont(size=16, weight='bold'))
        title.pack(pady=(0, 10))

        chart_frame = ctk.CTkFrame(chart_placeholder_frame, height=300)
        chart_frame.pack(fill='both', expand=True, padx=10, pady=10)

        df = data_tables.get_iris_dataframe()
        data_tables.plot_iris_data(df, chart_frame)

        # Demo Controls
        controls_frame = ctk.CTkFrame(self.chart_tab)
        controls_frame.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="ew")
        
        chart_label = ctk.CTkLabel(controls_frame, text="Chart Type:")
        chart_label.grid(row=0, column=0, padx=10, pady=10)
        
        chart_type = ctk.CTkComboBox(controls_frame, values=["Bar Chart", "Line Chart", "Pie Chart", "Scatter Plot"])
        chart_type.grid(row=0, column=1, padx=10, pady=10)
        
        range_label = ctk.CTkLabel(controls_frame, text="Date Range:")
        range_label.grid(row=0, column=2, padx=10, pady=10)
        
        date_range = ctk.CTkComboBox(controls_frame, values=["Last 7 Days", "Last 30 Days", "Last Quarter", "Last Year"])
        date_range.grid(row=0, column=3, padx=10, pady=10)
        
        update_btn = ctk.CTkButton(controls_frame, text="Update Chart")
        update_btn.grid(row=0, column=4, padx=10, pady=10)       

    

        