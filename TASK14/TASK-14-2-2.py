#LIST OF THE BREWERIES PRESENT IN THE ALASKA ,MAINE,NEWYORK
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

def list_brewery_names_by_states(url, states):
    for state in states:
        print(f"Breweries in {state}:")
        breweries_data = fetch_breweries_by_state(url, state)

        if breweries_data:
            for brewery in breweries_data:
                brewery_name = brewery.get('name', 'N/A')
                print(f"-{brewery_name}")
        else:
            print("Failed to fetch data.")

        print("\n")
url = "https://api.openbrewerydb.org/breweries"
states_of_interest = ['Alaska', 'Maine', 'New York']
list_brewery_names_by_states(url, states_of_interest)