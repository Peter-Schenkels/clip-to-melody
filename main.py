from midi_to_notes import midi_to_notes
from note import note
from note_generator import clip_to_notes
from video_generator import clips_to_song



#turn clip into music notes
clip_file_location = input("give clip file location:")
export_location = input("give clips export location:")
note_range = input("give note range:")
clip_to_notes(clip_file_location, export_location, note_range)

#turn midi into song
midi_file_location = input("give midi file location:")
song = midi_to_notes(midi_file_location)

#turn song into video clip
clips_to_song(song,export_location)