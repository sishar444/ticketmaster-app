from dotenv import load_dotenv
from pathlib import Path
import requests
import json
import os
import datetime
import csv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path) # loads environment variables set in a ".env" file

# GLOBAL VARIABLES
api_key = os.environ.get("TICKETMASTER_API_KEY") or "OOPS. Please set an environment variable named 'TICKETMASTER_API_KEY'."
base_url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={api_key}"
is_last_page = False # used to check if we can load next page of results

def run():
    print(intro_header())

def intro_header():
    header = f"""
    -----------------------------------
    TICKETMASTER EVENTS LOOKUP
    -----------------------------------
    Welcome to the Ticketmaster search application!
    This app will let you search for any events with available tickets on the Ticketmaster platform.
    Please enter a search term to get started. Example search terms are below:
        Search By   Examples:
        --------- | ------------------
        Team      | 'New York Knicks'
        Artist    | 'Jay-Z'
        Show      | 'Harry Potter and the Cursed Child' """
    return header

def search_results_header():
    print("")

# HELPER METHODS

# Formats date into 'Month Day, Year'
def format_date_string(date_str):
    date_object = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    return date_object.strftime('%B %d, %Y')

if __name__ == "__main__": # "if this script is run from the command-line, then ..."
    run()
