# TF2-Console-Parser

Team Fortress 2 is an online multiplayer FPS, released by Valve Software in 2007 as part of the Orange Box. It utilizes the Source engine, an in-house engine developed by Valve. The console, which is easily accessible, can and is often used to execute commands and log information about the game. This includes, but is not limited to, errors and chat logs made by other players.

If -condebug is used in TF2's launch options on Steam, the full contents of this console log is written to a file in a user's TF2 directory.

### The Question

The TF2 community takes advantage of this ease of modding the game, allowing a flourishing community of modifications to the game. However, this means that a user with lots of mods may experience more errors and garbage in their console compared to a standard user.

My main interest in this short project is how I could potentially use the logs that I have inadvertently stored over the years to extract **chat messages.**

### What This Repo Contains

This repo contains the Python file ConsoleParser.py, which contains the methods necessary for parsing TF2 console logs.

None of the functions check for correct datatypes -- this is a personal project, and so it is assumed the inputs are carefully crafted manually.

- filename should be in filename.txt or filename.log format.
- steamid should be in STEAM_x:​x:xxxxxxxx format.
- text is a phrase in String format.
- name is a name in String format.
- chat is a formatted list from parse_console(filename). 

A short description of functions is provided.

- parse_console(filename)
	- This function returns a list of chat messages, as well as SteamID connected messages.
- instances_of_name(steamid)
	- This method is a helper function which parses a cleaned log and extracts aliases from SteamID connected messages.
- from_contains(name, text, chat, steamid=None)
	- This function restricts searches to a certain phrase from someone specific. If SteamID is provided, it will try to get messages from any recorded names.
- contains(text, chat):
	- This function restricts searches to a certain phrase.
- from_user(name, chat, steamid=None)
	- This function restricts searches to a certain person. If SteamID is provided, it will try to get messages from any recorded names.
	
Included is also some sample logs that one could use.

## WARNING: OFFENSIVE DATA

Because TF2 is an online community with little restrictions on the content being sent, the console logs provided may include derogatory, uncomfortable, or problematic messaging. **In no way does my inclusion of these logs suggest an endorsement of the content.** This is simply used as an interesting coding problem.

#### Other Information

The longest file included in this repo is approximately 228,000 lines. The unabridged console log is close to 5.5 million lines. This is ~350 mB in size, and so could not be included in Github.<br>
The communities being frequented during this time period included in the log (mid 2020) is The Brew Crew, a Versus Saxton Hale community which is now defunct. Therefore, there may be a concentration of specific terms that may not be representative of the overall TF2 community.<br>
The efficiency of this code is quite slow, especially when dealing with the full console log initially. In my full log, <10% of the lines in the file are actually chat messages. This means over 90% of the lines are garbage error lines.