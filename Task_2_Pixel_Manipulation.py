from PIL import Image
import random


def swap_pixels(pixels, width, height, key):
    random.seed(key)
    pixel_indices = [(i, j) for i in range(width) for j in range(height)]
    random.shuffle(pixel_indices)

    for index in range(0, len(pixel_indices), 2):
        if index + 1 < len(pixel_indices):
            (x1, y1), (x2, y2) = pixel_indices[index], pixel_indices[index + 1]
            pixels[x1, y1], pixels[x2, y2] = pixels[x2, y2], pixels[x1, y1]


def apply_math_operation(pixels, width, height, key):
    random.seed(key)
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256)


def encrypt_image(_image_path, key, output_path="encrypted_image.png"):
    img = Image.open(_image_path)
    img = img.convert('RGB')
    pixels = img.load()

    swap_pixels(pixels, img.width, img.height, key)
    apply_math_operation(pixels, img.width, img.height, key)

    img.save(output_path)
    print(f"Encrypted image saved as: {output_path}")


def decrypt_image(_image_path, key, output_path="decrypted_image.png"):
    img = Image.open(_image_path)
    img = img.convert('RGB')
    pixels = img.load()

    apply_math_operation(pixels, img.width, img.height, -key)
    swap_pixels(pixels, img.width, img.height, key)

    img.save(output_path)
    print(f"Decrypted image saved as {output_path}")


image_path = input("Enter path of your Image here:  ")
encryption_key = int(input("Enter your desired key in Numbers only:  "))
encrypt_image(image_path, encryption_key)
decrypt_image("encrypted_image.png", encryption_key)
