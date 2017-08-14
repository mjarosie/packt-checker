from nose.tools import assert_equals
from check_packt import parse_args
import config as cfg


class TestParser:
    def test_parse_args_all_default_arguments(self):
        args = parse_args()
        assert_equals(args.sender, cfg.sender)
        assert_equals(args.recipients, cfg.recipients)
        assert_equals(args.url, cfg.url)

    def test_parse_args_wrong_arguments(self):
        args = parse_args(['-l', '-m'])
        assert_equals(args.sender, cfg.sender)
        assert_equals(args.recipients, cfg.recipients)
        assert_equals(args.url, cfg.url)

    def test_parse_args_sender_specified(self):
        args = parse_args(['-s', 'sender@mail.com'])
        assert_equals(args.sender, 'sender@mail.com')
        assert_equals(args.recipients, cfg.recipients)
        assert_equals(args.url, cfg.url)

    def test_parse_args_one_recipient_specified(self):
        args = parse_args(['-r', 'recipient1@mail.com'])
        assert_equals(args.sender, cfg.sender)
        assert_equals(args.recipients, ['recipient1@mail.com'])
        assert_equals(args.url, cfg.url)

    def test_parse_args_multiple_recipients_specified(self):
        args = parse_args(['-r', 'recipient1@mail.com', '-r', 'recipient2@mail.com'])
        assert_equals(args.sender, cfg.sender)
        assert_equals(args.recipients, ['recipient1@mail.com', 'recipient2@mail.com'])
        assert_equals(args.url, cfg.url)