"""
  Default configurations
"""
import os
import json

server = "irc.freenode.net"
botnick = "emo-bot"
src_dir = os.path.dirname(__file__)
with open(os.path.join(src_dir, 'channels.json')) as channels_file:
	channels =	json.load(channels_file)