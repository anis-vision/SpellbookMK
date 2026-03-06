import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import re


class OCREngine:
    def __init__(self):
        self.config = (
            "--oem 3 "
            "--psm 7 "
            "-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-' "
        )

    def recognize(self, image):
        """
        Retourne le texte OCR nettoyé
        """
        raw_text = pytesseract.image_to_string(image, config=self.config)

        return self._clean_text(raw_text)

    def _clean_text(self, text):
        text = text.strip()
        text = re.sub(r"[^A-Za-z'\- ]", "", text)
        text = re.sub(r"\s+", " ", text)
        return text

