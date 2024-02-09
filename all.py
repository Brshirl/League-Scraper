# Importing requests and BeautifulSoup libraries
from bs4 import BeautifulSoup as bs
from selenium import webdriver as driver
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import ttk
import requests
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}
res = requests.get('https://www.op.gg/summoners/na/YukonCornelius-9296', headers=headers)
url = 'https://www.op.gg/summoners/na/YukonCornelius-9296'

edgedriver_path = "C:\\Users\\shirl\\Projects\\League\\msedgedriver.exe"
ffdriver = driver.Edge(executable_path=edgedriver_path)
ffdriver.get(url)
ffdriver.implicitly_wait(10)

soup = bs(res.content, 'html.parser')
page_title = soup.title.text

print(f"Page Title: {page_title}\n")
slash = '------------------------------------------------------------------------'
print('S2024 Split 1 Stats\n')

champion_boxes = soup.find_all('div', {'class': 'champion-box'})
for champion_box in champion_boxes:
    champion_info = champion_box.find('div', {'class': 'info'}).text.strip()
    champion_kda = champion_box.find('div', {'class': 'kda'}).text.strip()
    champion_play = champion_box.find('div', {'class': 'played'}).text.strip()
    print(f"Champion Info: {champion_info}, KDA: {champion_kda}, Play Rate: {champion_play}")
print(slash+'\n')
#
print('Seven day Ranked Stats')

stat_box = soup.find('div', {'class': 'css-1v1ie3n e1pwffi60'})
if stat_box:
    info_elements = stat_box.find_all('div', {'class': 'info'})
    graph_elements = stat_box.find_all('div', {'class': 'graph'})
    winratio_elements = stat_box.find_all('div', {'class': 'winratio'})

    # Create lists to store data
    champions = []
    win_rates = []

    for info, graph, winratio in zip(info_elements, graph_elements, winratio_elements):
        info_text = info.text.strip()
        graph_text = graph.text.strip()
        winratio_text = winratio.text.strip()
        
        champions.append(info_text)
        win_rates.append(float(winratio_text.rstrip('%')) / 100)  # Convert win ratio to a float between 0 and 1

        print(f"Champion: {info_text}, Graph: {graph_text}, Win Rate: {winratio_text}")
else:
    print("No 'css-1v1ie3n e1pwffi60' element found.")
print(slash + '\n')

stats_df = pd.DataFrame({'Champion': champions, 'Win Rate': win_rates})
#pie chart
plt.figure(figsize=(8, 8))
plt.pie(stats_df['Win Rate'], labels=stats_df['Champion'], autopct='%1.1f%%', startangle=140)
plt.title('Seven day Ranked Win Rates')
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(stats_df['Champion'], stats_df['Win Rate'], color='blue')
plt.title('Seven day Ranked Win Rates')
plt.xlabel('Champion')
plt.ylabel('Win Rate')
plt.show()



#div class css-10e7s6g ehma9yf0 is the main class
# div class summary which holds classes css-12oj9o5 ehma9yf1,summary-graph,css-12oj9o5 ehma9yf1
#thead that has op, score, kda, damage, wards, cs, items
#table result = lose and then a table result = win for each player in game
#table result td champion spells runes etc 

