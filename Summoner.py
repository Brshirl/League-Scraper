from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver as driver
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import ttk


url = 'https://www.op.gg/summoners/na/YukonCornelius-9296'

# Set up the WebDriver (you need to have the appropriate WebDriver executable, e.g., chromedriver, in your PATH)
edgedriver_path = "C:\\Users\\shirl\\Projects\\League\\msedgedriver.exe"
ffdriver = driver.Edge(executable_path=edgedriver_path)
ffdriver.get(url)

# Wait for the page to load (you may need to adjust the waiting time)
ffdriver.implicitly_wait(10)

# Find the table rows using Selenium
rows = ffdriver.find_elements_by_css_selector('.css-17mfto3.ehp118b0 tbody tr')

# Extract data from each row and create a list of dictionaries
data_list = []
for row in rows:
    columns = row.find_elements_by_tag_name('td')
    if len(columns) == 4:  # Ensure the correct number of columns
        data_list.append({
            'Summoner': columns[0].text.strip(),
            'Played': columns[1].text.strip(),
            'Win-Lose': columns[2].text.strip(),
            'Win Rate': columns[3].text.strip(),
        })

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(data_list)

# Print the dataframe
print("\n\nPANDAS DATAFRAME\n")
print(df)

# Close the WebDriver
driver.quit()
