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

def count_and_list_breweries_with_websites(url, states):
    for state in states:
        breweries_data = fetch_breweries_by_state(url, state)

        if breweries_data:
            breweries_with_websites = [brewery for brewery in breweries_data if 'website_url' in brewery]

            print(f"Number of breweries with websites in {state}: {len(breweries_with_websites)}")
            print(f"Breweries with websites in {state}:")

            for brewery in breweries_with_websites:
                name = brewery.get('name', 'N/A')
                website_url = brewery.get('website_url', 'N/A')

                print(f"  - {name}: {website_url}")

            print("\n")
        else:
            print(f"Failed to fetch data for {state}.")

# Example usage
url = "https://api.openbrewerydb.org/breweries"
states_of_interest = ['Alaska', 'Maine', 'New York']
count_and_list_breweries_with_websites(url, states_of_interest)