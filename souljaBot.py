import requests
import json
import random 
import lyricsgenius
from dhooks import Webhook, Embed


genius = lyricsgenius.Genius("FwCgViQ4qHi6iXS5hVfrA7zNQQZ2baTDvhXOOX_jDWEkY_DhAwwnZzyanjPx13K1")
url = 'https://api.genius.com/artists/1194/songs?per_page=50'
hook = Webhook('https://discord.com/api/webhooks/790388875033706497/MXX23JmFP1coCcQDl4-iV_OhEdd451lZvRLQwtS2C99OcCrG1Cj34m6BotUOEc2ig1LW')

#Soulja ID 1194

headers = {"Authorization": "Bearer FwCgViQ4qHi6iXS5hVfrA7zNQQZ2baTDvhXOOX_jDWEkY_DhAwwnZzyanjPx13K1"}

r = requests.get(url, headers=headers)


data = json.loads(r.text)
songs = songTitle = data['response']['songs']
songTitle = songs[random.randint(0, len(songs))]['title']
songURL = songs[random.randint(0, len(songs))]['url']
song = genius.search_song(songTitle, "Soulja Boy")



embed = Embed(
    description=song.lyrics,
    title=songTitle + " by Soulja Boy",
    )
#embed.set_footer(text='Made by @NicTron#3722')

hook.send(embed=embed)