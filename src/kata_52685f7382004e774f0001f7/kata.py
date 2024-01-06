

def make_readable(seconds):

    s = seconds % 60
    m = (seconds // 60) % 60
    h = seconds // (60*60)
    return f'{h:02}:{m:02}:{s:02}'
