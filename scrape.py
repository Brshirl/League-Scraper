from bs4 import BeautifulSoup as bs
from selenium import webdriver as driver
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import ttk

# Input User
SMALL_FONT = ("Calibri", 12)
LARGE_FONT = ("Arial", 16)

# Login tkinter page
root = tk.Tk()
root.geometry("300x100")
user = None
root.wm_title("GameScraper")


# Button click, closes Login window and runs GameScraper for CSV
def loginbtnclick():
    global user
    user = str(userInput.get("1.0", "end-1c"))
    root.destroy()


userInput = tk.Text(root, height=1, width=10)
userInput.pack()

button1 = ttk.Button(root, text="Login", command=lambda: loginbtnclick())
button1.pack()
print(user)
root.mainloop()

# File Name/ Site Variables
username = user.replace(" ", "%20")
print(username)
filename = "gamelist.csv"
site = 'https://www.op.gg/summoners/na/' + username


# Grab Page
edgedriver_path = "C:\\Users\\shirl\\Projects\\League\\msedgedriver.exe"
ffdriver = driver.Edge(executable_path=edgedriver_path)
ffdriver.get(site)

# HTML Parsing
page_bs = bs(ffdriver.page_source, "html.parser")

# Iterate over webpage to retrieve up to 100 games
x = 0
while x < 100:
    try:
        ffdriver.find_element(By.XPATH, "//a[text()='Show More']").click()
        ffdriver.implicitly_wait(20)
    except Exception as e:
        print(f"An error occurred: {e}")
        break
    x += 1

# Find all main containers
containers = page_bs.findAll("div", {"class": "css-1jxewmm e1mwhike0"})
# Iterate over each main container
for container in containers:
    # Create a new GameListContainer for each iteration
    GameListContainer = {}

    # Find the inner container within each main container
    inner_container = container.find("div", {"class": "css-j7qwjs e4p6qc60"})

    if inner_container:
        # Find the contents within the inner container
        contents = inner_container.find("div", {"class": "main"})
        print(contents)

                                

# Open/Write CSV
with open(filename, "w") as f:
    headers = "Game_Result, Game_Type, Game_Length, Champ_Played, Kills, Deaths, Assists, Tier, LP\n"
    f.write(headers)
    print(f"Found {len(containers)} containers")
    
    # Find Results in Containers Loop
    for container in containers:
        # Game Results
        GameResults = container.findAll("div", {"class": "GameResult"})
        GameResult = GameResults[0].text.strip()

        # Game Type
        GameTypes = container.findAll("div", {"class": "GameType"})
        GameType = GameTypes[0].text.strip()

        # Time Played
        GameLengths = container.findAll("div", {"class": "GameLength"})
        GameLength = GameLengths[0].text.strip()

        # Champion Played
        GameChamps = container.findAll("div", {"class": "ChampionName"})
        GameChamp = GameChamps[0].text.strip()

        # Kills
        GameKills = container.findAll("span", {"class": "Kill"})
        GameKill = GameKills[0].text.strip()

        # Deaths
        GameDeaths = container.findAll("span", {"class": "Death"})
        GameDeath = GameDeaths[0].text.strip()

        # Assists
        GameAssists = container.findAll("span", {"class": "Assist"})
        GameAssist = GameAssists[0].text.strip()

        # Write to CSV
        f.write(
            GameResult + ","
            + GameType + ","
            + GameLength + ","
            + GameChamp + ","
            + GameKill + ","
            + GameDeath + ","
            + GameAssist + ","
            + GameListContainer.get('tier', '') + ","
            + GameListContainer.get('lp', '') + "\n"
        )

print("File created called " + filename)

# Open a file for reading
with open("gamelist.csv", "r") as file:
    # Read the whole file
    content = file.read()
    print(content)

# Close the driver
ffdriver.close()
#exec(open('app.py').read())
