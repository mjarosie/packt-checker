import mimetypes
import urllib.request
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText


def offer_image_url_extracter(soup):
    """Returns URL of an image of a given offer."""
    tag = soup.find(class_='bookimage')
    return 'http:' + tag['src']


def offer_title_extracter(soup):
    """Returns a title of a given offer."""
    tag = soup.find(class_='dotd-title')
    title = str.strip(tag.h2.string)
    return title


def offer_description_extracter(soup):
    """Returns a description of a given offer."""
    tag = soup.find(class_='dotd-title')
    # Go to the next <div> - this is where the description is.
    tag = _get_next_tag(tag)

    # Description of the book is placed within classless <div> tags,
    # between <div class="dotd-title"> and <div class="dotd-main-book-form cf">
    description = ''
    while 'class' not in tag.attrs or 'dotd-main-book-form' not in tag['class']:
        description = description + str.strip(tag.get_text()) + '\n'
        # Find the next <div> tag.
        tag = _get_next_tag(tag)

    return description


def message_creator(img_url, image_getter, title, description, sender, recipients):
    msg_root = MIMEMultipart()
    msg_root['Subject'] = 'Packt offer: ' + title
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

    ctype, encoding = mimetypes.guess_type(image_url)
    maintype, subtype = ctype.split('/', 1)
    with image_getter(img_url) as img:
        msg_img = MIMEImage(img.read(), _subtype=subtype)
        msg_img.add_header('Content-ID', '<image1>')
        msg_img.add_header('Content-Disposition', 'inline', filename=image_url)
    # Set the filename parameter

    msg_root.attach(msg_html)
    msg_root.attach(msg_img)
    return msg_root.as_string()


def image_getter(url):
    """Returns a file-like object of the given image."""
    return urllib.request.urlopen(url).read()


def _get_next_tag(tag):
    """Helper function that returns the next HTML tag."""
    for sibling in tag.next_siblings:
        if sibling == '\n':
            continue
        tag = sibling
        break
    return tag
