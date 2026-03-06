import cv2

from card_scanner.camera import CameraManager
from vision.roi import compute_card_and_title_roi, extract_roi
from vision.overlay import draw_card_guide
from vision.debug import show_roi
from vision.text_overlay import draw_text_above_card
from ocr.preprocess import preprocess_for_ocr
from ocr.ocr_engine import OCREngine


def main():
    camera = CameraManager()
    ocr = OCREngine()

    try:
        camera.start()

        while True:
            # 1. Capture frame
            frame = camera.read_frame()

            # 2. Calcul des zones
            card_rect, title_rect = compute_card_and_title_roi(frame.shape)

            # 3. Dessin des guides utilisateur
            draw_card_guide(frame, card_rect, title_rect)

            # 4. Extraction de la ROI titre
            title_roi = extract_roi(frame, title_rect)

            # 5. Prétraitement OCR
            processed_roi = preprocess_for_ocr(title_roi)

            # 6. OCR
            recognized_text = ocr.recognize(processed_roi)

            # 7. Debug visuel
            show_roi("ROI Titre", title_roi)
            show_roi("ROI OCR", processed_roi)

            # 8. Affichage du texte au-dessus de la carte
            draw_text_above_card(
                frame=frame,
                text=recognized_text,
                card_rect=card_rect
            )

            # 9. Affichage principal
            camera.show_frame(frame)

            # Quitter avec 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        camera.stop()


if __name__ == "__main__":
    main()
