#!/bin/sh
feh --bg-scale /usr/share/endeavouros/backgrounds/eos_wallpapers_community/krimkerre_2_poly.jpg

nm-applet & disown

clipster -d & disown

setxkbmap 'us,ru,uz' -option 'grp:caps_toggle' & disown

# picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
# ~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
# eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
