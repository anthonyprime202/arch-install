# at https://docs.qtile.org/en/latest/manual/config/lazy.html

# <-----------------------------------------------------------> #
# <------------------------- IMPORTS -------------------------> #
# <-----------------------------------------------------------> #


# <-------------------------- QTILE --------------------------> #
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.utils import guess_terminal
from libqtile import layout, hook, bar
from libqtile.lazy import lazy
# <----------------------- QTILE EXTRAS ----------------------> #
from qtile_extras import widget
# <-------------------------- CUSTOM -------------------------> #
from catppuccin import Flavour
# <------------------------ BUILT-INS ------------------------> #
import subprocess
import os

# <-----------------------------------------------------------> #
# <--------------------- USER VARIABLES ----------------------> #
# <-----------------------------------------------------------> #

mod = "mod4"
alt = "mod1"
terminal = guess_terminal()
mocha = Flavour.mocha()

# <-----------------------------------------------------------> #
# <----------------------- KEYBINDINGS -----------------------> #
# <-----------------------------------------------------------> #

keys = [
    # <-------------------------- ROFI -------------------------> #
    Key([mod], "r",                                 lazy.spawn("launcher"),                                 desc="Launch Rofi"),
    Key([mod, "control"], "q",                      lazy.spawn("powermenu"),                                desc="Launch Rofi PowerMenu"),
    Key([mod], "e",                                 lazy.spawn("emoji"),                                    desc="Launch Rofi"),
    # <----------------------- LAUNCHERS -----------------------> #
    Key([mod], "Return",                            lazy.spawn(terminal),                                   desc="Launch terminal"),
    Key([mod], "f",                                 lazy.spawn("firefox"),                                  desc="Launch firefox"),
    Key([mod], "d",                                 lazy.spawn("discord"),                                  desc="Launch discord"),
    # <------------------------- SYSTEM ------------------------> #
    Key([], "XF86MonBrightnessUp",                  lazy.spawn("brightnessbar up"),                         desc="Incrdase Brightness"),
    Key([], "XF86MonBrightnessDown",                lazy.spawn("brightnessbar down"),                       desc="Decrease Brightness"),
    Key([], "XF86AudioRaiseVolume",                 lazy.spawn("volumebar up"),                             desc="Increase Volume"),
    Key([], "XF86AudioLowerVolume",                 lazy.spawn("volumebar down"),                           desc="Decrease Volume"),
    Key([], "XF86AudioMute",                        lazy.spawn("volumebar mute"),                           desc="Mute Volume"),
    Key([], "XF86AudioPlay",                        lazy.spawn("playerctl play-pause"),                     desc="Play or Pause Media"),
    Key([], "XF86AudioStop",                        lazy.spawn("playerctl stop"),                           desc="Stop Media"),
    Key([], "XF86AudioNext",                        lazy.spawn("playerctl next"),                           desc="Skip to Next Media"),
    Key([], "XF86AudioPrev",                        lazy.spawn("playerctl previous"),                       desc="Go to Next Media"),
    # <-------------------- SWITCH WINDOWS --------------------> #
    Key([mod], "h",                                 lazy.layout.left(),                                     desc="Move focus to left"),
    Key([mod], "l",                                 lazy.layout.right(),                                    desc="Move focus to right"),
    Key([mod], "j",                                 lazy.layout.down(),                                     desc="Move focus down"),
    Key([mod], "k",                                 lazy.layout.up(),                                       desc="Move focus up"),
    Key([mod], "space",                             lazy.layout.next(),                                     desc="Move window focus to other window"),
    # <--------------------- SHIFT WINDOWS --------------------> #
    Key([mod, "shift"], "h",                        lazy.layout.swap_left(),                                desc="Move window to left"),
    Key([mod, "shift"], "l",                        lazy.layout.swap_right(),                               desc="Move window to right"),
    Key([mod, "shift"], "j",                        lazy.layout.shuffle_down(),                             desc="Move window to down"),
    Key([mod, "shift"], "k",                        lazy.layout.shuffle_up(),                               desc="Move window to up"),
    # <---------------------- WINDOW SIZE ---------------------> #
    Key([mod, "shift"], "i",                        lazy.layout.grow(),                                     desc="Grow window"),
    Key([mod, "shift"], "m",                        lazy.layout.shrink(),                                   desc="Shrink window"),
    Key([mod, "shift"], "n",                        lazy.layout.normalize(),                                desc="Reset all window sizes"),
    Key([mod, "shift"], "o",                        lazy.layout.maximize(),                                 desc="Maximize current window"),
    Key([mod, "shift"], "space",                    lazy.layout.flip(),                                     desc="Flip layout"),
    Key([mod], "Tab",                               lazy.next_layout(),                                     desc="Toggle between layouts"),
    Key([mod], "w",                                 lazy.window.kill(),                                     desc="Kill focused window"),
    Key([mod, "control"], "r",                      lazy.reload_config(),                                   desc="Reload the config"),
]


