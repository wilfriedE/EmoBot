#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
A simple script to mapp the emojies in emoji.json
	It makes retrieval of emojies simpler.
"""

import json
with open('emoji/emoji.json') as emoji_file:
	emojies = json.load(emoji_file)

EmojiMap = {}

for emoji in emojies:
	if "emoji" in emoji:
		for alias in emoji["aliases"]:
			alias = alias.strip() #just in case it is not fully stripped by defualt
			EmojiMap[":"+alias+":"] = emoji["emoji"].encode("utf-8")
		for tag in emoji["tags"]:
			tag = tag.strip()
			EmojiMap[":"+tag+":"] = emoji["emoji"].encode("utf-8")

if __name__ == '__main__':
	print(EmojiMap)
	print("\nwritting to file\n")
	with open('emoji/emoji_map.json', 'w') as f:
		print("...")
		json.dump(EmojiMap, f)
	print("\nfinished writting.")