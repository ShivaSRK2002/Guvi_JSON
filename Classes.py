import requests


class countries():

    def __init__(self, url):
        self.url = url

    def get_json_data(self):

        try:
            response = requests.get(self.url, verify=False)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            return None

    def dollar_currency_country(self):
        data = self.get_json_data()
        if data is None:
            return None

        dollar_countries = []

        for i in data:
            if 'currencies' in i:
                for currency, details in i['currencies'].items():
                    if 'dollar' in details['name']:
                        dollar_countries.append(i['name']['common'])
                        break
        return dollar_countries

    def euro_currency_country(self):
        data = self.get_json_data()
        if data is None:
            return None
        euro_countries = []
        for i in data:
            if 'currencies' in i:
                if 'EUR' in i['currencies']:
                    euro_countries.append(i['name']['common'])
        return euro_countries

    def country_name_currency_symbol(self):
        data = self.get_json_data()
        if data is None:
            return None
        countries = []
        currency_details = []
        for i in data:
            if 'name' in i and 'currencies' in i:
                for currency, details in i['currencies'].items():
                    countries.append(i['name']['common'])
                    currency_details.append(details)
        return countries, currency_details


get_data = countries("https://restcountries.com/v3.1/all")

d = get_data.dollar_currency_country()

print("The countries that has dollar as their currency are as follows: ", d)

e = get_data.euro_currency_country()

print("The countries that has euro as their currency are as follows: ", e)

x, y = get_data.country_name_currency_symbol()

data = []

for i in range(0, len(x)):
    country_data = {}
    country_data['country_name'] = x[i]
    country_data['currency'] = y[i]
    data.append(country_data)

print(data)


