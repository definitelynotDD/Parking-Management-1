import cv2
import pytesseract

def scan_vehicle_number(img):
    try:
        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Use Tesseract OCR to extract text from the image
        vehicle_number = pytesseract.image_to_string(gray, config='--psm 6')
        
        return vehicle_number.strip()  # Remove leading/trailing whitespace
    except Exception as e:
        print("An error occurred:", str(e))
        return None
"C:\\Users\dell\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract"