#Qtile Configuration
#Julen Camps

from libqtile.config import Group, Key
from libqtile.lazy import lazy 
from modules.keys import keys, mod

#Groups
groups = [Group(i) for i in [ "WWW", "SYS", "DEV", "DOC", "ARC", "MIS"]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
