"""
Tests for EmoBot and it's components
"""

from emoji import *

Emoticons = Emoji()

def test_emojies():
	print(":smiley: => ", Emoticons.get(":smiley:"))
	print(":raised_hands: => ", Emoticons.get(":raised_hands:"))
	print(":heart_eyes_cat: => ", Emoticons.get(":heart_eyes_cat:"))
	print(":innocent: => ", Emoticons.get(":innocent:"))
	print(":punch: => ", Emoticons.get(":punch:"))
	print(":muscle: => ", Emoticons.get(":muscle:"))
	print(":pray: => ", Emoticons.get(":pray:"))
	print(":spy: => ", Emoticons.get(":spy:"))
	print(":alien: => ", Emoticons.get(":alien:"))
	print(":globe_with_meridians: => ", Emoticons.get(":globe_with_meridians:"))
	print(":rocket: => ", Emoticons.get(":rocket:"))
	print(":100: => ", Emoticons.get(":100:"))

if __name__ == '__main__':
	test_emojies()