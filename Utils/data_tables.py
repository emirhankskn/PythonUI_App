import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# FigureCanvasTkAgg: It renders the matplotlib figures as a Tkinter Widget

def get_iris_dataframe() -> pd.DataFrame:
    """Load the Iris dataset and return it as a pandas DataFrame."""
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    return df

def plot_iris_data(df:pd.DataFrame, frame) -> None:
    """Plot the Iris dataset using seaborn."""

    melted_df = df.melt(id_vars='target', var_name='feature', value_name='value')
    grouped_df = melted_df.groupby(['target', 'feature'], as_index=False).mean()

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.lineplot(data=grouped_df, x='target', y='value', hue='feature', marker='o', ax=ax)
    ax.set_title('Average Feature Values by Target')
    ax.set_xlabel('Iris Class')
    ax.set_ylabel('Average Value')
    ax.legend(title='Feature', bbox_to_anchor=(1.05, 1), loc='upper left')
    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
    
def plot_big_data(frame):
    np.random.seed(0)
    num_rows = 1_000_000
    df = pd.DataFrame({
        'index': np.arange(num_rows),
        'sensor_1': np.random.normal(loc=0, scale=1, size=num_rows),
        'sensor_2': np.random.normal(loc=5, scale=2, size=num_rows),
        'sensor_3': np.random.normal(loc=10, scale=3, size=num_rows),
        'sensor_4': np.random.normal(loc=15, scale=4, size=num_rows),
    })

    # Step 2: Melt the dataframe for seaborn
    melted = df.melt(id_vars='index', var_name='sensor', value_name='value')

    # Step 3: Plot using Seaborn
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=melted, x='index', y='value', hue='sensor', ax=ax)

    ax.set_title('Raw 1,000,000 Data Points Per Sensor')
    ax.set_xlabel('Index')
    ax.set_ylabel('Sensor Value')
    fig.tight_layout()

    # Step 4: Draw on your tkinter frame
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)
    
    