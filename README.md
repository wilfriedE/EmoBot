# EmoBot
An IRC bot that adds unicode emoji auto correction, based on http://www.emoji-cheat-sheet.com/.

#How it works
	Type ``` Hello Channel :smiley: ``` from your irc client and EmoBot will follow up with
	``` nick means* 😃```

# Adding EmoBot to your channel
	-Invite EmoBot to your channel or
	-Add your channel name as "#channel_name" in the channels.json file on update EmoBot server would join those channels.

#Supported Emojies
	-Primarily unicode emojies: http://apps.timwhitlock.info/emoji/tables/unicode

#Optout
	-You can tell EmoBot not to autocorrect you by saying ```emo-bot optout```
	Note that emo-bot will only keep track of opt-out users as long as it is connected.
	When it disconnects and reconects it will automatically consider all users opted in.

#Optin after Optout
	-When you decide to optout you have options to view about emo-bot or to optin.
	Enter ```emo-bot optin``` from your irc client.

#COntributors
	-All pull request and issues welcome! 😃