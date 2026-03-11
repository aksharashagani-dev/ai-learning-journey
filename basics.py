# My favourite songs
songs = ["Song 1", "Song 2", "Song 3", "Song 4", "Song 5"]

for song in songs:
    print("🎵 " + song)
mood = input("What's your mood right now? ")

# Check the mood and recommend a song
if mood == "happy":
    print("🎵 Play: Happy by Pharrell Williams")
elif mood == "sad":
    print("🎵 Play: Someone Like You by Adele")
elif mood == "focused":
    print("🎵 Play: Lo-fi beats playlist")
elif mood == "hype":
    print("🎵 Play: HUMBLE by Kendrick Lamar")
else:
    # If mood doesn't match anything, play this
    print("🎵 Play: Blinding Lights — works for everything!")
# Program 3 - Now playing function
# This function takes a song name and returns a formatted string

def now_playing(song):
    # Format the song name into a "now playing" message
    return "🎵 Now playing: " + song

# Test the function with a few songs
print(now_playing("Blinding Lights"))
print(now_playing("HUMBLE"))
print(now_playing("Levitating"))

