from headless_chrome import create_driver
from selenium.webdriver.common.by import By

def lambda_handler(_event=None, _context=None):
    driver = create_driver()
    target_url = "https://www.example.edu/"
    driver.get(target_url)
    
    try:
        h1_element = driver.find_element(By.XPATH, "//h1")
        h1_text = h1_element.text
    except Exception as e:
        h1_text = f"Error: {str(e)}"
        print(f"Error occurred in script 4: {h1_text}")
    
    driver.quit()
    
    result = {
        'body': f'<h1>: {h1_text}'
    }

    return result

if __name__ == "__main__":
    lambda_handler()