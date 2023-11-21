#PRINT ALL THE BREWERIES PRESENT IN ALASKA MAINE NEWYORK
import requests

def fetch_breweries_by_state(url, state):
    try:
        response = requests.get(url, params={'by_state': state})
        response.raise_for_status()
        json_data = response.json()
        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def count_breweries_by_states(url, states):
    for state in states:
        breweries_data = fetch_breweries_by_state(url, state)

        if breweries_data:
            brewery_count = len(breweries_data)
            print(f"Number of breweries in {state}: {brewery_count}")
        else:
            print(f"Failed to fetch data for {state}.")
url = "https://api.openbrewerydb.org/breweries"
states_of_interest = ['Alaska', 'Maine', 'New York']
count_breweries_by_states(url, states_of_interest)