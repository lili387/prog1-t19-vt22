import discord
import os
import urllib
import json
 
client = discord.Client()
 
@client.event
async def on_ready():
   print(' {0.user} has arrived...'.format(client))
   
def todo(message):
   todoSearch = message.content.split(' ')
   if len(todoSearch) < 2: 
      return 'need number!!!'

   else:
      number = todoSearch[-1]
      todoUrl = 'https://jsonplaceholder.typicode.com/todos/' + number
      todoRaw = urllib.request.urlopen(todoUrl)
      todoJson = json.loads(todoRaw.read())
      return todoJson

def sl(message):
   stationSearch = message.content.split(' ')
   if len(stationSearch) < 2:
      return 'need station!!!'

   else: 
      s = ''
      for i in range (1,len(stationSearch)-1):
         s = s + stationSearch[i] + '+'
      s = s + stationSearch[-1]
       
      stationUrl = 'https://api.sl.se/api2/typeahead.json?key=4c123e93d7f147039fac4c15e0356257&searchstring=' + s
      stationRaw = urllib.request.urlopen(stationUrl)
      stationJson = json.loads(stationRaw.read())
      stationID = stationJson['ResponseData'][0]['SiteId']

      departureUrl = 'https://api.sl.se/api2/realtimedeparturesV4.json?key=10a7d32e89ec413994ee70661fa72a91&siteid=' + stationID + '&timewindow=60'
      departureRaw = urllib.request.urlopen(departureUrl)
      departureJson = json.loads(departureRaw.read())
		 
      departureDestination = departureJson['ResponseData']['Metros'][0]['Destination']
      departureTime = departureJson['ResponseData']['Metros'][0]['ExpectedDateTime'][11:]
      departureName = departureJson['ResponseData']['Metros'][0]['StopAreaName']
      responseString = 'next metro from ' + departureName + ' departs at ' + departureTime + ' towards ' + departureDestination
      return responseString

@client.event
async def on_message(message):
   if message.author == client.user:
      return
 
   if message.content.startswith('::'):
      await message.channel.send('*goblin noises* \n')
      if 'help' in message.content:
         await message.channel.send('::help displays this message \n'
                                    '::goblin tells goblin lore \n'
                                    '::todo <number> shows dumb API test shit'
                                    '::SL <station> helps your journey \n')
      if message.content == '::goblin':
         await message.channel.send('i am goblin')
         
      if message.content.startswith('::todo'):
         response = todo(message)
         await message.channel.send(response)

      
      if message.content.startswith('::SL '):
         response = sl(message)
         await message.channel.send(response)

helpFile = open("readme.txt", "r")
token = helpFile.readline()      
client.run(token)