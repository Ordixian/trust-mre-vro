import easyocr
import os
from typing import List

# Initialize the reader globally so it doesn't reload on every request
# 'en' tells it to look for English text (standard for Nigerian products)
reader = easyocr.Reader(['en'], gpu=False) 

def extract_label_text(image_path: str) -> str:
    """
    Takes the path to an uploaded image, processes it, 
    and returns all detected text as a single uppercase string.
    """
    try:
        if not os.path.exists(image_path):
            return ""

        # Perform OCR
        # detail=0 returns just the text strings without coordinates
        result = reader.readtext(image_path, detail=0)
        
        # Combine list into one string and clean up whitespace
        full_text = " ".join(result).strip().upper()
        
        return full_text
        
    except Exception as e:
        print(f"OCR Error: {str(e)}")
        return ""

def search_for_keywords(text: str, keywords: List[str]) -> dict:
    """
    Helper to check if specific keywords (like 'NAFDAC' or 'BATCH') 
    exist in the scanned text.
    """
    found_map = {}
    for word in keywords:
        found_map[word] = word.upper() in text
    return found_map