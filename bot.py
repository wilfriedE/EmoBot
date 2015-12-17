#!/usr/bin/env python
# -*- coding: utf-8 -*-
from defaults import *
from emoji import *
import re
import socket 

def commands(nick,channel,message):
  if containsGreetings(message):
    hello(channel, nick)

  global optout_nicks
  if message.find(botnick+': about')!=-1 or message.find(botnick+' about')!=-1:
    ircsock.send('PRIVMSG %s :%s: I am an Emoji bot that adds emoji auto corrects. Go http://git.io/v05Ik for more info.!\r\n' % (channel,nick))
  elif message.find(botnick+': optout')!=-1 or message.find(botnick+' optout')!=-1:
    if nick not in optout_nicks:
      optout_nicks += [nick]
    ircsock.send('PRIVMSG %s :%s: You have been opted out %s. Note when emo-bot disconnects you will be opted back in by default. More at [gir-url].\r\n' % (channel,nick, Emo.get(":cry:")))
  elif message.find(botnick+': optin')!=-1 or message.find(botnick+' optin')!=-1:
    ircsock.send('PRIVMSG %s :%s: You are already been opted in %s .\r\n' % (channel,nick, Emo.get(":guitar:")))
  elif message.find(botnick+': help')!=-1 or message.find(botnick+' help')!=-1:
    ircsock.send('PRIVMSG %s :%s: Available commands [about, optout,].\r\n' % (channel,nick))

def opted_out_commads(nick, channel, message):
  """
    commands Available for opted out users.
  """
  global optout_nicks
  if message.find(botnick+': optin')!=-1 or message.find(botnick+' optin')!=-1:
    if nick in optout_nicks:
      optout_nicks.remove(nick)
    ircsock.send('PRIVMSG %s :%s: You have been opted in %s .\r\n' % (channel,nick, Emo.get(":guitar:")))
  elif message.find(botnick+': help')!=-1 or message.find(botnick+' help')!=-1:
    ircsock.send('PRIVMSG %s :%s: Available commands [about, optin].\r\n' % (channel,nick))

def containsGreetings(msg):
  message = msg.lower()
  if (message.find("hello "+ botnick) != -1 or
    message.find("hi "+ botnick) != -1 or
    message.find("hey "+ botnick) != -1 or
    message.find(botnick+': hello')!=-1 or
    message.find(botnick+': hi')!=-1 or
    message.find(botnick+': hey')!=-1 or
    message.find(botnick+' hello')!=-1 or
    message.find(botnick+' hi')!=-1 or
    message.find(botnick+' hey')!=-1
    ):
    return True
  else:
    False

# Some basic variables used to configure the bot
def ping():
  """respond to server Pings."""
  ircsock.send("PONG :pingis\n")  

def sendmsg(chan , msg): 
  """simply sends messages to the channel."""
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): # This function is used to join channels.
  ircsock.send("JOIN "+ chan +"\n")

def hello(chan, nick):
  ircsock.send("PRIVMSG "+ chan +" :Hello! " + nick + " " + Emo.get(":smiley:") +" \n")

def getNick(msg):
  return msg.split('!')[0][1:]

def getChannel(msg):
  return msg.split(' PRIVMSG ')[-1].split(' :')[0]

def joinInvite(msg):
  channel = msg.split("INVITE " + botnick)[-1].split(':')[-1]
  joinchan(channel)
  sendmsg(channel , "Hello! "+ channel + " . emo-bot is here type 'emo-bot help' for more.")

def run():
  ircsock.connect((server, 6667)) # Here we connect to the server using the port 6667
  ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Emojie Bot to ligthen up your day 😄. More at http://git.io/v05Ik.\n") # user authentication
  ircsock.send("NICK "+ botnick +"\n") # here we actually assign the nick to the bot

  for channel in channels:
    joinchan(channel)

  while 1:
    ircmsg = ircsock.recv(2048) # receive data from the server
    ircmsg = ircmsg.strip('\n\r') # removing any unnecessary linebreaks.
    print(ircmsg) # Here we print what's coming from the server
    channel = getChannel(ircmsg)
    nick = getNick(ircmsg)

    if nick not in optout_nicks:
      emojies = re.findall(r':([\w+-]+):', ircmsg)
      emojies = [ Emo.get(":"+emoji+":") for emoji in emojies if Emo.valid(":"+emoji+":")]
      if emojies:
        ircsock.send('PRIVMSG %s :%s: means* ' % (channel,nick) + ' '.join([ emoji for emoji in emojies]) +' \r\n')
      commands(nick,channel,ircmsg)
    else:
      opted_out_commads(nick,channel,ircmsg)

    if ircmsg.find("INVITE " + botnick)!=-1: #when invited to channel join channel
      joinInvite(ircmsg)

    if ircmsg.find("PING :") != -1: # if the server pings us then we've got to respond!
      ping()

def test():
  print("beginning tests\n")
  ircmsg = ':botiE!~botiE@unaffiliated/botiE PRIVMSG #theChannel :Hello emo-bot'
  print("nick => botiE : ", getNick(ircmsg) == "botiE")
  print("channel => theChannel : ", getChannel(ircmsg) == "#theChannel")
  print("tests have completed.\n\n")

if __name__ == '__main__':
  Emo = Emoji()
  optout_nicks = []
  test()
  ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  run()
