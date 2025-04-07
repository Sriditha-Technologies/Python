import cv2
# Load an image (make sure to use the correct path)
img = cv2.imread("D:\\Desktop\\photos\\1.jpg",1)
# Resize the image
resized_image = cv2.resize(img, (600, 600))  # Correct usage with a tuple (width, height)
# Display the resized image
cv2.imshow("Resized Image", resized_image)
# Wait indefinitely for a key press
cv2.waitKey(2000)
# Destroy all windows after the key press
cv2.destroyAllWindows()