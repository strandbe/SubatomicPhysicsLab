from __future__ import print_function
import ipywidgets as widgets
from IPython.display import display
button = widgets.Button(description="Tip resonance shape")
display(button)

def on_button_clicked(b):
    print("Check out https://en.wikipedia.org/wiki/Resonance_(particle_physics)" )

button.on_click(on_button_clicked)