# <-----------------------------------------------------------> #
# <-------------------------- GROUPS -------------------------> #
# <-----------------------------------------------------------> #

# groups = [Group(i) for i in "123456789"]
groups = [Group(f"{i+1}", label="") for i in range(8)]

for i in groups:
    keys.extend(
[
    Key([mod], i.name,                              lazy.group[i.name].toscreen(),                          desc="Switch to group {}".format(i.name),),
    Key([mod, "shift"], i.name,                     lazy.window.togroup(i.name, switch_group=True),         desc="Switch to & move focused window to group {}".format(i.name)),
]
    )

# <-----------------------------------------------------------> #
# <----------------------- SCRATCHPADS -----------------------> #
# <-----------------------------------------------------------> #

groups.append(
    ScratchPad("scratchpad", 
[
    DropDown("term",    "alacritty",            x=0.05,     y=0.08,     width=0.9,      height=0.75),
    DropDown("music",   "spotify-launcher",     x=0.05,     y=0.08,     width=0.9,      height=0.75),
]
    )
)

keys.extend(
[
    Key([alt], "return",                            lazy.group["scratchpad"].dropdown_toggle("term"),       desc="Toggle terminal scratchpad"),
    Key([alt], "s",                                 lazy.group["scratchpad"].dropdown_toggle("music"),      desc="Toggle spotify scratchpad"),
]
)

# <-----------------------------------------------------------> #
# <------------------------- LAYOUTS -------------------------> #
# <-----------------------------------------------------------> #

layout_config = dict(
    margin=5,
    border_width=2,
    border_focus=mocha.blue.hex,
    border_normal=mocha.base.hex,
)

layouts = [
    layout.MonadTall(
        grow_amount=5,
        **layout_config,
    ),
    layout.Max(**layout_config),
]

# <-----------------------------------------------------------> #
# <--------------------------- BAR ---------------------------> #
# <-----------------------------------------------------------> #

widget_defaults = dict(
    font="FiraCode Font Bold",
    fontsize=12,
    padding=5,
)
extension_defaults = widget_defaults.copy()

soft_sep = {'linewidth': 2, 'size_percent': 70,
            'foreground': '393939', 'padding': 7}

main_bar = bar.Bar(
    [
        widget.GroupBox(),
        # widget.Mpris2(background='253253', name='spotify',
        #               stop_pause_text='▶', scroll_chars=None,
        #               display_metadata=['xesam:title', 'xesam:artist'],
        #               objname="org.mpris.MediaPlayer2.spotify"),
        widget.Sep(linewidth=2, size_percent=100, padding=12),
        widget.WindowName(),
        widget.Systray(),
        widget.Sep(**soft_sep),
        widget.Clock(format='%B %-d, %H:%M'),
    ], 30, 
    background=mocha.base.hex, margin=5, radius=10 
)

screens = [Screen(top=main_bar)]

# <-----------------------------------------------------------> #
# <--------------------- FLOATING RULES ----------------------> #
# <-----------------------------------------------------------> #

floating_layout = layout.Floating(
    border_focus=mocha.rosewater.hex,
    border_normal=mocha.base.hex,
    border_width=2,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="Event Tester"), # xev event tester
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="blueman-manager"), # blueman 
        Match(wm_class="lxappearance"), # lxappearance
        Match(wm_class="qt5ct"), # qt5ct
    ],
)

mouse = [
    Drag([mod], "Button1",                          lazy.window.set_position_floating(),                    start=lazy.window.get_position()),
    Drag([mod], "Button3",                          lazy.window.set_size_floating(),                        start=lazy.window.get_size()),
    Click([mod], "Button2",                         lazy.window.bring_to_front()),
]

# <-----------------------------------------------------------> #
# <----------------------- OTHER RULES -----------------------> #
# <-----------------------------------------------------------> #

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "Qtile"


# <-----------------------------------------------------------> #
# <------------------------ AUTOSTART ------------------------> #
# <-----------------------------------------------------------> #


@hook.subscribe.startup_once
def autostart():
    main_bar.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)
    home = os.path.expanduser("/home/anthonyprime/.local/scripts/autostart")
    subprocess.Popen([home])


