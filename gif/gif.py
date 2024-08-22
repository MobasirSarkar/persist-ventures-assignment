from selenium import webdriver
import time
import pyperclip
from selenium.webdriver.common.by import By
from concurrent.futures import ThreadPoolExecutor


class Gif:

    def __init__(self, gif_id, driver):
        self.gif_id = gif_id
        self.driver = driver

    def search_gif(self):
        driver = self.driver
        driver.get(f"https://tenor.com/view/{self.gif_id}")
        time.sleep(2)
        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = [executor.submit(self.click_and_copy) for _ in range(100)]
            for future in futures:
                try:
                    future.result()
                except Exception as e:
                    print(f"An error has occured{e}")
        time.sleep(2)

    def click_and_copy(self):
        driver = self.driver
        try:
            element = driver.find_element(
                By.XPATH,
                "/html/body/div/div/div[3]/div[1]/div[2]/div[3]/div[1]/input",
            )

            driver.execute_script("arguments[0].scrollIntoView(true);", element)
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
            print(f"An Error has occured : {e}")
