import cv2


def extract_roi(frame, rect):
    """
    Extrait une ROI à partir d'un rectangle (x, y, w, h)
    avec clamp sécurité.
    """
    x, y, w, h = rect
    h_frame, w_frame, _ = frame.shape

    x = max(0, x)
    y = max(0, y)
    w = min(w, w_frame - x)
    h = min(h, h_frame - y)

    return frame[y:y+h, x:x+w]

def compute_card_and_title_roi(frame_shape):
    """
    Retourne :
    - rectangle carte (x, y, w, h)
    - rectangle titre (x, y, w, h)
    """
    height, width, _ = frame_shape

    # Zone carte (centrée)
    card_w = int(width * 0.5)
    card_h = int(height * 0.75)
    card_x = (width - card_w) // 2
    card_y = (height - card_h) // 2

    # Zone titre (en haut de la carte)
    title_h = int(card_h * 0.12)
    title_x = card_x + int(card_w * 0.05)
    title_y = card_y + int(card_h * 0.04)
    title_w = int(card_w * 0.9)

    card_rect = (card_x, card_y, card_w, card_h)
    title_rect = (title_x, title_y, title_w, title_h)

    return card_rect, title_rect
