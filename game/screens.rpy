# Coffee Vending Machine - Screens

# Essential RenPy Screen
screen say(who, what):
    window:
        id "window"
        yalign 0.95
        xfill True
        padding (50, 20)
        background Solid("#000000c0")
        vbox:
            if who:
                text who id "who" size 30 color "#ffcc00"
            text what id "what" size 26

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
    button:
        xpos 400 ypos 100 xsize 480 ysize 520
        action Return()
        if show_debug_area:
            background Frame(Solid("#BF00FF"), 4, 4)
        else:
            background None
    
    textbutton "Toggle Debug" action ToggleVariable("show_debug_area"):
        align (1.0, 0.0)
        text_size 14

# 2. Coffee Type Selection
screen coffee_selection():
    modal True
    add "bg_machine":
        blur 20
    add Solid("#00000060")
    
    vbox:
        align (0.5, 0.4)
        spacing 30
        label "{b}SELECT DRINK{/b}" xalign 0.5 text_size 40
        
        hbox:
            spacing 40
            xalign 0.5
            for c in [("Americano", "americano(1:1).png"), ("Latte", "latte(1:1).png"), ("Mocha", "mocha(1:1).png")]:
                $ img = "images/" + c[1]
                vbox:
                    spacing 10
                    frame:
                        padding (4, 4)
                        background Solid("#D2A43A") # Light Brown / Brownish color
                        imagebutton:
                            idle Image(img)
                            hover Image(img)
                            action [SetVariable("selected_coffee", c[0]), Return()]
                            at transform:
                                xysize (180, 180)
                    text c[0] xalign 0.5

# 3. Customization Sliders
screen customization_screen():
    modal True
    add "bg_machine":
        blur 20
    add Solid("#00000060")
    
    vbox:
        align (0.5, 0.45) # Adjusted to fit screen better
        spacing 30
        
        label "{b}CUSTOMIZE [selected_coffee]{/b}" xalign 0.5 text_size 45
        
        hbox:
            spacing 350 # Adjusted separation
            xalign 0.5
            
            # Coffee Strength (0-10 for 10 subsections)
            vbox:
                spacing 15
                label "COFFEE" xalign 0.5 text_size 28
                fixed:
                    xsize 70 ysize 350 xalign 0.5
                    # The Bar Container
                    add Solid("#222222", xsize=70, ysize=350) 
                    
                    vbar value VariableValue("coffee_amount", 10):
                        style "segmented_vbar"
                        xsize 70 ysize 350
                    
                    # 9 Lines to make 10 sections
                    for i in range(1, 10):
                        add Solid("#ffffff30", xsize=70, ysize=2) ypos (i * 35)
                
                text "[coffee_amount]" xalign 0.5 size 30 color "#ffcc00"
            
            # Milk Amount
            vbox:
                spacing 15
                label "MILK" xalign 0.5 text_size 28
                fixed:
                    xsize 70 ysize 350 xalign 0.5
                    add Solid("#222222", xsize=70, ysize=350)
                    
                    vbar value VariableValue("milk_amount", 10):
                        style "segmented_vbar"
                        xsize 70 ysize 350
                    
                    for i in range(1, 10):
                        add Solid("#ffffff30", xsize=70, ysize=2) ypos (i * 35)

                text "[milk_amount]" xalign 0.5 size 30 color "#ffcc00"

        textbutton "BREW COFFEE" action Return():
            xalign 0.5 padding (40, 15)
            background Solid("#4a2c2a")
            hover_background Solid("#6a3c3a")

# 4. Final Coffee Reveal Screen
screen coffee_reveal():
    modal True
    add "bg_machine":
        blur 30
    add Solid("#00000080")
    
    frame:
        align (0.5, 0.5)
        xsize 800
        ysize 600
        background Solid("#333333e0") # A semi-transparent dark frame
        padding (30, 30) # Padding applied to the frame
        
        vbox:
            spacing 30
            xfill True
            yfill True
            
            label "{color=#ffcc00}{b}YOUR [selected_coffee!u] IS READY{/b}{/color}" xalign 0.5 text_size 40
            
            $ cup_image = "images/" + selected_coffee.lower() + "_nobg.png" 
            add cup_image:
                xalign 0.5
                yalign 0.5
                at transform:
                    size (400, 300)
                    fit 'contain'
            
            text "Enjoy your drink!" xalign 0.5 size 26
            
            textbutton "FINISH" action Return():
                xalign 0.5 padding (50, 15)
                background Solid("#4a2c2a")
                hover_background Solid("#6a3c3a")

# Styles
style button_text:
    color "#ffffff"
    hover_color "#ffcc00"
    size 24

style vbar:
    bottom_bar Solid("#ffcc00")
    top_bar Solid("#00000000") # Transparent so background shows
    thumb None
    bottom_gutter 0
    top_gutter 0

style segmented_vbar is vbar:
    xsize 70
    ysize 350
