from stegano import lsb
try:
#    secret = lsb.hide("photo.png", "the photo is not morphed")
#    secret.save("secret.png")

    secret_code = lsb.reveal("secret.png")
    
    if secret_code:
      print("Decoded message:", secret_code)
    else:
      print("No hidden message found.") 

except IndexError:
    print("The photo is morphed")
except FileNotFoundError:
    print("Error: Image file not found. Make sure file exists in the correct directory.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

#pip install stegano

#this code is used for the embedding of the secret code and extracting the secret code