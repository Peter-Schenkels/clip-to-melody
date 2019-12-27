from moviepy.editor import *
from copy import deepcopy
from note import note


song = [note('0', 0.2),
        note('2', 0.2),
        note('6', 0.2),
        note('9', 0.2),
        note('6', 0.2),
        note('2', 0.2),
        note('0', 0.2)]

clips = []
videoName = input("Video name:") + ".webm"
file_directory = "D:\dev\\note video generator\\notes\\"

for note in song:

    fileName = file_directory + note.name + ".mp4"

    print(fileName)
    tmpClip = VideoFileClip(fileName).subclip(0, note.length)
    clips.append(tmpClip)


video = concatenate_videoclips(clips)
video.write_videofile(videoName, fps=25)



