"""

"""

TAG_LINK      = '_link_'
REG_LINK      = 'https?\:\/\/[^ ]+'

def hlink(area):
    """
    It highlighes links.
    
    """

    seq = area.find(REG_LINK, '1.0', 'end')

    for (_, pos0, pos1) in seq:
        area.tag_add(TAG_LINK, pos0, pos1)


INSTALL = [(-1, '<<LoadData>>', lambda event: hlink(event.widget))]

def install(area, setup={'background':'yellow', 'foreground':'blue'}):
    area.tag_config(TAG_LINK, **setup)
    area.install(*INSTALL)





