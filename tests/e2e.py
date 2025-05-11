from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

def test_scores_service(url):
    try:
        # Launch browser (headless Chrome for automation)
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)

        # Open the application
        driver.get(url)
        time.sleep(2)  # Let the page load

        # Find the score element
        score_element = driver.find_element(By.ID, "score")
        score = int(score_element.text)

        # Close browser
        driver.quit()

        # Check if score is between 1 and 1000
        return 1 <= score <= 1000

    except Exception as e:
        print(f"Test failed due to: {e}")
        return False


def main():
    url = "http://localhost:8777"  # Change to your actual URL
    if test_scores_service(url):
        print("Test passed.")
        sys.exit(0)
    else:
        print("Test failed.")
        sys.exit(-1)


if __name__ == "__main__":
    main()
