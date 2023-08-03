from tkinter import *
from PIL import Image, ImageTk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def show_active_cases():

    active_cases_window = Toplevel(root)
    active_cases_window.title("Active Cases Chart")


    india_data = pd.read_csv(r"C:\Users\MBG Traders\Downloads\your_dataset_without_outliers.csv")

    india_data['Active'] = india_data['Confirmed'] - (india_data['Deaths'] + india_data['Cured'])

    india_state_data = india_data.groupby("State/UnionTerritory", as_index=False)["Active"].max().nlargest(10, "Active")


    global_data = pd.read_csv(r"C:\Users\MBG Traders\Desktop\worldometer_coronavirus_daily_data.csv")

    global_data['Active'] = global_data['Confirmed'] - (global_data['Death'] + global_data['Cured'])

    global_country_data = global_data.groupby("country", as_index=False)["Active"].max().nlargest(10, "Active")

    fig, ax = plt.subplots(figsize=(8, 6))

    india_bars = ax.bar(india_state_data["State/UnionTerritory"], india_state_data["Active"], color="blue", label="Top 10 Indian States")

    global_bars = ax.bar(global_country_data["country"], global_country_data["Active"], color="red", label="Top 10 Countries")

    ax.set_xlabel("States/Countries")
    ax.set_ylabel("Active Cases")
    ax.set_title("Comparison of Top 10 Active Cases (India vs Global)")

    plt.xticks(rotation=45, ha='right', fontsize=10)

    for bar in india_bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, height, ha='center', va='bottom', color='white', fontweight='bold', fontsize=10, rotation=45)

    for bar in global_bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, height, ha='center', va='bottom', color='white', fontweight='bold', fontsize=10, rotation=45)

    ax.grid(True, linestyle="--", alpha=0.4)

    ax.legend(loc="upper right", bbox_to_anchor=(1, 1))

    ax.set_facecolor('#1c1c1c')

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    canvas = FigureCanvasTkAgg(fig, master=active_cases_window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    active_cases_window.mainloop()
    
def show_death_confirmed():

    death_confirmed_window = Toplevel(root)
    death_confirmed_window.title("Deaths and Confirmed Chart")
    india_data = pd.read_csv(r"C:\Users\MBG Traders\Downloads\your_dataset_without_outliers.csv")
    top_10_states = india_data.groupby("State/UnionTerritory").max().nlargest(10, "Deaths")
    confirmed_cases_india = top_10_states["Confirmed"]
    deaths_india = top_10_states["Deaths"]
    states_india = top_10_states.index
    global_data = pd.read_csv(r"C:\Users\MBG Traders\Desktop\worldometer_coronavirus_daily_data.csv")
    top_10_countries = global_data.groupby("country").max().nlargest(10, "Death")
    confirmed_cases_global = top_10_countries["Confirmed"]
    deaths_global = top_10_countries["Death"]
    countries_global = top_10_countries.index
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(deaths_india, confirmed_cases_india, color="blue", label="Top 10 Indian States")
    ax.scatter(deaths_global, confirmed_cases_global, color="red", label="Top 10 Countries")
    for i, state in enumerate(states_india):
        ax.annotate(state, (deaths_india.iloc[i], confirmed_cases_india.iloc[i]),
                     textcoords="offset points", xytext=(10, 0), ha='center', fontsize=8)
    for i, country in enumerate(countries_global):
        ax.annotate(country, (deaths_global.iloc[i], confirmed_cases_global.iloc[i]),
                     textcoords="offset points", xytext=(10, 0), ha='center', fontsize=8)
    ax.set_xlabel("Deaths")
    ax.set_ylabel("Confirmed Cases")
    ax.set_title("Relationship between Deaths and Confirmed Cases")
    ax.grid(True, linestyle="--", alpha=0.4)
    ax.legend(loc="upper left", bbox_to_anchor=(1, 1))
    ax.set_facecolor((0.2, 0.4, 0.6))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    canvas = FigureCanvasTkAgg(fig, master=death_confirmed_window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    death_confirmed_window.mainloop()


def show_recovery_mortality():
    recovery_mortality_window = Toplevel(root)
    recovery_mortality_window.title("Recovery and Mortality Chart")
    india_data = pd.read_csv("C:\\Users\MBG Traders\Downloads\\your_dataset_without_outliers.csv")
    overall_mortality_india = (india_data['Deaths'].sum() / india_data['Confirmed'].sum()) * 100
    overall_recovery_india = (india_data['Cured'].sum() / india_data['Confirmed'].sum()) * 100
    global_data = pd.read_csv('C:/Users/MBG Traders/Desktop/worldometer_coronavirus_daily_data.csv')
    # Calculate the overall mortality and recovery rates globally
    overall_mortality_global = (global_data['Death'].sum() / global_data['Confirmed'].sum()) * 100
    overall_recovery_global = (global_data['Cured'].sum() / global_data['Confirmed'].sum()) * 100
    fig = plt.figure(figsize=(9, 6))
    colors = ['#28a745', '#dc3545', '#ff5733', '#ffa500']
    plt.bar(['India (Mortality)', 'India (Recovery)', 'Global (Mortality)', 'Global (Recovery)'],
            [overall_mortality_india, overall_recovery_india, overall_mortality_global, overall_recovery_global],
            color=colors)
    # Set the axis labels and title
    plt.xlabel('Dataset', fontsize=12, fontweight='bold', color='white')
    plt.ylabel('Rate (%)', fontsize=12, fontweight='bold', color='white')
    plt.title('Comparison of Overall Mortality and Recovery Rates (India vs Global)',
              fontsize=14, fontweight='bold', color='white')
    label_fontsize = 10
    for i, rate in enumerate([overall_mortality_india, overall_recovery_india,
                              overall_mortality_global, overall_recovery_global]):
        plt.text(i, rate + 1, f'{rate:.2f}%', ha='center', va='bottom',
                 fontsize=label_fontsize, color='white')
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.xticks(fontsize=10, color='white')
    plt.yticks(fontsize=10, color='white')
    plt.gca().set_facecolor('#333333')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    canvas = FigureCanvasTkAgg(fig, master=recovery_mortality_window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    recovery_mortality_window.mainloop()


root = Tk()
root.title("Programming For Artificial Intelligence CCP")

# Open and convert the JPEG image to PNG format
jpeg_image = Image.open(r"C:\Users\MBG Traders\Desktop\comparision.jpeg")
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
    text="Active Cases",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
    command=show_active_cases  # Call the show_active_cases function when clicked
)
button1.place(relx=0.3, rely=0.9, anchor="center")

button2 = Button(
    root,
    text="Death and Confirmed",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
    command=show_death_confirmed
)
button2.place(relx=0.5, rely=0.9, anchor="center")

button3 = Button(
    root,
    text="Recovery and Mortality",
    relief=RAISED,
    bg=button_bg_color,
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=3,
    activebackground=button_bg_color,
    activeforeground="white",
    command= show_recovery_mortality
)
button3.place(relx=0.7, rely=0.9, anchor="center")

root.mainloop()
