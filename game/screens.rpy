# Screens for the Coffee Vending Machine

# 1. The main interaction screen (the machine itself)
screen machine_interaction():
    # This is the "Area of Affect". 
    # Change the xpos, ypos, width, height to match the machine in your image.
    button:
        # ADJUST THESE PARAMETERS:
        xpos 400 
        ypos 100
        xsize 480
        ysize 520
        
        # Action to progress the script
        action Return()
        
        # Visual feedback: A bright purple outline for debugging
        if show_debug_area:
            background Frame(Solid("#BF00FF"), 2, 2) # Purple border
        else:
            background None

# 2. Coffee Type Selection Screen
screen coffee_selection_menu():
    modal True
    add Solid("#000000a0") # Dim the background
    
    vbox:
        align (0.5, 0.4)
        spacing 10
        
        label "SELECT YOUR DRINK" xalign 0.5 text_size 40 text_color "#ffffff"
        
        grid 2 3: # 2 columns, 3 rows for 6 types
            spacing 20
            xalign 0.5
            
            # Note: Add your specific coffee images here later
            # For now, these are text buttons that set the variable
            textbutton "Espresso" action [SetVariable("selected_coffee", "Espresso"), Return()]
            textbutton "Americano" action [SetVariable("selected_coffee", "Americano"), Return()]
            textbutton "Cappuccino" action [SetVariable("selected_coffee", "Cappuccino"), Return()]
            textbutton "Latte" action [SetVariable("selected_coffee", "Latte"), Return()]
            textbutton "Mocha" action [SetVariable("selected_coffee", "Mocha"), Return()]
            textbutton "Macchiato" action [SetVariable("selected_coffee", "Macchiato"), Return()]

# 3. Customization Screen (Sliders)
screen customization_menu():
    modal True
    add Solid("#000000a0")
    
    vbox:
        align (0.5, 0.4)
        spacing 30
        
        label "CUSTOMIZE: [selected_coffee]" xalign 0.5 text_size 40 text_color "#ffffff"
        
        # Coffee Amount
        vbox:
            spacing 5
            label "Coffee Strength" xalign 0.5
            hbox:
                spacing 20
                bar value VariableValue("coffee_amount", 10):
                    xsize 400
                text "[coffee_amount]"
        
        # Milk Amount
        vbox:
            spacing 5
            label "Milk Amount" xalign 0.5
            hbox:
                spacing 20
                bar value VariableValue("milk_amount", 10):
                    xsize 400
                text "[milk_amount]"

        null height 20
        
        textbutton "START BREWING":
            xalign 0.5
            padding (30, 15)
            background Frame(Solid("#4a2c2a"), 4, 4)
            hover_background Solid("#6a3c3a")
            action Return()

# Basic Styles
style default:
    font "DejaVuSans.ttf"
    size 24
    color "#ffffff"

style button:
    background Solid("#333333")
    padding (15, 10)
    hover_background Solid("#555555")

style button_text:
    idle_color "#ffffff"
    hover_color "#ffcc00"
    size 28
    xalign 0.5
