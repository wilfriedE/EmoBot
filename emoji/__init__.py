"""
 This is a simple Emoji class to allow access to all emojies
"""
import os
import json

class Emoji(object):
	"""Emoji
	A class that allows easy accessibility of emojies.
	"""
	def __init__(self):
		src_dir = os.path.dirname(__file__)
		with open(os.path.join(src_dir, 'emoji_map.json')) as emoji_map_file:
			self.emojies =	json.load(emoji_map_file)

	def get(self, emoji):
		"""
		returns an emojie based on mapping
		"""
		if emoji in self.emojies:
			return self.emojies[emoji].encode('utf-8')

	def valid(self, emoji):
		"""
		returns True or False based on wether or not the emojie exists
		"""
		if emoji in self.emojies:
			return True
		else:
			return False

