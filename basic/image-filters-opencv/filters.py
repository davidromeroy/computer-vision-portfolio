import cv2

def apply_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def apply_blur(img, ksize=(15, 15)):
    return cv2.GaussianBlur(img, ksize, 0)

def apply_canny(img, low=100, high=200):
    return cv2.Canny(img, low, high)

def apply_threshold(img, thresh=127):
    gray = apply_grayscale(img) if len(img.shape) == 3 else img
    _, result = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
    return result

def apply_laplacian(img):
    gray = apply_grayscale(img) if len(img.shape) == 3 else img
    return cv2.Laplacian(gray, cv2.CV_64F)

def apply_equalize_histogram(img):
    gray = apply_grayscale(img) if len(img.shape) == 3 else img
    return cv2.equalizeHist(gray)
