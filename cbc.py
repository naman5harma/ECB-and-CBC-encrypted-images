from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from PIL import Image

def encrypt_cbc(key, plaintext):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return iv + ciphertext

def decrypt_cbc(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext

# Load image
image_path = "image1.png"  # Replace with your image path
img = Image.open(image_path)
img_bytes = img.tobytes()

# AES key
key = get_random_bytes(16)  # 16 bytes key for AES-128

# Encrypt using CBC mode
encrypted_cbc = encrypt_cbc(key, img_bytes)

# Save encrypted image as PNG
encrypted_img_cbc = Image.frombytes('RGB', img.size, encrypted_cbc[AES.block_size:])
encrypted_img_cbc.save("encrypted_cbc_image.png")

# Decrypt the encrypted image for comparison
decrypted_cbc = decrypt_cbc(key, encrypted_cbc)

# Save decrypted image for comparison
decrypted_img = Image.frombytes('RGB', img.size, unpad(decrypted_cbc, AES.block_size))
decrypted_img.save("decrypted_cbc_image.png")
