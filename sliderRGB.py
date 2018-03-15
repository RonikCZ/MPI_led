import RPi.GPIO as GPIO
import time

dotTime = 0.25
dashTime = 0.5

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

CODE = {' ': ' ', 
        "'": '.----.', 
        '(': '-.--.-', 
        ')': '-.--.-', 
        ',': '--..--', 
        '-': '-....-', 
        '.': '.-.-.-', 
        '/': '-..-.', 
        '0': '-----', 
        '1': '.----', 
        '2': '..---', 
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...', 
        '8': '---..', 
        '9': '----.', 
        ':': '---...', 
        ';': '-.-.-.', 
        '?': '..--..', 
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....', 
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.', 
        'Q': '--.-', 
        'R': '.-.', 
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-', 
        'Y': '-.--', 
        'Z': '--..', 
        '_': '..--.-'}

try:
 while True:
  string = input("Napis slovo")
  for character in string:
   morse = CODE[character.upper()]
   for morseCharacter in morse:
	if morseCharacter == '.':
	   GPIO.output(23,GPIO.HIGH)
	   time.sleep(dotTime)
       GPIO.output(23,GPIO.LOW)
	if morseCharacter == '.':
	   GPIO.output(23,GPIO.HIGH)
	   time.sleep(dashTime)
       GPIO.output(23,GPIO.LOW)
  
except KeyboardInterrupt:
 GPIO.output(23,GPIO.LOW)
 GPIO.cleanup()
