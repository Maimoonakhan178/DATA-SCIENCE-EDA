#!/usr/bin/env python
# coding: utf-8

# In[12]:


from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Programming For Artificial Intelligence CCP")

# Open and convert the JPEG image to PNG format
jpeg_image = Image.open("C:/Users/MBG Traders/Desktop/front.jpeg")
png_image = jpeg_image.convert("RGBA")

# Create a PhotoImage from the converted PNG image
image = ImageTk.PhotoImage(png_image)

# Set the window size to match the image size
root.geometry(f"{image.width()}x{image.height()}")

# Create Label in our window
img = Label(root, image=image)
img.place(x=0, y=0, relwidth=1, relheight=1)

# Define the background color for the buttons
button_bg_color = "#1f77b4"

# Create the button for the Complex Computing Program
button1 = Button(
    root,
    text="Complex Computing Program",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=30,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
   
)
button1.place(relx=0.5, rely=0.9, anchor="center")

root.mainloop()


# In[13]:


from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Programming For Artifical Intellgience CCP")

# Open and convert the JPEG image to PNG format
jpeg_image = Image.open("C:/Users/MBG Traders/Desktop/front.jpeg")
png_image = jpeg_image.convert("RGBA")

# Create a PhotoImage from the converted PNG image
image = ImageTk.PhotoImage(png_image)

# Set the window size to match the image size
root.geometry(f"{image.width()}x{image.height()}")

# Create Label in our window
img = Label(root, image=image)
img.place(x=0, y=0, relwidth=1, relheight=1)

# Define the background color for the buttons
button_bg_color = "#1f77b4"

# Create three buttons in the center
button1 = Button(
    root,
    text="India Covid Data",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
)
button1.place(relx=0.3, rely=0.9, anchor="center")

button2 = Button(
    root,
    text="India Vaccination Data",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
)
button2.place(relx=0.5, rely=0.9, anchor="center")


button3 = Button(
    root,
    text="Global Covid Data",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
)
button3.place(relx=0.7, rely=0.9, anchor="center")


root.mainloop()


# In[15]:


from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title("Programming For Artificial Intelligence CCP")

# Define df as a global variable
df = None

# Function to handle button click event
def open_file():
    global df  # Access the global df variable
    path = 'C:/Users/MBG Traders/Desktop/covid_vaccine_statewise.csv'
    df = pd.read_csv(path)
    data_text.delete("1.0", END)  # Clear previous data
    data_text.insert(END, "Vaccination Data:\n")
    data_text.insert(END, df.head())

def clear_text():
    data_text.delete("1.0", END)  # Clear the text field

def check_missing_values():
    data_text.delete("1.0", END)  # Clear previous data
    data_text.insert(END, "Checking Date column is appropriate or not:\n")
    data_text.insert(END, str(df.dtypes) + "\n")  # Display the data types of columns
    data_text.insert(END, "\nCHECKING MISSING VALUES:\n")
    data_text.insert(END, str(df.isnull().sum()) + "\n")  # Display the missing values count

    data_text.insert(END, "\n\nCHECKING UNIQUE VALUES:\n")
    for column in df.select_dtypes(include='object'):
        data_text.insert(END, f"Column: {column}\n")
        data_text.insert(END, str(df[column].value_counts()) + "\n")
        data_text.insert(END, "\n")

def perform_data_cleaning():
    global df  # Access the global df variable
    columns_to_fill = df.columns[df.columns != 'Second Dose Administered']

    for column in columns_to_fill:
        df[column].fillna(method='bfill', inplace=True)
        df[column].fillna(method='ffill', inplace=True)

    data_text.delete("1.0", END)  # Clear previous data
    data_text.insert(END, "Data Cleaning:\n")
    data_text.insert(END, df.head())
    
def create_graph():
    global df  # Access the global df variable
    if df is not None:
        # Create bar chart
        if 'Total' in df.columns:
            min_vac = df.groupby('State')['Total'].sum().to_frame('Total')
            min_vac = min_vac.sort_values('Total')[:5]

            fig = plt.figure(figsize=(10, 5))
            plt.title("Least 5 Vaccinated States in India", size=20)
            sns.barplot(data=min_vac.iloc[:10], y="Total", x=min_vac.index, linewidth=2, edgecolor='black')
            plt.xlabel("States")
            plt.ylabel("Vaccination")
            plt.show()
        
            # Create a FigureCanvasTkAgg instance
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas.draw()
            canvas.get_tk_widget().place(relx=0.6, rely=0.5, anchor="center")
        
        # Create pie chart
        male = df["Male(Individuals Vaccinated)"].sum()
        female = df["Female(Individuals Vaccinated)"].sum()
        labels = ["Male", "Female"]
        values = [male, female]

        fig_pie = px.pie(names=labels, values=values, title="Male and Female Vaccination")
        fig_pie.show()

# Open and convert the JPEG image to PNG format
jpeg_image = Image.open("C:/Users/MBG Traders/Desktop/vaccine.jpg")
png_image = jpeg_image.convert("RGBA")

# Create a PhotoImage from the converted PNG image
image = ImageTk.PhotoImage(png_image)

# Set the window size to match the image size
root.geometry(f"{image.width()}x{image.height()}")

# Create Label in our window
img = Label(root, image=image)
img.place(x=0, y=0, relwidth=1, relheight=1)

# Define the background color for the buttons
button_bg_color = "#1f77b4"

# Create Text widget for displaying data
data_text = Text(root, font=("Arial", 12), width=60, height=20)
data_text.place(relx=0.05, rely=0.1, anchor="nw")

