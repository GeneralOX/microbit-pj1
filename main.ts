let number = 0
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    basic.showNumber(receivedNumber)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    number += number - 1
    basic.showNumber(number)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    radio.sendNumber(number)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    number += number + 1
    basic.showNumber(number)
})
