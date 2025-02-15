import cv2
import os
import numpy as np

# Load image
img = cv2.imread("mypic.jpg")  # Ensure this file exists

if img is None:
    print("Error: Image not found!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Convert message and password into ASCII values
msg_ascii = [ord(c) for c in msg]
password_ascii = [ord(c) for c in password]

msg_length = len(msg_ascii)
password_length = len(password_ascii)

if password_length > 255:
    print("Error: Password too long!")
    exit()

# Store password length at (0,0,0) and message length at (0,0,1)
img[0, 0, 0] = password_length
img[0, 0, 1] = msg_length

# Store password in the next pixels
n, m, z = 0, 1, 0  # Start at (0,1)
for value in password_ascii:
    img[n, m, z] = value
    m += 1
    if m >= img.shape[1]:  # Move to next row if needed
        m = 0
        n += 1
    z = (z + 1) % 3  # Cycle through RGB channels

# Store message after password
for value in msg_ascii:
    img[n, m, z] = value
    m += 1
    if m >= img.shape[1]:  # Move to next row if needed
        m = 0
        n += 1
    z = (z + 1) % 3  # Cycle through RGB channels

# Save the encoded image
cv2.imwrite("encryptedImage.png", img)
print("Message successfully encoded in 'encryptedImage.png'!")
os.system("start encryptedImage.png")