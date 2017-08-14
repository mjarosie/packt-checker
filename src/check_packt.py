import urllib.request
from argparse import ArgumentParser
from bs4 import BeautifulSoup

import sys
import config as cfg
from message import create_email, send_email
from offer import create_offer


def main():
    if cfg.INFO:
        print('Started script with parameters: ' + '; '.join(sys.argv[1:]))
    args = parse_args()
    if cfg.INFO:
        print('Sender: ' + args.sender)
        print('List of recipients: ' + ', '.join(args.recipients))
        print('URL: ' + args.url)
    soup = prepare_soup(args.url)
    offer = create_offer(soup)
    email = create_email(offer, args.sender, args.recipients)
    send_email(email, args.recipients)


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


def prepare_soup(url):
    r = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(r, 'html.parser')
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
