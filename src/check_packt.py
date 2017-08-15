from argparse import ArgumentParser
from bs4 import BeautifulSoup
import sys
print('check_packt sys.path: ' + ';'.join(sys.path))
print('importing config')
import config as cfg
import packt_offer as offer
import message

if sys.version_info[0] < 3:
    import urllib as url_requester
else:
    import urllib.request as url_requester


def main():
    if cfg.INFO:
        print('Started script with parameters: ' + '; '.join(sys.argv[1:]))
    args = parse_args()
    if cfg.INFO:
        print('Sender: ' + args.sender)
        print('List of recipients: [' + ', '.join(args.recipients) + ']')
        print('URL: ' + args.url)

    # Prepare a page to be scraped.
    page_content = url_requester.urlopen(args.url).read()
    soup = get_page_soup(page_content)

    # Get offer parameters.
    offer_image_url = offer.offer_image_url_extracter(soup)
    offer_title = offer.offer_title_extracter(soup)
    offer_description = offer.offer_description_extracter(soup)

    if cfg.INFO:
        if offer_image_url != '':
            print('Offer image url: ' + offer_image_url)
        if offer_title != '':
            print('Offer title: ' + offer_title)
        if offer_description != '':
            print('Offer description: ' + offer_description)

    # Prepare a message to be send.
    image = offer.image_getter(offer_image_url)
    msg_to_be_send = offer.message_creator(image, offer_image_url, offer_title, offer_description, args.sender, args.recipients)

    # Send a message.
    message.send_message(msg_to_be_send, args.sender, args.recipients)


def parse_args(args=None):
    """Parses command line arguments, overrides the default behaviour of argparse which appends arguments to default value.

    :param args: List of command line arguments to parse (for ex. ['-s', 'sender@mail.com', '-r', 'recipient1@mail,com']
    :return: Namespace with fields defined while creating parser.
    """
    parser = create_parser()
    args, unknown = parser.parse_known_args(args)
    if len(args.recipients) == 0:
        args.recipients = cfg.recipients
    return args


def get_page_soup(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    for linebreak in soup.find_all('br'):
        linebreak.extract()
    return soup


def create_parser():
    parser = ArgumentParser(description="""\
        Check the Packtpub page for a free book offer and send its description by mail.
        Provide parameters unless they are put in the config.py file.
        """)
    parser.add_argument('-s', '--sender', default=cfg.sender,
                        help='The value of the From: header (if not provided - searched in config.py file)')
    parser.add_argument('-r', '--recipients',
                        action='append', metavar='RECIPIENT',
                        default=[],
                        help='The value of the To: header (if not provided - searched in config.py file)')
    parser.add_argument('-u', '--url', default=cfg.url,
                        help='The site under which script is supposed to look for a description of a free offer by packtpub.')
    return parser


if __name__ == '__main__':
    main()
