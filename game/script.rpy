# Coffee Vending Machine Script

# Game state
default selected_coffee = None
default milk_amount = 5
default coffee_amount = 5
default brewing = False

# Debug flag for the interactive area outline
define config.developer = True
default show_debug_area = True

image background_machine = "images/coffee_machine_final_2.png"

label start:
    scene background_machine
    
    # Main interaction loop
    label interaction_loop:
        call screen machine_interaction
        
        # Once the machine is clicked, show the selection menu
        call screen coffee_selection_menu
        
        # After selecting coffee, show the customization menu
        call screen customization_menu
        
        # Brewing animation or message
        "Brewing your [selected_coffee]..."
        "Your [selected_coffee] (Coffee: [coffee_amount], Milk: [milk_amount]) is ready!"
        
        # Reset and loop back
        $ selected_coffee = None
        jump interaction_loop

    return
