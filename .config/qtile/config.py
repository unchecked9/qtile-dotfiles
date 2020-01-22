from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget

from typing import List  # noqa: F401

mod = 'mod4'
colors = {
    'black1': '000000',
    'black2': '515151',
    'white1': 'ffffff',
    'white2': 'cccccc',
    'cyan': '3e83d8',
    'blue': '7f70e7',
    'magenta': '9f65ed'
}

keys = [
    # Custom application keybinds
    Key([mod], 'w', lazy.spawn('firefox')),
    Key([mod], 'e', lazy.spawn('emacs')),
    Key([mod], 'r', lazy.spawn('rofi -show run')),
    Key([mod], 'c', lazy.spawn('code')),
    Key([mod], 'v', lazy.spawn('urxvt -e vifm')),
    Key([mod], 'g', lazy.spawn('gimp')),
    Key([mod], 'Return', lazy.spawn('urxvt')),

    # Window operation keybinds
    Key([mod], 'k', lazy.layout.down()),
    Key([mod], 'j', lazy.layout.up()),
    Key([mod, 'control'], 'k', lazy.layout.shuffle_down()),
    Key([mod, 'control'], 'j', lazy.layout.shuffle_up()),
    Key([mod, 'shift'], 'q', lazy.window.kill()),
    Key([mod], 'f', lazy.window.toggle_fullscreen()),

    # Qtile operation keybinds
    Key([mod, 'control'], 'r', lazy.restart()),
    Key([mod], '0', lazy.shutdown()),
]

groups = [Group(i) for i in '123456']

for i in groups:
    keys.extend([
        # Group operation keybinds
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)),
    ])

layouts = [
    layout.MonadTall(
        border_focus=colors['white1'],
        border_normal=colors['black1'],
        border_width=1,
        margin=10
    )
]

widget_defaults = dict(
    font='SourceCodePro-Black',
    fontsize=18,
    padding=4,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method='line',
                    background=colors['blue'],
                    active=colors['white1'],
                    inactive=colors['black2'],
                    highlight_color=[colors['blue'], colors['blue']],
                    this_current_screen_border=colors['black1']
                ),
                widget.Image(
                    filename='~/.config/qtile/edge1.png'
                ),
                widget.Spacer(),
                widget.Image(
                    filename='~/.config/qtile/edge2.png'
                ),
                widget.Battery(
                    format='{char} {percent:2.0%}',
                    background=colors['magenta'],
                    foreground=colors['white1'],
                    low_foreground=colors['white1']
                ),
                widget.Image(
                    filename='~/.config/qtile/edge3.png'
                ),
                widget.Clock(
                    format='%m-%d-%y',
                    background=colors['cyan'],
                    foreground=colors['white2']
                ),
                widget.Image(
                    filename='~/.config/qtile/edge4.png'
                ),
                widget.Clock(
                    format='%a',
                    background=colors['magenta'],
                    foreground=colors['white1']
                ),
                widget.Image(
                    filename='~/.config/qtile/edge3.png'
                ),
                widget.Clock(
                    format='%I:%M %p',
                    background=colors['cyan'],
                    foreground=colors['white2']
                ),
            ],
            30,
            background=colors['black2']
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], 'Button1', lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], 'Button2', lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = 'smart'

wmname = 'qtile'
