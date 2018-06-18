from dotenv import load_dotenv
import requests
import json
import os
import datetime
import csv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path) # loads environment variables set in a ".env" file

api_key = os.environ.get("TICKETMASTER_API_KEY") or "OOPS. Please set an environment variable named 'TICKETMASTER_API_KEY'."

def run():
    print("Running application")

if __name__ == "__main__": # "if this script is run from the command-line, then ..."
    run()
