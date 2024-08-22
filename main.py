from selenium import webdriver
from gif.gif import Gif
from concurrent.futures import ThreadPoolExecutor


def process_gif(gif_id):
    driver = webdriver.Chrome()
    driver.maximize_window()
    gif = Gif(gif_id, driver)
    gif.search_gif()
    driver.quit()


if __name__ == "__main__":
    gif_id = ["luffy-gear-5-luffy-monkey-d-luffy-one-piece-wano-gif-241855050869579563"]

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process_gif, gif_id) for _ in range(10)]

    for future in futures:
        future.result()
