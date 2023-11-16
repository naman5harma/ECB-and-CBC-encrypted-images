from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from PIL import Image

def encrypt_ecb(key, plaintext):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

def decrypt_ecb(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    return unpad(decrypted, AES.block_size)

# Load image
image_path = "image1.png"  # Replace with your image path
img = Image.open(image_path)
img_bytes = img.tobytes()

# AES key
key = get_random_bytes(16)  # 16 bytes key for AES-128

# Encrypt using ECB mode
encrypted_ecb = encrypt_ecb(key, img_bytes)

# Save encrypted image as PNG
encrypted_img = Image.frombytes(img.mode, img.size, encrypted_ecb)
encrypted_img.save("encrypted_ecb_image.png")

# Decrypt the encrypted image for comparison
decrypted_ecb = decrypt_ecb(key, encrypted_ecb)

# Save decrypted image for comparison
decrypted_img = Image.frombytes(img.mode, img.size, decrypted_ecb)
decrypted_img.save("decrypted_ecb_image.png")
