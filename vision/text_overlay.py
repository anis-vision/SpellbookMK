import cv2


def draw_text_above_card(
    frame,
    text,
    card_rect,
    padding=8,
    font_scale=0.9,
    thickness=2
):
    """
    Affiche un texte lisible au-dessus de la carte
    """
    if not text:
        return

    x, y, w, h = card_rect

    font = cv2.FONT_HERSHEY_SIMPLEX
    (text_w, text_h), baseline = cv2.getTextSize(
        text, font, font_scale, thickness
    )

    # Position du texte
    text_x = x + (w - text_w) // 2
    text_y = max(10, y - padding)

    # Rectangle de fond
    bg_x1 = text_x - padding
    bg_y1 = text_y - text_h - padding
    bg_x2 = text_x + text_w + padding
    bg_y2 = text_y + baseline + padding

    # Clamp sécurité
    bg_y1 = max(0, bg_y1)

    # Fond semi-opaque
    overlay = frame.copy()
    cv2.rectangle(
        overlay,
        (bg_x1, bg_y1),
        (bg_x2, bg_y2),
        (0, 0, 0),
        -1
    )

    alpha = 0.6
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    # Texte
    cv2.putText(
        frame,
        text,
        (text_x, text_y),
        font,
        font_scale,
        (0, 255, 0),
        thickness,
        cv2.LINE_AA
    )