# Create Open File button
open_button = Button(
    root,
    text="Vaccination Data",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
    command=open_file
)
open_button.place(relx=0.1, rely=0.9, anchor="center")

# Check Missing Values button
button_check_missing_values = Button(
    root,
    text="Check Missing Values",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
    command=check_missing_values
)
button_check_missing_values.place(relx=0.3, rely=0.9, anchor="center")

# Data Cleaning button
button_data_cleaning = Button(
    root,
    text="Data Cleaning",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
    command=perform_data_cleaning
)
button_data_cleaning.place(relx=0.5, rely=0.9, anchor="center")

# Create Graph button
button_create_graph = Button(
    root,
    text="Create Graph",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
    command=create_graph
)
button_create_graph.place(relx=0.7, rely=0.9, anchor="center")

# Clear button
button_clear = Button(
    root,
    text="Clear",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
    command=clear_text
)
button_clear.place(relx=0.9, rely=0.9, anchor="center")

root.mainloop()


# In[15]:


from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title("Programming For Artificial Intelligence CCP")

# Define df as a global variable
df = None

# Function to handle button click event
def open_file():
    global df  # Access the global df variable
    path = 'C:/Users/MBG Traders/Desktop/covid_vaccine_statewise.csv'
    df = pd.read_csv(path)
    data_text.delete("1.0", END)  # Clear previous data
    data_text.insert(END, "Vaccination Data:\n")
    data_text.insert(END, df.head())

def clear_text():
    data_text.delete("1.0", END)  # Clear the text field

def check_missing_values():
    data_text.delete("1.0", END)  # Clear previous data
    data_text.insert(END, "Checking Date column is appropriate or not:\n")
    data_text.insert(END, str(df.dtypes) + "\n")  # Display the data types of columns
    data_text.insert(END, "\nCHECKING MISSING VALUES:\n")
    data_text.insert(END, str(df.isnull().sum()) + "\n")  # Display the missing values count

    data_text.insert(END, "\n\nCHECKING UNIQUE VALUES:\n")
    for column in df.select_dtypes(include='object'):
        data_text.insert(END, f"Column: {column}\n")
        data_text.insert(END, str(df[column].value_counts()) + "\n")
        data_text.insert(END, "\n")

def perform_data_cleaning():
    global df  # Access the global df variable
    columns_to_fill = df.columns[df.columns != 'Second Dose Administered']

    for column in columns_to_fill:
        df[column].fillna(method='bfill', inplace=True)
        df[column].fillna(method='ffill', inplace=True)

    data_text.delete("1.0", END)  # Clear previous data
    data_text.insert(END, "Data Cleaning:\n")
    data_text.insert(END, df.head())
    
def create_graph():
    global df  # Access the global df variable
    if df is not None:
        # Create bar chart
        if 'Total' in df.columns:
            min_vac = df.groupby('State')['Total'].sum().to_frame('Total')
            min_vac = min_vac.sort_values('Total')[:5]

            fig = plt.figure(figsize=(10, 5))
            plt.title("Least 5 Vaccinated States in India", size=20)
            sns.barplot(data=min_vac.iloc[:10], y="Total", x=min_vac.index, linewidth=2, edgecolor='black')
            plt.xlabel("States")
            plt.ylabel("Vaccination")
            plt.show()
        
            # Create a FigureCanvasTkAgg instance
            canvas = FigureCanvasTkAgg(fig, master=root)
            canvas.draw()
            canvas.get_tk_widget().place(relx=0.6, rely=0.5, anchor="center")
        
        # Create pie chart
        male = df["Male(Individuals Vaccinated)"].sum()
        female = df["Female(Individuals Vaccinated)"].sum()
        labels = ["Male", "Female"]
        values = [male, female]

        fig_pie = px.pie(names=labels, values=values, title="Male and Female Vaccination")
        fig_pie.show()

# Open and convert the JPEG image to PNG format
jpeg_image = Image.open("C:/Users/MBG Traders/Desktop/vaccine.jpg")
png_image = jpeg_image.convert("RGBA")

# Create a PhotoImage from the converted PNG image
image = ImageTk.PhotoImage(png_image)

# Set the window size to match the image size
root.geometry(f"{image.width()}x{image.height()}")

# Create Label in our window
img = Label(root, image=image)
img.place(x=0, y=0, relwidth=1, relheight=1)

# Define the background color for the buttons
button_bg_color = "#1f77b4"

# Create Text widget for displaying data
data_text = Text(root, font=("Arial", 12), width=60, height=20)
data_text.place(relx=0.05, rely=0.1, anchor="nw")

# Create Open File button
open_button = Button(
    root,
    text="Vaccination Data",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
    command=open_file
)
open_button.place(relx=0.1, rely=0.9, anchor="center")

# Check Missing Values button
button_check_missing_values = Button(
    root,
    text="Check Missing Values",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
    command=check_missing_values
)
button_check_missing_values.place(relx=0.3, rely=0.9, anchor="center")

# Data Cleaning button
button_data_cleaning = Button(
    root,
    text="Data Cleaning",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
    command=perform_data_cleaning
)
button_data_cleaning.place(relx=0.5, rely=0.9, anchor="center")

# Create Graph button
button_create_graph = Button(
    root,
    text="Create Graph",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
    command=create_graph
)
button_create_graph.place(relx=0.7, rely=0.9, anchor="center")

# Clear button
button_clear = Button(
    root,
    text="Clear",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
    command=clear_text
)
button_clear.place(relx=0.9, rely=0.9, anchor="center")

root.mainloop()


# In[ ]:




