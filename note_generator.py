from moviepy.editor import *
import moviepy.video.fx.all as vfx




def clip_to_notes(file_location, export_location, note_range):

    export_location += "\\"
    for i in range(int(note_range)):

        newclip = VideoFileClip(file_location).subclip(0, 2)
        newclip = newclip.fx(vfx.speedx, factor=(1.059463)**i)
        export = CompositeVideoClip([newclip])
        export.write_videofile(export_location + str(i) + ".mp4")
        print(newclip.size)

    ColorClip(newclip.size, (0,0,0), duration=2).write_videofile(export_location +"x.mp4", 25)
