import mimetypes
import smtplib
import urllib.request
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import config as cfg


def create_email(offer, sender, recipients):
    """Creates a message based on the content of offer dict passed as an argument."""
    try:
        image_url = offer['image_url']
        title = offer['title']
        description = offer['desc']
    except KeyError:
        print('Invalid dictionary provided')
        return

    msg_root = MIMEMultipart()
    msg_root['Subject'] = 'Packt offer: ' + offer['title']
    msg_root['From'] = sender
    msg_root['To'] = ', '.join(recipients)
    msg_root.preamble = 'This is a multi-part message in MIME format.'

    # Create the body of the message.
    html = """\
        <div><h2>New Packtpub offer:</h2></div>
        </br>
        <div>
            <img src="cid:image1">
        </div>
        <div><h2>{title}</h2></div>
        </br>
        <div>{description}</div>
        </br>
        <a href="{url}">Get it!</a>
    """.format(title=title, description=description, url=cfg.url)

    # Record the MIME types.
    msg_html = MIMEText(html, 'html')
    # image = urllib.request.urlopen(image_url).read()

    ctype, encoding = mimetypes.guess_type(image_url)
    maintype, subtype = ctype.split('/', 1)
    with urllib.request.urlopen(image_url) as fp:
        msg_img = MIMEImage(fp.read(), _subtype=subtype)
        msg_img.add_header('Content-ID', '<image1>')
        msg_img.add_header('Content-Disposition', 'inline', filename=image_url)
    # Set the filename parameter

    msg_root.attach(msg_html)
    msg_root.attach(msg_img)
    return msg_root


def send_email(msg, destination):
    sender = msg['From']
    conn = smtplib.SMTP_SSL(cfg.SMTPserver, cfg.SMTPport)
    conn.ehlo()
    # conn.starttls()
    # conn.set_debuglevel(False)
    # conn.ehlo()
    conn.login(cfg.USERNAME, cfg.PASSWORD)
    conn.sendmail(sender, destination, msg.as_string())
    conn.quit()
