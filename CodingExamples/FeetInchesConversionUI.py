import FreeSimpleGUI as Fsg

feet_text = Fsg.Text("Enter feet:")
inch_text = Fsg.Text("Enter inches:")
ft_input = Fsg.Input()
in_input = Fsg.Input()
convert_button = Fsg.Button("Convert")

window = Fsg.Window("Convertor", layout=[[feet_text, ft_input], [inch_text, in_input], [convert_button]])
window.read()
window.close()