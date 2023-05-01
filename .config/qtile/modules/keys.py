#Qtile Configuration
#Julen Camps

from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
from os import path

mod = "mod4"
terminal = guess_terminal()
home = path.expanduser('~')


keys = [
    # ------------ Window Navigation ------------

    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
        # Menu
    Key([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    Key([mod], "a",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "d",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
            ),

    Key([mod, "shift"], "m", lazy.spawn("rofi -show")),

    #Media Keys
    #Key([], "XF86AudioRaiseVolume", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +4%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -4%")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    # ------------ App Configs ------------

    # Browser (firefox)
    Key([mod], "b", lazy.spawn("firefox")),
    Key([mod], "t", lazy.spawn("/opt/tor-browser_en-US/Browser/start-tor-browser")),
    # Screenshot (scrot)
    Key([mod], "p", lazy.spawn("scrot /home/julen/images/screenshots/")),
    # File Manager(nemo)
    Key([mod], "f", lazy.spawn("nemo")),
    #Screen Locker(slock)
    Key([mod], "g", lazy.spawn("slock")),
    # Brightness Control
    Key([mod], "o", lazy.spawn("brightnessctl  s +5%")),
    Key([mod], "i", lazy.spawn("brightnessctl  s 5%-")),
    #Shutdown menu
    Key([mod], "k", lazy.spawn("/home/julen/.config/qtile/shutdown.sh")),
]
