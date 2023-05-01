#Qtile Configuration
#Julen Camps

from typing import List  # noqa: F401

import os
from libqtile import qtile
from libqtile import layout, hook
from libqtile.config import Match
from libqtile.lazy import lazy

from os import path
import subprocess

from modules.keys import keys, mod
from modules.groups import groups
from modules.layouts import layout_conf, layouts
from modules.widgets import widget_defaults, extension_defaults, screens, mouse

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(path.expanduser('~'), '.config', 'qtile', 'autostart.sh')])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
