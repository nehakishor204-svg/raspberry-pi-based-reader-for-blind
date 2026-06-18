import cv2
import pytesseract
import pyttsx3
from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO


engine = pyttsx3.init()


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
camera = PiCamera()
camera.resolution = (640, 480)

def capture_image():
  
    camera.capture('captured_image.png')

def perform_ocr(image_path):
    
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)


    extracted_text = pytesseract.image_to_string(gray)

    return extracted_text

def speak_text(text):
    
    engine.say(text)
    engine.runAndWait()

def main():
    print("Press the button to capture an image for OCR")

    try:
        while True:
            
            input_state = GPIO.input(17)
            if input_state == GPIO.LOW: 
                print("Button pressed, capturing image...")
                capture_image()
                print("Image captured, performing OCR...")
                
                
                extracted_text = perform_ocr('captured_image.png')
                print(f"Recognized Text: {extracted_text}")
                
                
                speak_text(extracted_text)
                
                sleep(1)  
    except KeyboardInterrupt:
        print("Program terminated")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
