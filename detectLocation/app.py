from flask import Flask, send_file, request
import datetime
import requests
from senddata import send_email_alert  # ✅ Correct import (remove quotes)

app = Flask(__name__)

@app.route('/tracker/<photo_id>.png')
def tracker(photo_id):
    ip_address = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.datetime.utcnow()

    # 🌍 Use IP Geolocation API
    geo_info = {}
    try:
        geo_response = requests.get(f"http://ip-api.com/json/{ip_address}").json()
        geo_info = {
            "city": geo_response.get("city"),
            "region": geo_response.get("regionName"),
            "country": geo_response.get("country"),
            "lat": geo_response.get("lat"),
            "lon": geo_response.get("lon"),
            "isp": geo_response.get("isp")
        }
    except:
        geo_info = {"error": "Could not retrieve location"}

    # 📝 Log info
    print(f"\n🔍 Download Detected")
    print(f"Photo ID: {photo_id}")
    print(f"IP: {ip_address}")
    print(f"Location: {geo_info}")
    print(f"User-Agent: {user_agent}")
    print(f"Timestamp: {timestamp}")

    # ✅ Trigger email alert to the photo owner
    send_email_alert(photo_id, geo_info)

    # 🖼️ Return invisible tracking pixel
    return send_file("pixel.png", mimetype="image/png")

if __name__ == '__main__':
    app.run(debug=True)
