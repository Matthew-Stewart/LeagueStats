from riotwatcher import RiotWatcher, LoLException, error_404, error_429
from riotInfo import riot_api_key
import quickstart
from pprint import pprint

w = RiotWatcher(riot_api_key)

# check if we have API calls remaining
print(w.can_make_request())

me = w.get_summoner(name='StewartTheMouse')
print(me)

try:
    response = w.get_summoner('voyboy')
except LoLException as e:
    if e == error_429:
        print('We should retry in {} seconds.'.format(e.headers['Retry-After']))
    elif e == error_404:
        print('Summoner not found.')


match = '2364201286'

m = w.get_match(match)

pprint(m)

columns = [chr(i) for i in range(ord('B'),ord('K')+1)]
names = ['Kills', 'Deaths', 'Assists', 'Damage', 'Wards Placed', 'Wards Killed', 'CS', 'Gold', 'Time', 'Total Kills']

col_map = dict(zip(names, columns))

print(col_map)

print('asdf')

#quickstart.get_data("Team Dat Ashe", "B2:E")


def get_kills(uid):
   print('hello')


