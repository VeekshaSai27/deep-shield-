import base64
from PIL import Image
import io

# Step 1: Read original image as bytes
with open("secret.png", "rb") as img_file:
    original_bytes = img_file.read()

# Step 2: Encode to base64
encoded_str = base64.b64encode(original_bytes).decode("utf-8")

# ✅ Save base64 string to 'pixeldata.txt'
with open("pixeldata.txt", "w") as b64_file:
    b64_file.write(encoded_str)

# Step 3: Decode back to bytes
decoded_bytes = base64.b64decode(encoded_str)

# Step 4: Write the decoded image to a new file
with open("secret1.png", "wb") as out_file:
    out_file.write(decoded_bytes)

# Step 5: Compare pixels (optional check)
img1 = Image.open(io.BytesIO(original_bytes))
img2 = Image.open("secret1.png")

if list(img1.getdata()) == list(img2.getdata()):
    print("✅ Pixel values are preserved.")
else:
    print("❌ Pixel values are different.")



#when the image is sent from one place to another, compressions and decompressions take placeso instead we use 
#base64 method to convert the image into an txt file consisting of the bit values
#we then transport the bit values and then re code the values to get the image
# doing this, the image pixel values are preserved, hence the secret code embedded into the code.