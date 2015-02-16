#!/usr/bin/env python3

import pylast
import sqlite3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("database", help="database file to scrape")
args = parser.parse_args()

conn = sqlite3.connect(args.database)

c = conn.cursor()
c.execute("""select * from scrobbles""")

data = []
for row in c:
	data.append({'artist': row[2], 'track': row[3], 'album': row[4], 'tracknr': row[5], 'mbid': row[6], 'duration': row[8], 'whenplayed': row[9]})
c.close()
#print(data)

# scrobbles (_id integer primary key autoincrement, musicapp integer not null, artist text not null, album text not null, track text not null, tracknr text not null, mbid text not null, source text not null, duration integer not null, whenplayed integer not null,rating text not null);

API_KEY = "b25b959554ed76058ac220b7b2e0a026" # This is a sample key!
API_SECRET = "425b55975eed76058ac220b7b4e8a054"

username = "your_user_name"
password_hash = pylast.md5("your_password")

network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = API_SECRET, username = username, password_hash = password_hash)

for line in data:
	network.scrobble(artist = line['artist'], title = line['track'], timestamp = line['whenplayed'], album = line['album'], track_number = line['tracknr'], duration = line['duration'])
