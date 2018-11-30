from __future__ import print_function
import ipywidgets as widgets
from IPython.display import display
button = widgets.Button(description="Tip event loop")
display(button)

def on_button_clicked(b):
    print("Since it takes a long time to run over all data, only run over a small number of events while developing. Then, when you are satisfied with the method, you can increase the number of events.")

button.on_click(on_button_clicked)
