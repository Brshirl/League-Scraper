# Importing requests and BeautifulSoup libraries
from bs4 import BeautifulSoup as bs
from selenium import webdriver as driver
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import ttk
import requests
import pandas as pd

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

    for info, graph, winratio in zip(info_elements, graph_elements, winratio_elements):
        info_text = info.text.strip()
        graph_text = graph.text.strip()
        winratio_text = winratio.text.strip()
        print(f"Champion: {info_text}, Graph: {graph_text}, Win Rate: {winratio_text}")
else:
    print("No 'css-1v1ie3n e1pwffi60' element found.")
print(slash+'\n')
#
rows = ffdriver.find_elements_by_css_selector('.css-17mfto3.ehp118b0 tbody tr')
data_list = []
for row in rows:
    columns = row.find_elements_by_tag_name('td')
    if len(columns) == 4:  
        data_list.append({
            'Summoner': columns[0].text.strip(),
            'Played': columns[1].text.strip(),
            'Win-Lose': columns[2].text.strip(),
            'Win Rate': columns[3].text.strip(),
        })
df = pd.DataFrame(data_list)
print("\n\nPANDAS DATAFRAME\n")
print(df)
print(slash+'\n')
#

# Make Loop to loop through game list

main_container = soup.find('div', {'class': 'css-1jxewmm e1y8psvp0'})

if main_container:
    print("Main Container Found")
    print(main_container.contents)  # Print the HTML content of the main container

    # Find all div elements within the main container
game_boxes = main_container.find_all('div', {'class': 'css-j7qwjs e4p6qc60'})
print(game_boxes)

