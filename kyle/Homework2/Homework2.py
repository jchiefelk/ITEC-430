import os

list = ["https://www.youtube.com/watch?v=XE4BxPwu4zI", "https://www.youtube.com/watch?v=CTAud5O7Qqk", "https://www.youtube.com/watch?v=bWXazVhlyxQ"]

for x in range (0, len(list)):
	os.system("youtube-dl -x --extract-audio --audio-format mp3 " + list[x])
