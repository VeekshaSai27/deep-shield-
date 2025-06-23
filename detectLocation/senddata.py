from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_email_alert(photo_id, geo_info):
    try:
        message = Mail(
            from_email="23f3002244@ds.study.iitm.ac.in",  # 🔁 Replace with verified sender
            to_emails="veeksha.sai05@gmail.com",    # 🔁 Replace with actual recipient
            subject='🔒 Photo Access Detected',
            plain_text_content=f"""
            Your photo (ID: {photo_id}) was accessed.
            
            Geo Info:
            City: {geo_info.get('city')}
            Region: {geo_info.get('region')}
            Country: {geo_info.get('country')}
            ISP: {geo_info.get('isp')}
            Coordinates: ({geo_info.get('lat')}, {geo_info.get('lon')})
            """
        )

        sg = SendGridAPIClient("YOUR_REAL_SENDGRID_API_KEY")
        response = sg.send(message)

        print(f"✅ Email sent! Status Code: {response.status_code}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")


#"23f3002244@ds.study.iitm.ac.in"
#"veeksha.sai05@gmail.com"