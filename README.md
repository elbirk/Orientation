# Orientation
RetoPie/Emulationstation change orientation with a button/switch


I want to rotate the screen manually but want Retropie to rotate automatically when I rotate the screen. I solved this by having a switch that is closed when the screen is vertical and another switch connected to F4 (exit Emulation Station). I start Emulation Station through a script that calls a Python program that reads if the screen is vertical / horizontal on a raspberry GPIO. Then I call Emulation Station with vertical or horizontal command. If I rotate the screen it calls F4 and then the script.
