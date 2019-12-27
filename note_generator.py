from moviepy.editor import *
import moviepy.video.fx.all as vfx


file_location = input("give file location:")
export_location = input("give export location:") + "\\"
note_range = input("give note range:")


for i in range(int(note_range)):

    newclip = VideoFileClip(file_location).subclip(0, 2)
    newclip = newclip.fx(vfx.speedx, factor=(1.059463)**i)
    export = CompositeVideoClip([newclip])
    export.write_videofile(export_location + str(i) + ".mp4")
