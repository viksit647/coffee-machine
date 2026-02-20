# Ren'Py Coffee Vending Machine

An interactive coffee vending machine project for Ren'Py. This project features a clickable machine interface, a drink selection menu, and customization sliders for coffee and milk amounts.

## 🛠 Features

- **Interactive Background**: Click on the vending machine to start the process.
- **Selection System**: Choose from multiple coffee types (Espresso, Latte, etc.).
- **Customization**: Adjust the strength of your coffee and the amount of milk using interactive sliders.
- **Debug Mode**: Includes a visible purple outline to help you perfectly align the clickable area with your custom background images.

## 🚀 How to Run

1.  Download or clone this repository.
2.  Open the **Ren'Py Launcher**.
3.  Click **"+" (Add Project)** and select the folder containing this project.
4.  Click **Launch Project**.

## 🔧 Customization

### Adjusting the Clickable Area
To move or resize the interactive area of the machine:
1.  Open `game/screens.rpy`.
2.  Find the `screen machine_interaction():` block.
3.  Modify the `xpos`, `ypos`, `xsize`, and `ysize` values to match your image.
4.  **To Hide the Debug Outline**: In `game/script.rpy`, set `default show_debug_area = False`.

### Adding Custom Coffee Images
The selection menu currently uses text buttons. To add images for the coffee types:
1.  Place your images in `game/images/`.
2.  In `game/screens.rpy`, update the `coffee_selection_menu` to use `imagebutton` instead of `textbutton`.

## 📂 Project Structure

- `game/script.rpy`: Logic flow and game state variables.
- `game/screens.rpy`: UI definitions for the machine, selection menu, and sliders.
- `game/options.rpy`: Project configuration and build settings.
- `game/images/`: Contains backgrounds and asset files.

## 📝 License
Feel free to use and modify this for your own Ren'Py projects!
