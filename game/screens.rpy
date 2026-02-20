# Coffee Vending Machine - Screens

# Essential RenPy Screen
screen say(who, what):
    window:
        id "window"
        yalign 1.0
        xfill True
        padding (50, 20)
        background Solid("#000000c0")
        
        vbox:
            if who:
                text who id "who" font "DejaVuSans.ttf" size 30 color "#ffcc00"
            text what id "what" font "DejaVuSans.ttf" size 26

# Main Menu
screen main_menu():
    tag menu
    add Solid("#1a1a1a")
    vbox:
        align (0.5, 0.5)
        spacing 20
        text "COFFEE MACHINE" size 60 color "#ffffff" xalign 0.5
        textbutton "Start" action Start() xalign 0.5
        textbutton "Quit" action Quit(confirm=False) xalign 0.5

# 1. Clickable Area
screen machine_interaction():
    # ADJUST THESE COORDINATES:
    button:
        xpos 400 ypos 100 xsize 480 ysize 520
        action Return()
        if show_debug_area:
            background Frame(Solid("#BF00FF"), 4, 4)
        else:
            background None
    
    # Tiny toggle button for debug mode
    textbutton "Toggle Debug" action ToggleVariable("show_debug_area"):
        align (1.0, 0.0)
        text_size 14

# 2. Coffee Type Selection
screen coffee_selection():
    modal True
    add Solid("#000000a0")
    
    vbox:
        align (0.5, 0.4)
        spacing 20
        label "{b}SELECT DRINK{/b}" xalign 0.5 text_size 40
        
        vpgrid:
            cols 2
            spacing 20
            xalign 0.5
            draggable True
            mousewheel True
            
            for c in ["Espresso", "Americano", "Cappuccino", "Latte", "Mocha", "Macchiato"]:
                textbutton c:
                    xsize 200 padding (10, 10)
                    background Solid("#333333")
                    hover_background Solid("#555555")
                    text_align 0.5
                    action [SetVariable("selected_coffee", c), Return()]

# 3. Customization Sliders
screen customization_screen():
    modal True
    add Solid("#000000a0")
    
    vbox:
        align (0.5, 0.4)
        spacing 40
        
        label "{b}CUSTOMIZE [selected_coffee]{/b}" xalign 0.5 text_size 40
        
        vbox:
            spacing 10
            label "Coffee Strength ([coffee_amount])" xalign 0.5
            bar value VariableValue("coffee_amount", 10) xsize 500 xalign 0.5
            
        vbox:
            spacing 10
            label "Milk Amount ([milk_amount])" xalign 0.5
            bar value VariableValue("milk_amount", 10) xsize 500 xalign 0.5

        textbutton "BREW" action Return():
            xalign 0.5 padding (40, 20)
            background Solid("#4a2c2a")
            hover_background Solid("#6a3c3a")

# Minimal Button Styles
style button:
    padding (10, 5)
style button_text:
    color "#ffffff"
    hover_color "#ffcc00"
    size 24
