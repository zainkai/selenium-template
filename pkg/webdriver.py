from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from config.configuration import Config
from time import sleep

class WebDriver:
  def __init__(self, url: str):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-notifications")

    self.Driver = webdriver.Chrome(chrome_options=options, executable_path=Config.get("chrome_path"))
    self.Driver.get(url)

  def Done(self):
    sleep(1)
    self.Driver.quit()