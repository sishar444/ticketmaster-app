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
app_running = True # used to keep prompts running until this is set to False
is_last_page = False # used to check if we can load next page of results

def run():
    print(intro_header())
    # Prompt user to input for search keywords
    prompt_user_search_keywords()


    # Parse response
    # Print parsed response
    # Call print(search_results_header())
    # Prompt user to input a command


def intro_header():
    header = f"""
    -----------------------------------
        TICKETMASTER EVENTS LOOKUP
    -----------------------------------
    Welcome to the Ticketmaster search application!
    This app will let you search for any events with available tickets on the Ticketmaster platform.
    Please enter keyword(s) for a search to get started. Example search keywords are below:
        Search By   Examples
        --------- | ------------------
        Team      | 'New York Knicks'
        Artist    | 'Jay-Z'
        Show      | 'Harry Potter and the Cursed Child' """
    return header

def search_results_header():
    header = f"""
    -----------------------------------
    COMMANDS
    -----------------------------------
    'A' - New Search | 'N' - Next Page | 'P' - Previous Page | 'S' - Save Results | 'X' - Exit"""
    return header

def prompt_user_search_keywords():
    search_keywords = input("Search keyword(s): ")
    prompt_user_filters(search_keywords)

def prompt_user_filters(keywords):
    request_url, city, state, country = "", "", "", ""

    # Ask user if they would like to filter by city, state, or country
    will_filter = input("Would you like to filter your search by city, state, or country? (y/n): ")
    if will_filter.lower() == 'y':
        # If yes, give prompts for user to input city, state, and country
        city = input("Enter a city to filter your search. Hit ENTER to skip: ")
        state = input("Enter a state to filter your search. Hit ENTER to skip: ")
        country = input("Enter a country to filter your search. Hit ENTER to skip: ")
        request_url = build_request_url(keywords, city, state, country)
    else:
        request_url = build_request_url(keywords)
    # Make Api call with user inputs
    search_with_url(request_url)

def prompt_user_command():
    print(search_results_header())
    command = input("Enter a command: ")
    handle_user_commands(command)

# Performs actions based on command user inputs after search
def handle_user_commands(command):
    command_upper = command.upper()
    if command_upper == 'A':
        # Start new search
        prompt_user_search_keywords()
    elif command_upper == 'N':
        # Go to next page of results
        go_to_next_page()
    elif command_upper == 'P':
        # Go to previous page of results
        go_to_previous_page()
    elif command_upper == 'S':
        # Save results to file
        save_results_to_file()
    elif command_upper == 'X':
        quit("Thanks for using out app. Enjoy!")
    else:
        print("Sorry, we don't recognize that command. Please enter a new command.")
        prompt_user_command()

# ACTIONS

def search_with_url(url):
    print("Searching with url :", url)

def go_to_next_page():
    print("Going to next page")
    prompt_user_command()

def go_to_previous_page():
    if is_last_page:
        print("There are no more results.")
    prompt_user_command()

def save_results_to_file():
    print("Saving to file")
    prompt_user_command()

# HELPER METHODS

# Formats date into 'Month Day, Year'
def format_date_string(date_str):
    date_object = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    return date_object.strftime('%B %d, %Y')

def build_request_url(keywords, city=None, state=None, country=None):
    keyword_param = f"?keyword={keywords}"
    city_param, state_param, country_param = "", "", ""

    if city!=None and len(city)>0:
        city_param = f"&city={city}"
    if state!=None and len(state)>0:
        state_param = f"&state={state}"
    if country!=None and len(country)>0:
        country_param = f"&country={country}"

    request_url = base_url + keyword_param
    request_url += city_param
    request_url += state_param
    request_url += country_param
    return request_url

def parse_response(json):
    print("Parsing response json :", json)

if __name__ == "__main__": # "if this script is run from the command-line, then ..."
    run()
