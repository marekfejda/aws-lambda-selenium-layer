# AWS Lambda Selenium Layer

A precompiled AWS Lambda layer that bundles Selenium, Headless Chrome, and Chromedriver for Python-based headless environments in AWS Lambda.

## Features
- **Headless Chrome Version:** 86.0.4240.111
- **Selenium Version:** 4.31.1
- **Supported Python Versions:**  
  - 3.8: ❌  
  - 3.9: ✅  
  - 3.10: ✅  
  - 3.11: ✅  
  - 3.12: ❌  

### Why Use This?
This layer simplifies deploying Selenium-based automation and testing in AWS Lambda, ensuring compatibility and saving setup time. It stays within the **AWS Free Tier**, making it cost-effective for small to medium-scale use.

---

## Getting Started

### Prerequisites
- AWS CLI configured with appropriate permissions.
- AWS Lambda and S3 setup.
- Python (3.9, 3.10, or 3.11) for running Selenium scripts.

### Uploading the Layer to AWS
1. **Download the precompiled layer:**
   - Clone or download the `layer.zip` from the repository.

2. **Upload to S3:**
   - Replace `<your-bucket-name>` and `<layer-name>` with your values.
     ```bash
     aws s3 cp layer.zip s3://<your-bucket-name>/<layer-name>.zip
     ```

3. **Deploy the layer in AWS Lambda:**
   - Use the AWS CLI to create a new Lambda layer:
     ```bash
     aws lambda publish-layer-version \
       --layer-name "<layer-name>" \
       --description "Selenium with headless Chrome for AWS Lambda" \
       --content S3Bucket=<your-bucket-name>,S3Key=<layer-name>.zip \
       --compatible-runtimes python3.9 python3.10 python3.11 \
       --license-info "MIT"
     ```

4. **Attach the Layer to Your Lambda Function:**
   - Go to your Lambda function in the AWS Console.
   - In the **Layers** section, choose "Add a layer."
   - Select "Custom layers" and choose the layer you uploaded.

---

## Examples

The `/examples` directory provides sample scripts demonstrating how to use the AWS Lambda Selenium layer effectively.

### 1. Hello World Example
File: `/examples/helloworld.py`

A simple Lambda function that:
1. Initializes a Selenium driver using `create_driver` from the `headless_chrome` library.
2. Opens a URL (`https://www.example.com/`).
3. Fetches and returns the title of the website.

**Code:**
```python
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
