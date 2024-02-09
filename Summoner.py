from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup as bs
from selenium import webdriver as driver
from selenium.webdriver.common.by import By
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import requests

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

