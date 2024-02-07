import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk
from tkinter import ttk

file = 'gamelist.csv'
df = pd.read_csv(file, header=0)
df.columns = ['GameResult', 'GameType', 'GameLength', 'GameChamp', 'GameKill', 'GameDeath', 'GameAssist']
df1 = df[['GameChamp','GameKill','GameDeath','GameAssist']].groupby('GameChamp').mean()
df2 = df[['GameKill','GameDeath']]
df3 = df[['GameKill','GameDeath','GameAssist']]

#Design
SMALL_FONT = ("Calibri", 12)
LARGE_FONT = ("Arial", 16)

# Background Frame Setup
class GameScraperapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        #Add Icon
        #tk.Tk.iconbitmap(self, default="clienticon.ico")
        tk.Tk.wm_title(self, "GameScraper")
        tk.Tk.wm_geometry(self,"1920x1080")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        username = ""
        self.frames = {}
        for Frames in (StartPage, RegChart, ScatterChart, ChampKillBar):
            frame = Frames(container, self)
            self.frames[Frames] = frame
            frame.grid(row=0, column = 0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, background='white')
        titlelabel = tk.Label(self, text="GameScraper", font=LARGE_FONT)
        titlelabel.pack(pady=10, padx=10)

     #Buttons

        button1 = ttk.Button(self, text="KDA Trends",
                            command=lambda: controller.show_frame(RegChart))
        button1.pack(pady=10, padx=10)
        button2 = ttk.Button(self, text="KDA Scatter",
                            command=lambda: controller.show_frame(ScatterChart))
        button2.pack(pady=10, padx=10)
        button3 = ttk.Button(self, text="Champ Stats",
                            command=lambda: controller.show_frame(ChampKillBar))
        button3.pack(pady=10, padx=10)

# Trend Line Charts for Recent History
class RegChart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="KDA Trends", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="KDA Scatter",
                             command=lambda: controller.show_frame(ScatterChart))
        button2.pack()
        button3 = ttk.Button(self, text="Champ Stats",
                             command=lambda: controller.show_frame(ChampKillBar))
        button3.pack()

        # Display the data in a text widget
        text_widget = tk.Text(self, wrap=tk.WORD, height=20, width=80)
        text_widget.pack(pady=10, padx=10)

        # Get the data and convert it to a string for display
        data_str = df3.to_string(index=True)

        # Insert the data into the text widget
        text_widget.insert(tk.END, data_str)


# Scatter Plot - Need: Regression Analysis (May Convert to Seaborn App)
class ScatterChart(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="KDA Scatter", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="KDA Trends",
                             command=lambda: controller.show_frame(RegChart))
        button2.pack()
        button3 = ttk.Button(self, text="Champ Stats",
                             command=lambda: controller.show_frame(ChampKillBar))
        button3.pack()

        # Display the data in a text widget
        text_widget = tk.Text(self, wrap=tk.WORD, height=20, width=80)
        text_widget.pack(pady=10, padx=10)

        # Get the data and convert it to a string for display
        data_str = df2.to_string(index=True)

        # Insert the data into the text widget
        text_widget.insert(tk.END, data_str)


# KDA Bar Chart for recent Champions Played - Want: Build in Sorting button for sorting K/D/A
class ChampKillBar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Avg Champ Kills", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="KDA Scatter",
                             command=lambda: controller.show_frame(ScatterChart))
        button2.pack()
        button3 = ttk.Button(self, text="KDA Trends",
                             command=lambda: controller.show_frame(RegChart))
        button3.pack()

        # Display the data in a text widget
        text_widget = tk.Text(self, wrap=tk.WORD, height=20, width=80)
        text_widget.pack(pady=10, padx=10)

        # Get the data and convert it to a string for display
        data_str = df1.to_string(index=True)

        # Insert the data into the text widget
        text_widget.insert(tk.END, data_str)


app = GameScraperapp()
app.mainloop()
