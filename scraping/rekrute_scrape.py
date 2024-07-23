from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import base64

chrome_options = Options()
chrome_options.add_argument("--headless")  
