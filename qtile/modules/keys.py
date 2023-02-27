import os
from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "xfce4-terminal"


def window_to_previous_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i == 0:
        i = len(qtile.screens)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i - 1)


def window_to_next_screen(qtile, switch_group=False, switch_screen=False):
    i = qtile.screens.index(qtile.current_screen)
    if i == len(qtile.screens) - 1:
        i = -1
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group, switch_group=switch_group)
        if switch_screen == True:
            qtile.cmd_to_screen(i + 1)


keys = [
    Key([mod], "v", lazy.spawn('clipster -sp'),
        desc='clipster history selector'),
    Key([mod], "z", lazy.spawn('telegram-desktop'), desc='telegram-desktop'),
    Key([mod, "control"], "s", lazy.spawn(os.path.expanduser(
        '~/.config/rofi/powermenu.sh')), desc="Screenshot tool"),
    Key([mod, "shift"], "s", lazy.spawn(
        "flameshot gui"), desc="Screenshot tool"),

    Key([mod], "comma", lazy.prev_screen(), desc="Focus to the left screen"),
    Key([mod], "period", lazy.next_screen(), desc="Focus to the right screen"),

    Key([mod, "shift"],  "comma",  lazy.function(window_to_next_screen)),
    Key([mod, "shift"],  "period", lazy.function(window_to_previous_screen)),
    Key([mod, "control"], "comma",  lazy.function(
        window_to_next_screen, switch_screen=True)),
    Key([mod, "control"], "period", lazy.function(
        window_to_previous_screen, switch_screen=True)),



    Key([mod], "t", lazy.window.toggle_floating(),
        desc="Toggle floating window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen window"),

    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout."),


    # Switch between windows
    Key([mod], "left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "d", lazy.spawn("rofi -show combi"), desc="spawn rofi"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    Key([mod, "mod1"], "space", lazy.layout.previous(),
        desc="Move window focus to other window"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"],
        "j",
        lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
    Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
    Key([mod, "shift"], "space", lazy.layout.flip()),
    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 3%+")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 3%-")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle")),
]
