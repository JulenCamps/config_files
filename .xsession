#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap
sysresources=/etc/X11/xinit/.Xresources
sysmodmap=/etc/X11/xinit/.Xmodmap

# merge in defaults and keymaps

if [ -f $sysresources ]; then
    xrdb -merge $sysresources
fi

if [ -f $sysmodmap ]; then
    xmodmap $sysmodmap
fi

if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

# start some nice programs

#Set my personal screen layout
#xrandr --output HDMI-0 --primary --mode 1920x1080 --pos 1920x0 --rotate normal --output eDP-1-1 --mode 1920x1080 --pos 0x0 --rotate normal

#Secondary screen layout
xrandr --output HDMI-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal --output eDP-1-1 --mode 1920x1080 --pos 0x1080 --rotate normal

if [ -d /etc/X11/xinit/xinitrc.d ] ; then
 for f in /etc/X11/xinit/xinitrc.d/?*.sh ; do
  [ -x "$f" ] && . "$f"
 done
 unset f
fi

#Nextcloud
#nextcloud &
# Keyboard Layout
setxkbmap es &
# Wallpaper
 feh --bg-scale /home/julen/.config/qtile/img/004.jpg &
# Composer
picom & 
# Udiskie
udiskie -t &
# Network
nm-applet &
#Mullvad
mullvad-vpn &
#Optimus manager
optimus-manager-qt &
#Policykit
lxpolkit &
#Lenguagetool(server)
java -cp /opt/LanguageTool-5.6/languagetool-server.jar org.languagetool.server.HTTPServer --port 8081 --allow-origin &
