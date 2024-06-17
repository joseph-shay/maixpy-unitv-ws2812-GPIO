from Maix import GPIO
from fpioa_manager import fm
import time
from modules import ws2812

# Define the GPIO pin numbers
button_io_number = 19
ws2812_io_number = 8  

# Register the button pin to be used as GPIO
fm.register(button_io_number, fm.fpioa.GPIOHS0)  # Use GPIOHS0 for the button

# Create a GPIO instance for the button and set it as an input with a pull-up resistor
button = GPIO(GPIO.GPIOHS0, GPIO.IN, GPIO.PULL_UP)

# Initialize WS2812 LED
fm.register(ws2812_io_number)
class_ws2812 = ws2812(ws2812_io_number, 1)  # Assuming you have 1 LED

def turn_on_led():
    # Set all LEDs to red, for example
    for j in range(100):
        class_ws2812.set_led(j, (255, 0, 0))
    class_ws2812.display()

def turn_off_led():
    # Turn off all LEDs
    for j in range(100):
        class_ws2812.set_led(j, (0, 0, 0))
    class_ws2812.display()

# Main loop
while True:
    button_state = button.value()
    if button_state == 0:  #when pressed
        print("Button Pressed")
        turn_on_led()
        time.sleep(0.1)  # Delay for 100 milliseconds when the button is pressed
    else:
        turn_off_led()
        time.sleep(0.1)   
