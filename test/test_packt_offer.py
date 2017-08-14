from nose.tools import *
from packt_offer import *
from bs4 import BeautifulSoup


class TestPacktOffer:
    def setUp(self):
        self.proper_soup = BeautifulSoup(
            """"
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
        </div>""", "html.parser")
        for linebreak in self.proper_soup.find_all('br'):
            linebreak.extract()

        self.improper_soup = BeautifulSoup("""
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
        </div>""", "html.parser")

        for linebreak in self.improper_soup.find_all('br'):
            linebreak.extract()

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

    def test_offer_title_extracter_no_content(self):
        result = offer_title_extracter(self.improper_soup)
        assert_equals(result, '')

    def test_offer_description_extracter_proper(self):
        result = offer_description_extracter(self.proper_soup)
        assert_equals(result, """<div>
                            An example description of book offered by Packtpub.
                            <ul>
<li>First reason why you should read this book.</li>
<li>Second reason why you should read this book.</li>
</ul>
</div>
""")

    def test_offer_description_extracter_no_content(self):
        result = offer_description_extracter(self.improper_soup)
        assert_equals(result, '')

    def test_message_creator_all_proper(self):
        msg = message_creator(b'000000', 'www.image.com/image.jpg', 'Offer title', 'Offer description',
                              'sender@mail.com', ['receiver@mail.com'])
        assert_in(
            """\
MIME-Version: 1.0
Subject: Packt offer: Offer title
From: sender@mail.com
To: receiver@mail.com

This is a multi-part message in MIME format.""", msg)

        assert_in(
            """\
            <div><h2>New Packtpub offer:</h2></div>
            </br>
            <div>
                <img src="cid:image1">
            </div>
            <div><h2>Offer title</h2></div>
            </br>
            <div>Offer description</div>
            </br>
            <a href="https://www.packtpub.com/packt/offers/free-learning">Get it!</a>""", msg)

        assert_in(
            """\
Content-Type: image/jpeg
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Content-ID: <image1>
Content-Disposition: inline; filename="www.image.com/image.jpg"\
""", msg)

    @raises(AttributeError)
    def test_message_creator_wrong_image_url(self):
        msg = message_creator(b'000000', 'www.image.com', 'Offer title', 'Offer description',
                              'sender@mail.com', ['receiver@mail.com'])
