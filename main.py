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



#############################################

char = game.create_sprite(2, 2)

def on_forever():
    if input.acceleration(Dimension.Y) > 0:
        char.change(LedSpriteProperty.Y, 1)
        basic.pause(100)
    if input.acceleration(Dimension.Y) < 0:
        char.change(LedSpriteProperty.Y, -1)
        basic.pause(100)
    if input.acceleration(Dimension.X) < 0:
        char.change(LedSpriteProperty.X, -1)
        basic.pause(100)
    if input.acceleration(Dimension.X) > 0:
        char.change(LedSpriteProperty.X, 1)
        basic.pause(100)
basic.forever(on_forever)
