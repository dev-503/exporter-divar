# Import necessary modules for web automation and data handling
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


def scrape_divar(search_query: str, output_file: str) -> None:
    """
    Scrapes ads from Divar based on the given search query and saves the results to an Excel file.

    Args:
        search_query (str): The keyword to search for on the Divar platform.
        output_file (str): The file path where the extracted data will be saved.

    Returns:
        None
    """
    # Configure browser options for Selenium
    options = Options()
    options.add_argument('--start-maximized')  # Launch browser in maximized mode
    options.add_argument('--disable-blink-features=AutomationControlled')  # Reduce automation detection

    # Initialize WebDriver with the configured options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Open the target website
        driver.get("https://divar.ir/s/tehran")
        # Wait for the page to fully load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Locate the search input field and perform a search
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "input"))
        )
        search_box.send_keys(search_query)  # Enter the search query
        search_box.send_keys(Keys.RETURN)  # Submit the search
        time.sleep(5)  # Allow results to load

        # Prepare to scroll and collect ads
        ads = []
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Extract ads from the current page
            ad_elements = driver.find_elements(By.CLASS_NAME, "kt-post-card")
            for ad in ad_elements:
                try:
                    # Extract ad details
                    title = ad.find_element(By.CLASS_NAME, "kt-post-card__title").text
                    price = ad.find_element(By.CLASS_NAME, "kt-post-card__description").text
                    location = ad.find_element(By.CLASS_NAME, "kt-post-card__bottom-description").text
                    link = ad.find_element(By.TAG_NAME, "a").get_attribute("href")

                    # Append ad details to the list
                    ads.append({
                        'Title': title,
                        'Price': price,
                        'Location': location,
                        'Link': link
                    })
                except Exception as e:
                    print(f"Warning: Unable to extract ad details - {e}")

            # Scroll down to load more ads
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)  # Allow new ads to load

            # Check if scrolling has reached the bottom
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        # Save the extracted data to an Excel file
        if ads:
            df = pd.DataFrame(ads)
            df.to_excel(output_file, index=False)
            print(f"Data saved successfully to {output_file}")
        else:
            print("No ads found to save.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Ensure the browser is closed, even if an error occurs
        driver.quit()


if __name__ == "__main__":
    # Define search parameters
    search_query = "206 سفید"  # Example search term (e.g., "206 White")
    output_file = "divar_ads.xlsx"  # Output file path

    # Execute the scraping function
    scrape_divar(search_query, output_file)
