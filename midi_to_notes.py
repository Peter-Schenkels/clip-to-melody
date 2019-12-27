import mido
from note import note

def midi_to_notes(fileLocation):
    song = []
    mid = mido.MidiFile(fileLocation)

    currLow = 1000
    for event in mid:

        message = str(event)
        type = message.split()[0]
        if type == "note_on" or type == "note_off":

            music_note = message.split()[2].replace("note=", "")


            length = message.split()[4].replace("time=", "")
            if type == "note_off":
                song.append(note('x', length))
            else:
                song.append(note(music_note, length))
                if int(music_note) < currLow:
                    currLow = int(music_note)

    for musicn in song:
        if musicn.name != 'x':
            musicn.name = str(int(musicn.name) - currLow)

    return song