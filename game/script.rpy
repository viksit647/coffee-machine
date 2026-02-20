
# Coffee Vending Machine - Script

init -1:
    # Variables
    default selected_coffee = "None"
    default milk_amount = 5
    default coffee_amount = 5
    default show_debug_area = True

# Define images
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
        
        # Step 5: Reveal
        call screen coffee_reveal
        
        # Reset and loop
        $ selected_coffee = "None"
        jump main_loop

    return
