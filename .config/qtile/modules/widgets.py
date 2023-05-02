#Qtile Configuration
#Julen Camps

from libqtile import qtile, layout, bar, widget
from libqtile.config import Click, Drag, Screen
from libqtile.lazy import lazy

from modules.keys import mod
from modules.colors import colors


def shutdown_menu():
    qtile.cmd_spawn(home + "/.config/qtile/shutdown.sh")

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
                    text = "",
                    foreground = ["#f1ffff", "#f1ffff"],
                    background = colors[0],
                    fontsize = 20,
                    padding = 15,
                    mouse_callbacks = {"Button1" : lambda: qtile.cmd_spawn('rofi -show drun')},
                ),
                widget.GroupBox(
                    foreground = ["#f1ffff", "#f1ffff"],
                    background = ["#0f101a", "#0f101a"],
                    font = 'Ubuntu Bold',
                    fontsize = 9,
                    margin_y = 6,
                    margin_x = 3,
                    padding_y = 8,
                    padding_x = 6,
                    borderwidth = 3,
                    active = colors[1],
                    inactive = ["#f1ffff", "#f1ffff"],
                    rounded = False,
                    highlight_method = 'line',
                    this_current_screen_border = ["#a151d3", "#a151d3"],
                    this_screen_border = ["#353c4a", "#353c4a"],
                    other_current_screen_border = ["#0f101a", "#0f101a"],
                    other_screen_border = ["#0f101a", "#0f101a"]
                ),
                widget.WindowName(
                    foreground = ["#a151d3", "#a151d3"],
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
                    text="",
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0f101a", "#0f101a"],
                    fontsize = 50,
                    padding= -3
                ), 
                widget.TextBox(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                    text=' ' # Icon: nf-fa-feed
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
                    text="",
                    foreground=["#0174DF", "#0174DF"],
                    background=["#a151d3", "#a151d3"],
                    fontsize = 50,
                    padding= -3
                ),
                widget.TextBox(
                    text="󰃞",
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
                    text="",
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
                    text="",
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
                    text="",
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0174DF", "#0174DF"],
                    fontsize = 50,
                    padding= -3, 
                ),
                widget.TextBox(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                    text='󰃰 ' # Icon: nf-mdi-calendar_clock
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
                    text="",
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
                    text="",
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
                    text="",
                    foreground=["#0174DF", "#0174DF"],
                    background=["#a151d3", "#a151d3"],
                    fontsize = 50,
                    padding= -3
                ),
                widget.TextBox(
                    text="󰃞",
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
                    text="",
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
                    text="",
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
                    text="",
                    foreground=["#a151d3", "#a151d3"],
                    background=["#0174DF", "#0174DF"],
                    fontsize = 50,
                    padding= -3, 
                ),
                widget.TextBox(
                    foreground=["#0f101a", "#0f101a"],
                    background=["#a151d3", "#a151d3"],
                    text='󰃰 ' # Icon: nf-mdi-calendar_clock
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
