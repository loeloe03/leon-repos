from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start de Selenium-webdriver (zorg ervoor dat je de webdriver hebt geïnstalleerd)
driver = webdriver.Chrome()

# Ga naar de website
driver.get("https://www.bk-feedback-nl.com")

# Wacht tot de "NextButton" zichtbaar is (maximaal 10 seconden wachten)
next_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "NextButton"))
)

# Klik op de "NextButton"
next_button.click()

# Sluit de webdriver als je klaar bent
