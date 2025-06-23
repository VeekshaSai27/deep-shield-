Data Security and Image Monitoring System

This project is a Data Security System designed to protect sensitive information embedded in images, using a combination of steganography, cloud monitoring, IP tracking, and email alerts. The main idea behind the project is to use images as secure carriers of hidden information and track any unauthorized changes or access.

The core feature of the system is steganography, which is used to embed a secret code or watermark into an image. This code is invisible to the naked eye and does not affect the visual quality of the image. Once the image is embedded with this hidden data, it is uploaded to a cloud storage service like Google Photos or iCloud.

If someone later tries to alter the image—whether through deepfake, compression, or tampering—the hidden code is either changed or lost. The system periodically or upon request extracts the code from the stored image and compares it with the original. If a mismatch is detected, it acts as a clear sign that the image has been compromised.

To enhance the security layer, the system includes IP tracking and geolocation monitoring using a tiny 1x1 pixel beacon. This invisible pixel logs the IP address and location of the person accessing the image. If an unknown or suspicious location is detected, it helps identify potential misuse.

The final feature is a real-time email alert system, implemented using SendGrid. If any tampering is detected or the image is accessed from an untrusted source, the user receives an immediate email notification with the details—such as the time, IP address, and location of access.

Key Features:

->  Secret data embedding using steganography

->  Cloud image monitoring for tampering detection

->  Mismatch detection between original and altered images

->  1x1 pixel tracking for IP and geolocation logging

->  Automated email alerts via SendGrid for security breaches

This project combines data security, image processing, and network tracking in a creative way to demonstrate how modern threats like image manipulation can be addressed with proactive, intelligent systems.
