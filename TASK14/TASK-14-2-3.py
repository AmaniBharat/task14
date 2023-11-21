#TYPES OF BREWERIES PRESENT IN THE INDIVIDUAL STATE AS MENTIONED
import requests

def fetch_breweries_by_state(url, state):
    try:
        response = requests.get(url, params={'by_state': state})
        response.raise_for_status()

        # Assuming the response contains JSON data
        json_data = response.json()

        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def count_brewery_types_by_cities(url, state):
    breweries_data = fetch_breweries_by_state(url, state)

    if breweries_data:
        cities_data = {}
        
        for brewery in breweries_data:
            city = brewery.get('city', 'N/A')
            brewery_type = brewery.get('brewery_type', 'N/A')

            if city not in cities_data:
                cities_data[city] = set()

            cities_data[city].add(brewery_type)

        for city, brewery_types in cities_data.items():
            print(f"City: {city}")
            print(f"Number of Brewery Types: {len(brewery_types)}")
            print(f"Brewery Types: {', '.join(brewery_types)}")
            print("\n")
    else:
        print(f"Failed to fetch data for {state}.")
url = "https://api.openbrewerydb.org/breweries"
states_of_interest = ['Alaska', 'Maine', 'New York']

for state in states_of_interest:
    count_brewery_types_by_cities(url, state)