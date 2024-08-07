import time
import random
import requests


def retry_with_backoff(func, max_retries=5, initial_delay=1):
    # TODO: implement using urllib3 Retry
    retries = 0
    while retries < max_retries:
        try:
            return func()
        except Exception as e:
            print(f"Request failed: {e}. Retrying in {initial_delay} seconds...")
            time.sleep(initial_delay)
            retries += 1
            initial_delay *= 2  # Exponential backoff
            initial_delay += random.random()  # Add jitter to avoid synchronized retries
    raise Exception("Max retries exceeded")


# Example Usage (assuming 'upload_file' is a function that makes an API request to upload a file)
def upload_file(file_path):
    # TODO: (Implementation to upload the file)
    ...


result = retry_with_backoff(lambda: upload_file("my_file.txt"))
print(result)
