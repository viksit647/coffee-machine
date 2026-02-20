define config.name = _("Coffee Vending Machine")
define gui.show_name = True
define config.version = "1.0"
define gui.about = _("")
define build.name = "coffee_machine"
define config.has_sound = False
define config.has_music = False
define config.has_voice = False
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
default preferences.text_cps = 50
default preferences.afm_time = 15
define config.save_directory = "coffee_machine-123"
define config.window_icon = None

init python:
    # Set the resolution explicitly
    gui.init(1280, 720)
