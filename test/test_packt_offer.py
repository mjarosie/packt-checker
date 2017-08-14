from nose.tools import assert_equals
from packt_offer import *


class TestPacktOffer:
    def setUp(self):
        self.proper_soup = """
        <div id="deal-of-the-day" class="cf">
            <div class="dotd-main-book cf">
                <div class="section-inner">
                    <div class="dotd-main-book-image float-left">
                        <a href="/application-development/github-essentials">
                            <noscript><img src="//serv.cloudfront.net/sites/imagecache/9781783553716.png" class="bookimage imagecache imagecache-dotd_main_image" itemprop="url"/>
                            </noscript><img src="//serv.cloudfront.net/sites/imagecache/9781783553716.png" data-original="//d1ldz4te4covpm.cloudfront.net/sites/default/files/imagecache/dotd_main_image/9781783553716.png" class="bookimage imagecache imagecache-dotd_main_image" itemprop="url" style="opacity: 1;">						
                        </a>
                    </div>
                    <div class="dotd-main-book-summary float-left">
                        <div class="dotd-title">
                            <h2>Example title</h2>
                        </div>
                        <br>
                        <div>
                            An example description of book offered by Packtpub.
                            <ul>
                                <li>First reason why you should read this book.</li>
                                <li>Second reason why you should read this book.</li>
                            </ul>
                        </div>
                        <div class="dotd-main-book-form cf">
                            <div class="dots-main-book-price float-left"></div>
                            <div class="float-left free-ebook"></div>
                        </div>
                    </div>
        
                </div>
            </div>
        </div>"""

        self.improper_soup = """
        <div id="deal-of-the-day" class="cf">
            <div class="dotd-main-book cf">
                <div class="section-inner">
                    <div class="dotd-main-book-summary float-left">
                        <div class="dotd-title">
                        </div>
                        <br>
                    </div>

                </div>
            </div>
        </div>"""


    def test_offer_image_url_extracter_proper(self):
        result = offer_image_url_extracter(self.proper_soup)
        assert_equals(result,
                      'http://serv.cloudfront.net/sites/imagecache/9781783553716.png')

    def test_offer_image_url_extracter_no_content(self):
        """Case when <div> with a given image class is not present in a given page."""
        result = offer_image_url_extracter(self.improper_soup)
        assert_equals(result, '')

    def test_offer_title_extracter_proper(self):
        result = offer_title_extracter(self.proper_soup)
        assert_equals(result, 'Example title')

    def test_offer_title_extracter_proper_no_content(self):
        result = offer_title_extracter(self.improper_soup)
        assert_equals(result, '')

    def test_offer_description_extracter_proper(self):
        result = offer_description_extracter(self.proper_soup)
        assert_equals(result, "An example description of book offered by Packtpub.\n<ul>\n"
                              "<li>First reason why you should read this book.</li>\n"
                              "<li>Second reason why you should read this book.</li>\n</ul>")

    def test_offer_description_extracter_no_content(self):
        result = offer_description_extracter(self.improper_soup)
        assert_equals(result, '')

    def test_message_creator_:

    def test_extract_url(self):
        offer.extract_image_url()
        args = parse_args()
        assert_equals(args.sender, cfg.sender)
        assert_equals(args.recipients, cfg.recipients)
        assert_equals(args.url, cfg.url)
