import sys

def generate_key():
    try:
        with open("key.txt") as api_key:
            key = api_key.readlines()[0].strip()
    except FileNotFoundError:
        print("A CanLII API key is required to process this request")
        sys.exit()

    return key
