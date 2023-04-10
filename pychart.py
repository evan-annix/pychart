import sys
if 'numpy' in sys.modules:
    print("NumPy module was already imported.")
else:
    import numpy 
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Create a function to open the CSV file and create the chart
def create_chart():
    # Open file dialog to choose CSV file
    file_path = filedialog.askopenfilename()

    # Create a dataframe from the CSV data
    df = pd.read_csv(file_path)

    # Set the index to be the GPU model
    df.set_index('MODEL', inplace=True)

    # Create the bar chart
    df['VRAM'].plot(kind='bar', figsize=(10, 6))

    # Set the chart title and axis labels
    plt.title('GPU VRAM Allocations over Time')
    plt.xlabel('GPU Model')
    plt.ylabel('VRAM (GB)')

    # Show the chart
    plt.show()

# Create the GUI window
window = tk.Tk()
window.title("GPU VRAM Chart")
window.geometry("800x600")
window.resizable(True, True)

# Add a button to open the CSV file and create the chart
button = tk.Button(window, text='Open File', command=create_chart)
button.pack()

# Run the GUI loop
window.mainloop()