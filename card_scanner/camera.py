import cv2


class CameraManager:
    def __init__(self, camera_index=0, window_name="Camera"):
        self.camera_index = camera_index
        self.window_name = window_name
        self.cap = None
        self.running = False

    def start(self):
        """Initialise la caméra"""
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise RuntimeError("Impossible d'accéder à la caméra")

        self.running = True
        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)

    def read_frame(self):
        """Lit une frame depuis la caméra"""
        if not self.running:
            return None

        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Erreur lors de la lecture de la caméra")

        return frame

    def show_frame(self, frame):
        """Affiche une frame"""
        cv2.imshow(self.window_name, frame)

    def stop(self):
        """Libère les ressources"""
        self.running = False
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
