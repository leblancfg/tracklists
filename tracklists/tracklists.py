import pyperclip
import os

def tracklist(data):
    """Given a list of tracks with their duration,
    returns the same list, but with cumulative times
    so that they be skipped-to in YouTube. The last
    item of each line must represent the duration.
    Ex:
    1 Black Cow 5:07         1 Black Cow 0:00
    2 Aja 7:56           ->  2 Aja 5:07
    3 Deacon Blues 7:26      3 Deacon Blues 13:03
    str -> str."""
    # TODO: Better string 'sanitizing'.
    data = data.strip()
    timer = 0
    tracklist = []
    tracks = [t for t in data.split('\n')]
    for track in tracks:
        # Change the last word to the current duration
        mins, secs = divmod(timer, 60)
        words = track.split()
        details = ' '.join(words[0:-1])
        fixed_track = details + ' ' + str(mins) + ':' + str(secs).zfill(2)
        tracklist.append(fixed_track)

        # Split the last word into minutes and seconds
        # and update timer
        track_m, track_s = words[-1].split(':') 
        timer += int(track_m) * 60 + int(track_s)
    return '\n'.join(tracklist)

def main():
    # TODO: add CLI argument handling for files.
    try:
        data = pyperclip.paste()
        return tracklist(data)
    except:
        exit('Clipboard input unparseable.')

if __name__ == '__main__':
    main()
