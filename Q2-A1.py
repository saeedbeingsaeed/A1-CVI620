import cv2
import numpy as np

# a. Brightness and Contrast Adjustments

# i. Load the first image
img1 = cv2.imread(r"C:\Users\Saeed Bafana\OneDrive\Desktop\snapshots\image1.jpg")
cv2.imshow("Original Image", img1)

# ii. Increase brightness by adding a constant (150) to all pixel values
brightness = 150  
bright_img = cv2.add(img1, (brightness, brightness, brightness, 0))
cv2.imshow("Increased Brightness", bright_img)

# iii. Adjust contrast by multiplying pixel values by a scaling factor (0.5)
contrast = 0.5  
contrast_img = cv2.convertScaleAbs(img1, alpha=contrast, beta=0)
cv2.imshow("Changed Contrast", contrast_img)

# Wait for key press before proceeding
cv2.waitKey(0)

# b. Linear Blending

# i. Load the second image
img2 = cv2.imread(r"C:\Users\Saeed Bafana\OneDrive\Desktop\snapshots\image2.jpg")
cv2.imshow("Second Image", img2)

# ii. Resize the second image to match the first image's dimensions
img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
cv2.imshow("Resized Second Image", img2_resized)

# iii. Perform linear blending with user-defined alpha value
alpha = float(input("Enter alpha value between 0 and 1: "))  
blend_img = cv2.addWeighted(img1, 1 - alpha, img2_resized, alpha, 0)
cv2.imshow("Linear Blend Result", blend_img)

cv2.waitKey(0)
cv2.destroyAllWindows()