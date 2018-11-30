from __future__ import print_function
import ipywidgets as widgets
from IPython.display import display
button = widgets.Button(description="Give hint")
display(button)

def on_button_clicked(b):
    print("Hover with the mouse over a data point to see its value and corresponding uncertainty." )

button.on_click(on_button_clicked)
