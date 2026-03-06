import cv2


def draw_card_guide(frame, card_rect, title_rect):
    """
    Dessine la zone carte et la zone titre (OCR)
    """
    # Zone carte (vert)
    x, y, w, h = card_rect
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(frame, "Place la carte ici",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6, (0, 255, 0), 2)

    # Zone titre (bleu)
    tx, ty, tw, th = title_rect
    cv2.rectangle(frame, (tx, ty), (tx + tw, ty + th), (255, 0, 0), 2)
    cv2.putText(frame, "Zone OCR (Titre)",
                (tx, ty - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5, (255, 0, 0), 1)

