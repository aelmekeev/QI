# encoding: utf-8

import csv
import json
from datetime import datetime

EPISODE_NUMBER = 0
EPISODE_NAME = 1
GUESTS = 2
WINNER = 3
AIR_DATE = 4
NOTE = 5
LINK_ENG = 6
LINK_RUS = 7
LINK_ENG_XL = 8
LINK_RUS_XL = 9

ALAN = 'Alan Davies'
STEPHEN = 'Stephen Fry'
THE_AUDIENCE = 'The Audience'
NO_GUESTS = ['', 'N/A', 'Compilation episode']

links = set()
seasons = []
people = [{'name': STEPHEN, 'shows': [], 'winner': []}, {'name': ALAN, 'shows': [], 'winner': []}]
episodes = []


def format_date(date_string):
  if ' ' in date_string:
    date = datetime.strptime(date_string, '%d %B %Y')
    return datetime.strftime(date, '%d/%m/%Y')
  else:
    return date_string

def get_link(link):
  if 'album-' in link and 'video-' in link:
    return link[44:]
  else:
    return link


def add_episode(row, current_season):
  episode = {}
  
  episode['season'] = current_season
  episode['name'] = row[EPISODE_NAME][1:-1]
  
  number = row[EPISODE_NUMBER].split()
  episode['episode'] = number[0]
  if len(number) != 1:
    episode['episode_total'] = number[1][1:-1]
  
  if row[LINK_ENG] != '': episode['eng'] = get_link(row[LINK_ENG])
  if row[LINK_RUS] != '': episode['rus'] = get_link(row[LINK_RUS])
  if row[LINK_ENG_XL] != '': episode['eng_xl'] = get_link(row[LINK_ENG_XL])
  if row[LINK_RUS_XL] != '': episode['rus_xl'] = get_link(row[LINK_RUS_XL])
  if row[NOTE] != '': episode['note'] = row[NOTE]

  air_dates = row[AIR_DATE].split('\n')
  for date in air_dates:
    if 'XL edit' in date:
      episode['air_xl'] = format_date(date[:-13])
    else:
      episode['air'] = format_date(date)
  
  episodes.append(episode)

  
def log_guest(row, guest_name, episode_id):
  new_guest = False
  guest = next((x for x in people if x['name'] == guest_name), None)
  if guest is None:
    new_guest = True
    guest = {'name': guest_name, 'shows': [], 'winner': []}
  guest['shows'].append(episode_id)
  if guest_name in row[WINNER]:
    guest['winner'].append(episode_id)
  if new_guest:
    people.append(guest)
  

def verify_winners():
  shows_with_winners = set()
  all_shows_ids = set(range(0, len(episodes) -1 ))
        
  for participant in people:
    for win in participant['winner']:
      shows_with_winners.add(win)

  print('The following shows will not be marked as "winner" for any guest:', '\n')
  for show in all_shows_ids.difference(shows_with_winners):
    episode = episodes[show]
    print(seasons[episode['season']], episode['episode'], '-', episode['name'])
  

with open('../data/data.csv', encoding='utf-8', mode='r') as input, open('../data/data.js', encoding='utf-8', mode='w') as output:
  # open csv files
  input = csv.reader(input, delimiter=',')
  
  current_season = -1;
  
  for row in input:
    # verify correctness of links in the document
    for i in range(LINK_ENG, LINK_RUS_XL):
      if row[i] != '' and row[i] in links:
        print(row[i])
      links.add(row[i])
      
    if row[GUESTS] == '':
      seasons.append(row[EPISODE_NUMBER])
      current_season += 1
    else:
      add_episode(row, current_season)
      episode_id = len(episodes) - 1
      
      panel = row[GUESTS].split('\n')
      for guest_name in panel:
        if guest_name not in NO_GUESTS:
          log_guest(row, guest_name, episode_id)
            
      log_guest(row, STEPHEN, episode_id)
      log_guest(row, THE_AUDIENCE, episode_id)
      if 'No Alan' not in row[NOTE]:
        log_guest(row, ALAN, episode_id)

  verify_winners()

  output.write('var seasons=')
  output.write(json.dumps(seasons))
  output.write(';')
  
  output.write('var shows=')
  output.write(json.dumps(episodes))
  output.write(';')
  
  output.write('var guests=')
  output.write(json.dumps(sorted(people, key=lambda x: x['name'])))
  output.write(';')