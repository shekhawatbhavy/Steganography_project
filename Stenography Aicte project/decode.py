import cv2

# Load the encrypted image
img = cv2.imread("encryptedImage.png")

if img is None:
    print("Error: Encrypted image not found!")
    exit()

# Retrieve stored password and message lengths
password_length = img[0, 0, 0]
msg_length = img[0, 0, 1]

# Retrieve stored password
stored_password = ""
n, m, z = 0, 1, 0  # Start at (0,1)
for _ in range(password_length):
    stored_password += chr(img[n, m, z])
    m += 1
    if m >= img.shape[1]:  # Move to next row if needed
        m = 0
        n += 1
    z = (z + 1) % 3  # Cycle through RGB channels

# Ask for password input
user_password = input("Enter passcode for Decryption: ")

if user_password != stored_password:
    print("YOU ARE NOT AUTHORIZED!")
    exit()

# Decode the message
message = ""
for _ in range(msg_length):
    message += chr(img[n, m, z])
    m += 1
    if m >= img.shape[1]:  # Move to next row if needed
        m = 0
        n += 1
    z = (z + 1) % 3  # Cycle through RGB channels

print("Decryption successful!")
print("Hidden Message:", message)