import cv2

# Load an image
img = cv2.imread(r'C:\Users\Saeed Bafana\OneDrive\Desktop\snapshots\image1.jpg')

# 1.1 Draw a Green Rectangle with Thickness = 4
top_left = (50, 50)
bottom_right = (300, 300)
color = (0, 255, 0)  # Green color in BGR format
thickness = 4

img_with_rectangle = img.copy()
cv2.rectangle(img_with_rectangle, top_left, bottom_right, color, thickness)
cv2.imshow("Rectangle with Thickness 4", img_with_rectangle)

# 1.2 Change Thickness to -1 (Filled Rectangle)
thickness_filled = -1

img_with_filled_rectangle = img.copy()
cv2.rectangle(img_with_filled_rectangle, top_left, bottom_right, color, thickness_filled)
cv2.imshow("Rectangle with Filled Thickness", img_with_filled_rectangle)

# 1.3 Add Text to the Rectangle
font = cv2.FONT_HERSHEY_SIMPLEX
text = "Meow"
position = (100, 150)
font_scale = 1
font_color = (255, 255, 255)  # Change color here, currently white
font_thickness = 2

img_with_text = img.copy()
cv2.rectangle(img_with_text, top_left, bottom_right, color, thickness)
cv2.putText(img_with_text, text, position, font, font_scale, font_color, font_thickness, cv2.LINE_AA)
cv2.imshow("Rectangle with Text", img_with_text)

cv2.waitKey(0)
cv2.destroyAllWindows()