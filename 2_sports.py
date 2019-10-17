import requests

response = requests.get('https://footballapi.pulselive.com/football/players?pageSize=30&compSeasons=274&altIds=true&page=0&type=player&id=-1&compSeasonId=274')
resp_obj = response.json()
print(resp_obj)
