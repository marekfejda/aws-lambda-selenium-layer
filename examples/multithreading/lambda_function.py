import threading
import script1
import script2
import script3
import script4

def run_script(script_module, result_key, result, retries=3):
    attempt = 0
    while attempt < retries:
        try:
            result[result_key] = script_module.lambda_handler()
            print(f"{result_key} finished with result:", result[result_key])
            break
        except Exception as e:
            print(f"Error occurred in {result_key}: {str(e)}. Retrying...")
            attempt += 1
            if attempt == retries:
                result[result_key] = f"Error: {str(e)}"
                
def lambda_handler(event, context):
    results = {}
    
    threads = [
        threading.Thread(target=run_script, args=(script1, 'script1', results)),
        threading.Thread(target=run_script, args=(script2, 'script2', results)),
        threading.Thread(target=run_script, args=(script3, 'script3', results)),
        threading.Thread(target=run_script, args=(script4, 'script4', results))
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return {
        'statusCode': 200,
        'body': {
            'example.com': results.get('script1', 'No result from script1'),
            'example.org': results.get('script2', 'No result from script2'),
            'example.net': results.get('script3', 'No result from script3'),
            'example.edu': results.get('script4', 'No result from script4')
        }
    }