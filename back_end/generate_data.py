# encoding: utf-8

import csv
import json

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
NO_GUESTS = ['', 'N/A', 'Compilation episode']

links = set()
seasons = []
people = [ALAN]
episodes = []
guests = []


def add_episode(row, current_season):
  episode = {}
  
  episode['season'] = current_season
  episode['name'] = row[EPISODE_NAME][1:-1]
  
  number = row[EPISODE_NUMBER].split()
  episode['e#'] = number[0]
  if len(number) != 1:
    episode['#'] = number[1][1:-1]
    
  episode['eng'] = row[LINK_ENG]
  episode['rus'] = row[LINK_RUS]
  episode['eng_xl'] = row[LINK_ENG_XL]
  episode['rus_xl'] = row[LINK_RUS_XL]

  air_dates = row[AIR_DATE].split('\n')
  episode['air'] = air_dates[0]
  if len(air_dates) != 1:
    episode['air_xl'] = air_dates[1][:-13]
  
  episodes.append(episode)
  
  
def log_guest(row, guest_name):
  guest = {}
  
  guest['show_id'] = len(episodes) - 1
  guest['people_id'] = people.index(guest_name)
  guest['is_winner'] = guest_name in row[WINNER]
  
  guests.append(guest)
  

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
      
      panel = row[GUESTS].split('\n')
      for guest in panel:
        if guest not in NO_GUESTS:
          if guest not in people:
            people.append(guest)
          log_guest(row, guest)
          
      if 'No Alan' not in row[NOTE] and row[GUESTS] not in NO_GUESTS:
        log_guest(row, ALAN)

  print(episodes)