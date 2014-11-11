def clip_ph(area):
    """ Sends filename path to clipboard. """
    area.clipboard_clear()
    area.clipboard_append(area.filename)

INSTALL = [(2, '<Key-u>', lambda event: clip_ph(event.widget))]

def install(area):
    area.install(*INSTALL)







