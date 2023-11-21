#USING OOPS CONCEPT CLASS CONSTRUCTOR FOR TAKING DATA FROM THE MENTIONED URL IN THE TASK

import requests
class json:
    def __init__(self,url):
        self.url=url
    def fetch_countries_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        # Assuming the response contains JSON data
            json_data = response.json()
            return json_data
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None
# Example usage
#url = "https://restcountries.com/v3.1/all"
#countries_data = fetch_countries_data(url)
j=json("https://restcountries.com/v3.1/all")
countries_data=j.fetch_countries_data()
if countries_data:
    print(countries_data)
else:
    print("Failed to fetch data.")