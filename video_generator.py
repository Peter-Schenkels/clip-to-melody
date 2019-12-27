from moviepy.editor import *
from copy import deepcopy
from note import note

def clips_to_song(song, file_directory):
    clips = []
    videoName = input("export name:") + ".mp4"
    file_directory += "\\"
    for note in song:
        fileName = file_directory + note.name + ".mp4"
        tmpClip = VideoFileClip(fileName).subclip(0,float(note.length))
        clips.append(tmpClip)


    video = concatenate_videoclips(clips)
    video.write_videofile(videoName, fps=25)



