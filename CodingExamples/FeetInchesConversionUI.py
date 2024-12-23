import FreeSimpleGUI as Fsg

Fsg.theme("Black")

feet_text = Fsg.Text("Enter feet:")
inch_text = Fsg.Text("Enter inches:")
ft_input = Fsg.Input(key="feet_entered")
in_input = Fsg.Input(key="inches_entered")
convert_button = Fsg.Button("Convert", key="convert_button_pressed")
meters_text = Fsg.Text("Meters: ", key="meters_text_key")
exit_button = Fsg.Button("Exit")

window = Fsg.Window("Convertor", layout=[[feet_text, ft_input],
                                                [inch_text, in_input],
                                                [convert_button, meters_text, exit_button]
                                             ])

while True:
    event, value = window.read()
    match event:
        case "convert_button_pressed":
            try:
                feet = float(window["feet_entered"].get())
                inches = float(window["inches_entered"].get())
                meters = round((feet * 0.3048) + (inches * 0.0254), 2)
                new_meters_text = "Meters: " + str(meters)
                window["meters_text_key"].update(value=new_meters_text)
            except ValueError:
                Fsg.popup("Please provide two numbers for conversion")
        case "Exit":
            break
        case Fsg.WIN_CLOSED:
            break
window.close()