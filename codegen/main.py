from PIL import Image
from PIL.ExifTags import TAGS
import hashlib
import uuid
import io

def extract_metadata(image_path):
    """Extract metadata and timestamp from an image."""
    image = Image.open(image_path)
    exif_data = image._getexif() or {}
    metadata = {}

    for tag, value in exif_data.items():
        decoded = TAGS.get(tag, tag)
        metadata[decoded] = value

    timestamp = metadata.get("DateTime", "NoTimestamp")
    return metadata, timestamp

def hash_image_pixels(image_path):
    """Generate a SHA-256 hash from the image pixel data."""
    with Image.open(image_path) as img:
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')  # Convert image to bytes
        return hashlib.sha256(img_bytes.getvalue()).hexdigest()

def generate_unique_photo_id(image_path):
    """Generate a unique photo ID using metadata, timestamp, and pixel hash."""
    metadata, timestamp = extract_metadata(image_path)
    pixel_hash = hash_image_pixels(image_path)

    unique_string = f"{metadata}-{timestamp}-{pixel_hash}"
    return uuid.uuid5(uuid.NAMESPACE_DNS, unique_string).hex

def hash_image_pixels(image_path):
    """Generate a SHA-256 hash from the image pixel data."""
    with Image.open(image_path) as img:
        img_bytes = io.BytesIO()
        img.save(img_bytes, format='PNG')  # Convert image to bytes
        return hashlib.sha256(img_bytes.getvalue()).hexdigest()  # Hash image bytes



photo_id = generate_unique_photo_id("WIN_20250403_21_42_48_Pro.jpg")
print("Photo ID:", photo_id)
pixel_hash = hash_image_pixels("WIN_20250403_21_42_48_Pro.jpg")

print("Secret code:", pixel_hash)




#pip install pillow


#generates a secret code for the photo id 