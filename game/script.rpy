
# Coffee Vending Machine - Script

# Variables
default selected_coffee = "None"
default milk_amount = 5
default coffee_amount = 5
default show_debug_area = True

# Define images
# RenPy automatically finds files in images/, but let's be explicit
image bg_machine = "images/coffee_machine_final_2.png"

label start:
    # Use a solid color fallback if image fails to load
    scene black
    show bg_machine onlayer master:
        xalign 0.5 yalign 0.5
    
    label main_loop:
        # Step 1: Click the machine
        call screen machine_interaction
        
        # Step 2: Choose Coffee
        call screen coffee_selection
        
        # Step 3: Customize
        call screen customization_screen
        
        # Step 4: Result
        "The machine whirrs into action..."
        "Your [selected_coffee] (Coffee: [coffee_amount], Milk: [milk_amount]) is ready! Enjoy!"
        
        jump main_loop

    return
