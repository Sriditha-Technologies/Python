import cv2

# Load the Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load an image (make sure to use the correct path)
img = cv2.imread(r"D:\Desktop\photos\1.jpg")  # Replace with your image path
if img is None:
    print("Image not found.")
else:
    # Convert the image to grayscale (Haar cascade works on grayscale images)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform face detection
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

    print(type(faces))
    print(faces)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw rectangle with blue color


    # Display the resulting image with detected faces
    cv2.imshow("Detected Faces", img)
    
    # Wait indefinitely for a key press
    cv2.waitKey(0)
    
    # Destroy all windows after the key press
    cv2.destroyAllWindows()