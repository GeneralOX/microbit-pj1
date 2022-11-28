number = 0

def on_received_number(receivedNumber):
    basic.show_number(receivedNumber)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global number
    number += number - 1
    basic.show_number(number)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_number(number)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global number
    number += number + 1
    basic.show_number(number)
input.on_button_pressed(Button.B, on_button_pressed_b)
