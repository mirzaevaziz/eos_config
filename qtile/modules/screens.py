from .widgets import *
from libqtile import bar
from libqtile.config import Screen
from libqtile.command import lazy
from modules.keys import terminal
import os

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(padding=3, linewidth=0, background="#2f343f"),
                widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background="#2f343f",
                             mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background="#2f343f"),
                widget.GroupBox(
                    highlight_method='line',
                    this_screen_border="#5294e2",
                    this_current_screen_border="#5294e2",
                    active="#ffffff",
                    inactive="#848e96",
                    background="#2f343f"),
                widget.TextBox(
                    text='',
                    padding=0,
                    fontsize=28,
                    background="#94918f",
                    foreground='#2f343f'
                ),
                widget.Sep(padding=5, linewidth=0, background="#94918f"),
                widget.TextBox(
                    text='',
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn('qutebrowser')
                    },
                    foreground='#e8e8e8',
                    background="#94918f"
                ),
                widget.TextBox(
                    text='',
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn('google-chrome-stable')
                    },
                    foreground='#e8e8e8',
                    background="#94918f"
                ),
                widget.TextBox(
                    text='',
                    background="#94918f",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn('thunar')
                    },
                    foreground='#e8e8e8'
                ),
                widget.TextBox(
                    text='',
                    background="#94918f",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn('remmina')
                    },
                    foreground='#e8e8e8'
                ),
                widget.TextBox(
                    text='',
                    background="#94918f",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn('dbeaver')
                    },
                    foreground='#e8e8e8'
                ),
                widget.TextBox(
                    text='',
                    background="#94918f",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn('ymp')
                    },
                    foreground='#e8e8e8'
                ),
                widget.TextBox(
                    text='',
                    background="#94918f",
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn('code /home/ts/.config/')
                    },
                    foreground='#e8e8e8'
                ),
                widget.TextBox(
                    text='',
                    padding=0,
                    fontsize=28,
                    foreground='#94918f'
                ),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground='#99c0de', fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.TextBox(
                    text='',
                    padding=0,
                    fontsize=28,
                    foreground='#2f343f'
                ),
                widget.Systray(icon_size=20, background="#2f343f"),
                widget.Sep(padding=5, linewidth=0, background="#2f343f"),
                volume,
                widget.Clock(format='  %d.%m.%Y %a %I:%M %p',
                             background="#2f343f",
                             foreground='#9bd689'),
                widget.TextBox(
                    text='',
                    padding=0,
                    fontsize=28,
                    foreground='#404552',
                    background="#2f343f",
                ),
                widget.TextBox(
                    text='',
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser(
                            '~/.config/rofi/powermenu.sh'))
                    },
                    foreground='#e39378'
                ),
                widget.Sep(padding=5, linewidth=0),
            ],
            20,  # height in px
            background="#404552"  # background color
        ), ),
    Screen(
        top=bar.Bar(
            [
                widget.Sep(padding=3, linewidth=0, background="#2f343f"),
                widget.Image(filename='~/.config/qtile/eos-c.png', margin=3, background="#2f343f",
                             mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background="#2f343f"),
                widget.GroupBox(
                    highlight_method='line',
                    this_screen_border="#5294e2",
                    this_current_screen_border="#5294e2",
                    active="#ffffff",
                    inactive="#848e96",
                    background="#2f343f"),
                widget.TextBox(
                    text='',
                    padding=0,
                    fontsize=28,
                    foreground='#2f343f'
                ),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground='#99c0de', fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.TextBox(
                    text='',
                    padding=0,
                    fontsize=28,
                    foreground='#2f343f'
                ),
                volume,
                widget.Clock(format='  %d.%m.%Y %a %I:%M %p',
                             background="#2f343f",
                             foreground='#9bd689'),
                widget.TextBox(
                    text='',
                    padding=0,
                    fontsize=28,
                    foreground='#404552',
                    background="#2f343f",
                ),
                widget.TextBox(
                    text='',
                    mouse_callbacks={
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser(
                            '~/.config/rofi/powermenu.sh'))
                    },
                    foreground='#e39378'
                ),
                widget.Sep(padding=5, linewidth=0),
            ],
            20,  # height in px
            background="#404552"  # background color
        ), ),
]
