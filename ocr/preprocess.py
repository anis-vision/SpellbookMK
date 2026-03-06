import cv2


def preprocess_for_ocr(roi):
    """
    Prépare une image pour l'OCR du titre Magic
    """
    # Gris
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Augmentation contraste
    gray = cv2.normalize(gray, None, alpha=0, beta=255,
                          norm_type=cv2.NORM_MINMAX)

    # Lissage léger
    blur = cv2.GaussianBlur(gray, (3, 3), 0)

    # Threshold adaptatif
    thresh = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        31,
        5
    )

    return thresh
