from selenium import webdriver
from gif.gif import Gif


def process_gif(gif_id):
    driver = webdriver.Chrome()
    driver.maximize_window()
    gif = Gif(gif_id, driver)
    gif.search_gif()
    driver.quit()


if __name__ == "__main__":
    gif_id = ["one-piece-monkey-d-luffy-straw-hat-luffy-lol-gif-16566941"]
    process_gif(gif_id)
