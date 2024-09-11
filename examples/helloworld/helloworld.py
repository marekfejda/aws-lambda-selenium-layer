from headless_chrome import create_driver

def lambda_handler(_event, _context):
    driver = create_driver()
    
    target_url = "https://www.example.com/"
    print(f"Opening URL: {target_url}")
    driver.get(target_url)
    
    try:
        website_title = driver.title
        print(f"The website title is: {website_title}")
    except Exception as e:
        website_title = f"Error: {str(e)}"
        print(f"Error occurred while fetching the title: {website_title}")
    
    driver.quit()

    result = {
        'statusCode': 200,
        'body': f'The website title is: {website_title}'
    }
    print("Returning result:", result)
    
    return result
