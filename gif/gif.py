import time
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Gif:
    def __init__(self, gif_id, driver):
        self.gif_id = gif_id
        self.driver = driver

    def search_gif(self):
        driver = self.driver
        driver.get(f"https://tenor.com/view/{self.gif_id}")
        time.sleep(1)
        for _ in range(100):
            try:
                driver.execute_script("window.scrollBy(0,400)")
                element = driver.find_element(
                    By.XPATH,
                    "/html/body/div/div/div[3]/div[1]/div[2]/div[3]/div[1]/input",
                )
                driver.execute_script(
                    "window.scrollBy(0,arguments[0].getBoundingClientRect().top - 100)",
                    element,
                )
                time.sleep(2)
                element.click()
                time.sleep(2)

                copied_link = pyperclip.paste()

                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(copied_link)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            except Exception as e:
                print(f"An error occurred: {e}")
                break  # Optional: exit the loop on error
