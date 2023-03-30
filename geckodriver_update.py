from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# create a new Firefox service using the geckodriver executable managed by webdriver-manager
firefox_service = Service(executable_path=GeckoDriverManager().install())