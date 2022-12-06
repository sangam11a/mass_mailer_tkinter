import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(sender_email,password,body,subject,receiver_email,logo_path):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "html"))

    filename = "new.html"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()
    
    fp = open(logo_path, 'rb') #Read image 
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<image1>')
    message.attach(msgImage)
    # Log in to server using secure context and send email
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
    except Exception as e:
        print("Error in connection ",e)
if __name__ == "__main__":
    body12='''
        <html>
	<head>
		<style>@import url('https://fonts.googleapis.com/css?family=Oxygen');</style>
	</head>
	<body>
	<section>Sir,</section><section>We lkjhlsa llaskjdlkasjdas ldjasldkjaslkd jaslkdj salkdj laksjdlksajdlksajdlksajdlksajdlksa djas ld.We lkjhlsa llaskjdlkasjdas ldjasldkjaslkd jaslkdj salkdj laksjdlksajdlksajdlksajdlksajdlksa djas ld.We lkjhlsa llaskjdlkasjdas ldjasldkjaslkd jaslkdj salkdj laksjdlksajdlksajdlksajdlksajdlksa djas ld<br>
  qywieyqweywq ewq kjhdkjsa hdkjhasdkjash djsadjkakmsnzmx,bcmzxbc.<br>
 ouasdousadoas oidusadm nd,msan dkjas hdasndasdsaj kd.ouasdousadoas oidusadm nd,msan dkjas hdasndasdsaj kd.ouasdousadoas oidusadm nd,msan dkjas hdasndasdsaj kd.ouasdousadoas oidusadm nd,msan dkjas hdasndasdsaj kd.ouasdousadoas oidusadm nd,msan dkjas hdasndasdsaj kd.ouasdousadoas oidusadm nd,msan dkjas hdasndasdsaj kd.</section><section>Thank you!</section>
	
	<section>
	  <table style="width:100%;background:whitesmoke;height: 213px; padding-top:33px; padding-right:0; padding-bottom:38px; padding-left:10px; font-family: 'Oxygen', sans-serif; font-size: 12px">
		<tbody>
		<tr>
			<td style="width:110px; padding:0;">
			<img src="cid:image1"  style="width:92px;height:92px;border-radius:50%;  padding-right: 20px; opacity: 0.8">
			<br>
			<br>
			<a href="http://google.com"><img src="https://mleewise.com/assets/img/facebook32px.png" width=16px alt="Facebook Link" style="padding-left:14px;"></a>
			<a href="http://google.com"><img src="https://mleewise.com/assets/img/linkedin32px.png" width=16px alt="LinkedIn Link"></a>
			<a href="http://google.com"><img src="https://mleewise.com/assets/img/twitter32px.png" width=16px alt="Twitter Link"></a>
			
			</td>
			<td style="border-left: 2px solid #f1451e; width:22px; height:136px; padding: 0px; opacity:0.8"></td>
			<td style="padding:0px">
			
			<div style="font-size:26px;font-weight:700;">Sangam Thapa</div>
			<br style="line-height:10px">
			<a href="tel:9860865421" style="font-size:18px;text-decoration:none; color:black;"><img src="https://www.mleewise.com/assets/img/telephone32px.png"  height=10px alt="Orange Phone Icon">9860865421</a>
			<br>
			<a href="mailto:sangam@gmail.com" style="font-size:18px;text-decoration:none; color:black;"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNFH-wlpKR5lZPPkAKiOqhaiRYfR0L_gHTtzkIzZRl&s" width=16px alt="Twitter Link">sangam@gmail.com</a>
			<br>
			<a href="http://google.com" style="font-size:18px;text-decoration:none; color:black;"><img src="https://www.mleewise.com/assets/img/linkthickflip32px.png"  height=12px alt="Orange Link Icon"> http://google.com</a>
			<br><br style="line-height:30px">
			<!--a href="http://google.com"><img src="cid:logo" alt="The logo for 'Primary Theory'" style="width:158px;height:140px;"></a-->
			
			</td>
		 </tr>
		</tbody>
	</table>
	</section>
	
	</body>
	</html>

    '''
    print(body12)
    send_email("sangam.thapa218@gmail.com","bxtnjckdlnbihpva",body12,"Subject","sangam.thapa218@gmail.com","C:/Users/nikes/Downloads/logo.jpg")