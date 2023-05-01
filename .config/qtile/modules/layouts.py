#Qtile Configuration
#Julen Camps
# Layouts and layout rules

from libqtile import layout

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