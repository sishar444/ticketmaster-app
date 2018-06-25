# ticketmaster-app

An interactive command-line Python application which processes user search inputs and searches event data from the [Ticketmaster API](https://developer.ticketmaster.com/) to provide details on dates, location, and ticket prices for upcoming events. The application also provides interactive commands to help the user navigate through the data and save to a file if desired.

## Installation

First, "fork" [this upstream repository](https://github.com/sishar444/ticketmaster-app.git) under your own control.

Then download your forked version of this repository using the GitHub.com online interface or the Git command-line interface. If you are using command-line Git, you can download it by "cloning" it:

```sh
git clone https://github.com/YOUR_USERNAME/ticketmaster-app.git
```

After downloading your forked repository, navigate into its root directory:

```sh
cd ticketmaster-app/
```

> NOTE: all commands in this document assume you are running them from this root directory.

Install package dependencies using the following command:

```sh
# Pipenv on Mac or Windows:
pipenv install
```

## Setup

Register for a [Ticketmaster API Key](https://developer-acct.ticketmaster.com/user/register), which the app will supply when issuing requests to the API. The key to use will be named 'Consumer Key'.

To prevent your secret API Key from being tracked in version control, the application looks for an environment variable named `TICKETMASTER_API_KEY`. To set this environment variable, create a new file in this directory called ".env" and place inside the following contents:

    TICKETMASTER_API_KEY="abc123" # use your own API Key instead of "abc123"

To be able to save search results in the app to a file, add an empty folder in this directory named 'data'.

## Usage

If you are using Pipenv, enter a new virtual environment (`pipenv shell`) before running any of the commands below.

Run the application script:

```sh
# Homebrew-installed Python 3.x on Mac OS, not using Pipenv:
python3 app/events_lookup.py

# All others, including Pipenv on Mac or Windows:
python app/events_lookup.py
```

## [License](LICENSE.md)
