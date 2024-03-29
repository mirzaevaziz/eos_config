#!/bin/sh
feh --bg-scale /home/ts/Pictures/plane_sky_art_129149_1920x1080.jpg

/usr/lib/geoclue-2.0/demos/agent & disown
redshift-gtk & disown
nm-applet & disown
caffeine & disown
clipster -d & disown

setxkbmap 'us,ru,uz' -option 'grp:caps_toggle' & disown

picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
# ~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
# eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
