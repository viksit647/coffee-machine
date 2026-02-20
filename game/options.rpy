
define config.name = _("Coffee Vending Machine")
define gui.show_name = True
define config.version = "1.0"
define gui.about = _("")
define build.name = "coffee_machine"
define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.main_menu_music = None
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None
define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
default preferences.text_cps = 0
default preferences.afm_time = 15
define config.save_directory = "coffee_machine-123456789"
define config.window_icon = "gui/window_icon.png"

init python:
    build.directory_name = "coffee_machine"
    build.executable_name = "coffee_machine"
    build.include_update = False
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.documentation('*.html')
    build.documentation('*.txt')
