import os

list = [“https://youtu.be/g3nR_4F1anI”,
	“https://youtu.be/R8UUclE_9V8”,
	“https://youtu.be/ffzUBzrW9HA”,
	“https://youtu.be/KM1RpI2S97o”,
	“https://youtu.be/351s97eOsQ8”]

for i in range (0, len(list)):
	os.system(“youtube-dl -x --extract-audio --audio-format-mp3 “ list[i])

