
# Standard Ren'Py screens

screen say(who, what):
    style_prefix "say"
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"

screen main_menu():
    tag menu
    add gui.main_menu_background
    vbox:
        style_prefix "navigation"
        xalign 0.5
        yalign 0.5
        spacing 20
        text "[config.name!t]" size 80 xalign 0.5
        textbutton _("Start") action Start()
        textbutton _("Quit") action Quit(confirm=False)

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign gui.navigation_yalign
        spacing gui.navigation_spacing
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Quit") action Quit()

# --- Custom Coffee Machine Screens ---

screen machine_interaction():
    # ADJUST THESE PARAMETERS:
    button:
        xpos 400 
        ypos 100
        xsize 480
        ysize 520
        action Return()
        if show_debug_area:
            background Frame(Solid("#BF00FF"), 2, 2)
        else:
            background None

screen coffee_selection_menu():
    modal True
    add Solid("#000000a0")
    vbox:
        align (0.5, 0.4)
        spacing 10
        label "SELECT YOUR DRINK" xalign 0.5 text_size 40
        grid 2 3:
            spacing 20
            xalign 0.5
            textbutton "Espresso" action [SetVariable("selected_coffee", "Espresso"), Return()]
            textbutton "Americano" action [SetVariable("selected_coffee", "Americano"), Return()]
            textbutton "Cappuccino" action [SetVariable("selected_coffee", "Cappuccino"), Return()]
            textbutton "Latte" action [SetVariable("selected_coffee", "Latte"), Return()]
            textbutton "Mocha" action [SetVariable("selected_coffee", "Mocha"), Return()]
            textbutton "Macchiato" action [SetVariable("selected_coffee", "Macchiato"), Return()]

screen customization_menu():
    modal True
    add Solid("#000000a0")
    vbox:
        align (0.5, 0.4)
        spacing 30
        label "CUSTOMIZE: [selected_coffee]" xalign 0.5 text_size 40
        vbox:
            spacing 5
            label "Coffee Strength" xalign 0.5
            hbox:
                spacing 20
                bar value VariableValue("coffee_amount", 10) xsize 400
                text "[coffee_amount]"
        vbox:
            spacing 5
            label "Milk Amount" xalign 0.5
            hbox:
                spacing 20
                bar value VariableValue("milk_amount", 10) xsize 400
                text "[milk_amount]"
        null height 20
        textbutton "START BREWING":
            xalign 0.5
            padding (30, 15)
            background Frame(Solid("#4a2c2a"), 4, 4)
            action Return()

# Basic Styles
style say_window is default
style say_label is default
style say_dialogue is default
style namebox is default

style say_window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Solid("#00000080")

style say_dialogue:
    xpos gui.text_xpos
    xsize gui.text_width
    ypos gui.text_ypos
    color "#ffffff"

style namebox:
    xpos gui.name_xpos
    ypos gui.name_ypos
    background Solid("#000000a0")
    padding (10, 5)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style gui_button:
    background Solid("#333333")
    padding (10, 5)

style gui_button_text:
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color
