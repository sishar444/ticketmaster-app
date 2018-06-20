# ticketmaster-app/tests/test_script.py
from dotenv import load_dotenv
from pathlib import Path
import os

from app.events_lookup import format_date_string
from app.events_lookup import build_request_url

def test_format_date_string():
    test_date = "2018-09-22"
    expected_result = "September 22, 2018"
    result = format_date_string(test_date)
    assert result == expected_result

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path) # loads environment variables set in a ".env" file
api_key = os.environ.get("TICKETMASTER_API_KEY")
base_url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={api_key}"

def test_build_url_no_params():
    keywords = "Knicks"
    expected_url = base_url + f"?keyword={keywords}"
    url = build_request_url(keywords)
    assert url == expected_url

def test_build_url_city():
    keywords = "Knicks"
    city = "NY"
    expected_url = base_url + f"?keyword={keywords}" + f"&city={city}"
    url = build_request_url(keywords, city, "", "")
    assert url == expected_url

def test_build_url_state():
    keywords = "Knicks"
    state = "NY"
    expected_url = base_url + f"?keyword={keywords}" + f"&state={state}"
    url = build_request_url(keywords, "", state, "")
    assert url == expected_url

def test_build_url_country():
    keywords = "Knicks"
    country = "US"
    expected_url = base_url + f"?keyword={keywords}" + f"&country={country}"
    url = build_request_url(keywords, "", "", country)
    assert url == expected_url

def test_build_url_city_state_country():
    keywords = "Knicks"
    city = "NY"
    state = "NY"
    country = "US"
    expected_url = base_url + f"?keyword={keywords}" + f"&city={city}" + f"&state={state}" + f"&country={country}"
    url = build_request_url(keywords, city, state, country)
    assert url == expected_url
