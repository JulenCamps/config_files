#Qtile Configuration
#Julen Camps

from typing import List  # noqa: F401

import os
from libqtile import qtile
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen, Match
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from os import path
import subprocess

@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(path.expanduser('~'), '.config', 'qtile', 'autostart.sh')])

mod = "mod4"
terminal = guess_terminal()
home = path.expanduser('~')

def shutdown_menu():
    qtile.cmd_spawn(home + "/.config/qtile/shutdown.sh")

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


#Groups

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons: 
#nf-mdi-firefox
#nf-dev-python
#nf-fa-file_text
#nf-dev-terminal
#nf-mdi-folder
#nf-seti-config

groups = [Group(i) for i in [ "WWW", "SYS", "DEV", "DOC", "ARC", "MIS"]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])


# Layouts and layout rules

layout_conf = {
    'border_focus': '#a151d3',
    'border_width': 2,
    'margin': 5, 
}       

layouts = [
    layout.MonadTall(**layout_conf),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    #layout.Bsp(),
    # layout.Columns(),
    #layout.Matrix(**layout_conf),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    #layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='UbuntuMono Nerd Font',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.TextBox(
                    text="",
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#0f101a", "#0f101a"],
                    fontsize=20,
                    padding= 15,
                    mouse_callbacks={"Button1" : lambda: qtile.cmd_spawn('rofi -show drun')},
                ),
                widget.GroupBox(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#0f101a", "#0f101a"],
                    font='Ubuntu Bold',
                    fontsize=9,
                    margin_y=6,
                    margin_x=3,
                    padding_y=8,
                    padding_x=6,
                    borderwidth=3,
                    active=["#f1ffff", "#f1ffff"],
                    inactive=["#f1ffff", "#f1ffff"],
                    rounded=False,
                    highlight_method='line',
                    this_current_screen_border=["#a151d3", "#a151d3"],
                    this_screen_border=["#353c4a", "#353c4a"],
                    other_current_screen_border=["#0f101a", "#0f101a"],
                    other_screen_border=["#0f101a", "#0f101a"]
                ),
                widget.WindowName(
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0f101a", "#0f101a"],
                    fontsize=16
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                    text="卑",
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0f101a", "#0f101a"],
                    fontsize = 50,
                    padding= -3
                ), 
                widget.TextBox(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                    text='  ' # Icon: nf-fa-feed
                ),
                widget.Net(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                    format='{down} ↓↑ {up}'
                    # To run this widget you need to install psutil frop pip library         
                ),
                widget.Sep(
                    linewidth=0, padding=5,
                    background=["#a151d3", "#a151d3"]
                ),
                widget.TextBox(
                    text="卑",
                    foreground=["#0174DF", "#0174DF"],
                    background=["#a151d3", "#a151d3"],
                    fontsize = 50,
                    padding= -3
                ),
                widget.TextBox(
                    text="",
                    foreground=["#0f101a", "#0f101a"],
                    background=["#0174DF", "#0174DF"],
                    padding=8
                ),
                widget.Backlight(
                    backlight_name='amdgpu_bl0',
                    foreground=["#0f101a", "#0f101a"],
                    background=["#0174DF", "#0174DF"],
                ),
                widget.Sep(
                    linewidth=0, padding=5,
                    background=["#0174DF", "#0174DF"]
                ),
                widget.TextBox(
                    text="卑",
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0174DF", "#0174DF"],
                    fontsize = 50,
                    padding= -3
                ),
                widget.TextBox(
                    text="",
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                ),
                widget.ThermalSensor(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                    threshold = 85,
                    padding = 5
                    ),
                widget.Sep(
                    linewidth=0, padding=5,
                    background=["#a151d3", "#a151d3"]
                ),   
                widget.TextBox(
                    text="卑",
                    foreground=["#0174DF", "#0174DF"],
                    background=["#a151d3", "#a151d3"],
                    fontsize = 50,
                    padding= -3
                ),
                widget.CurrentLayoutIcon(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#0174DF", "#0174DF"],
                    scale=0.65
                ),
                widget.CurrentLayout(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#0174DF", "#0174DF"]
                ),
                widget.Sep(
                    linewidth=0, padding=5,
                    background=["#0174DF", "#0174DF"]
                ),
                widget.TextBox(
                    text="卑",
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0174DF", "#0174DF"],
                    fontsize = 50,
                    padding= -3, 
                ),
                widget.TextBox(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                    text='  ' # Icon: nf-mdi-calendar_clock
                ),
                widget.Clock(
                    format='%d/%m/%Y - %H:%M',
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                ),
                widget.Sep(
                    linewidth=0, padding=5,
                    background=["#a151d3", "#a151d3"]
                ),
                widget.TextBox(
                    text="卑",
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                    fontsize = 50,
                    padding= -3,

                ),    
                widget.Systray(
                    background=["#0f101a", "#0f101a"]
                    # Battery icon: install cbatticon from yay and add it to xsession
                    # Volumeicon: install volumeicon and add it to xsession
                    # Network Manager: install network-manager-applet and add nm-applet to .xsession
                    # Udiskie: install udiskie ntfs-3g and add udiskie to .xsession
                ),
                widget.Sep(
                    linewidth=0, padding=5,
                    background=["#0f101a", "#0f101a"]
                ),
                widget.TextBox(
                    text='⏻',
                    mouse_callbacks = {'Button1' : shutdown_menu},
                    padding=5,
                    foreground=['#8aaefc'],
                    background=["#0f101a", "#0f101a"],
                ),
                widget.Sep(
                    linewidth=0, padding=15,
                    background=["#0f101a", "#0f101a"]
                ),
            ],
            30,
            margin=[0, 0, 0, 0],
            opacity=0.9
        ),
    ),
    Screen(
        top=bar.Bar(
            [
                 widget.TextBox(
                    text="",
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#0f101a", "#0f101a"],
                    fontsize=20,
                    padding= 15,
                ),
                widget.GroupBox(
                    foreground=["#f1ffff", "#f1ffff"],
                    background=["#0f101a", "#0f101a"],
                    font='Ubuntu Bold',
                    fontsize=9,
                    margin_y=6,
                    margin_x=3,
                    padding_y=8,
                    padding_x=6,
                    borderwidth=3,
                    active=["#f1ffff", "#f1ffff"],
                    inactive=["#f1ffff", "#f1ffff"],
                    rounded=False,
                    highlight_method='line',
                    this_current_screen_border=["#a151d3", "#a151d3"],
                    this_screen_border=["#353c4a", "#353c4a"],
                    other_current_screen_border=["#0f101a", "#0f101a"],
                    other_screen_border=["#0f101a", "#0f101a"]
                ),
                widget.WindowName(
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0f101a", "#0f101a"],
                    fontsize=16
                ),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(
                    text="卑",
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0f101a", "#0f101a"],
                    fontsize = 50,
                    padding= -3
                ), 
                widget.TextBox(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                    text='  ' # Icon: nf-fa-feed
                ),
                widget.Net(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                    format='{down} ↓↑ {up}'
                    # To run this widget you need to install psutil frop pip library         
                ),
                widget.Sep(
                    linewidth=0, padding=5,
                    background=["#a151d3", "#a151d3"]
                ),
                widget.TextBox(
                    text="卑",
                    foreground=["#0174DF", "#0174DF"],
                    background=["#a151d3", "#a151d3"],
                    fontsize = 50,
                    padding= -3
                ),
                widget.TextBox(
                    text="",
                    foreground=["#0f101a", "#0f101a"],
                    background=["#0174DF", "#0174DF"],
                    padding=8
                ),
                widget.Backlight(
                    backlight_name='amdgpu_bl0',
                    foreground=["#0f101a", "#0f101a"],
                    background=["#0174DF", "#0174DF"],
                ),
                widget.Sep(
                    linewidth=0, padding=5,
                    background=["#0174DF", "#0174DF"]
                ),
                widget.TextBox(
                    text="卑",
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0174DF", "#0174DF"],
                    fontsize = 50,
                    padding= -3
                ),
                widget.TextBox(
                    text="",
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                ),
                widget.ThermalSensor(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                    threshold = 85,
                    padding = 5
                    ),
                widget.Sep(
                    linewidth=0, padding=5,
                    background=["#a151d3", "#a151d3"]
                ),   
                widget.TextBox(
                    text="卑",
                    foreground=["#0174DF", "#0174DF"],
                    background=["#a151d3", "#a151d3"],
                    fontsize = 50,
                    padding= -3
                ),
                widget.CurrentLayoutIcon(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#0174DF", "#0174DF"],
                    scale=0.65
                ),
                widget.CurrentLayout(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#0174DF", "#0174DF"]
                ),
                widget.Sep(
                    linewidth=0, padding=5,
                    background=["#0174DF", "#0174DF"]
                ),
                widget.TextBox(
                    text="卑",
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0174DF", "#0174DF"],
                    fontsize = 50,
                    padding= -3, 
                ),
                widget.TextBox(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                    text='  ' # Icon: nf-mdi-calendar_clock
                ),
                widget.Clock(
                    format='%d/%m/%Y - %H:%M',
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                ),
                widget.Sep(
                    linewidth=0, padding=8,
                    background=["#a151d3", "#a151d3"]
                ),
            ],
            30,
            margin=[0, 0, 0, 0],
            opacity=0.9
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

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
