import time
import seeed_dht
from gpiozero import LED

# Setup pins for the LEDs
led_blue = LED(24)  # Blue LED
led_green = LED(5)  # Green LED
led_red = LED(16)   # Red LED

def main():
    # Initialize the sensor (DHT11/DHT22)
    sensor = seeed_dht.DHT("11", 22)
    
    while True:
        try:
            # Read values from the sensor
            humidity, temperature = sensor.read()
            
            if humidity is not None and temperature is not None:
                print(f'DHT{sensor.dht_type}, humidity {humidity:.1f}, temperature {temperature:.1f}C')
                
                # Control LEDs based on the temperature
                if temperature <= 17:
                    led_blue.on()
                    led_green.off()
                    led_red.off()
                    print("Blue LED ON (Temperature <= 17C)")
                elif 18 <= temperature <= 21:
                    led_blue.off()
                    led_green.on()
                    led_red.off()
                    print("Green LED ON (Temperature between 18C and 21C)")
                elif temperature >= 22:
                    led_blue.off()
                    led_green.off()
                    led_red.on()
                    print("Red LED ON (Temperature >= 22)")
            else:
                print(f'DHT{sensor.dht_type}, failed to read data')
                # Turn off all LEDs in case of read error
                led_blue.off()
                led_green.off()
                led_red.off()
        except Exception as e:
            # Handle exceptions
            print(f"Error: {e}")
            # Turn off all LEDs in case of an exception
            led_blue.off()
            led_green.off()
            led_red.off()
        
        # Delay between measurements
        time.sleep(1)

if __name__ == '__main__':
    main()
