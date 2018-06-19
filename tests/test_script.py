# ticketmaster-app/tests/test_script.py

from app.events_lookup import format_date_string

def test_format_date_string():
    test_date = "2018-09-22"
    expected_result = "September 22, 2018"
    result = format_date_string(test_date)
    assert result == expected_result
