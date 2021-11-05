from Xlib.X import Button1
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
import pyautogui


opciones = webdriver.ChromeOptions()
opciones.add_argument('--start-maximized')
opciones.add_argument('--disable-extentions')

driver_path= '/usr/local/bin/chromedriver'

driver = webdriver.Chrome(driver_path, chrome_options=opciones)

driver.set_window_position(2000,0)
driver.maximize_window()
time.sleep(1)

driver.get('https://google.com')

