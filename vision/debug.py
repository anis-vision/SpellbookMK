import cv2


def show_roi(name, roi):
    """
    Affiche une ROI dans une fenêtre dédiée
    """
    if roi is None or roi.size == 0:
        return

    cv2.imshow(name, roi)
