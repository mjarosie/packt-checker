import unittest
from check_packt import parse_args
import config as cfg


class TestParser(unittest.TestCase):
    def test_parse_args_all_default_arguments(self):
        args = parse_args()
        self.assertEqual(args.sender, cfg.sender)
        self.assertEqual(args.recipients, cfg.recipients)
        self.assertEqual(args.url, cfg.url)

    def test_parse_args_wrong_arguments(self):
        args = parse_args(['-l', '-m'])
        self.assertEqual(args.sender, cfg.sender)
        self.assertEqual(args.recipients, cfg.recipients)
        self.assertEqual(args.url, cfg.url)

    def test_parse_args_sender_specified(self):
        args = parse_args(['-s', 'sender@gmail.com'])
        self.assertEqual(args.sender, 'sender@gmail.com')
        self.assertEqual(args.recipients, cfg.recipients)
        self.assertEqual(args.url, cfg.url)


# class TestPrepareSoup(unittest.TestCase):
#
#     def setUp(self):
#         this.content = """<div class="dotd-main-book cf">
#         				<div class="section-inner">
#         					<div class="dotd-main-book-image float-left">
#
#         						<a href="/application-development/github-essentials">
#         							<noscript><img src="//d1ldz4te4covpm.cloudfront.net/sites/default/files/imagecache/dotd_main_image/9781783553716.png" alt="" title="" class="bookimage imagecache imagecache-dotd_main_image" itemprop="url"/></noscript><img src="//d1ldz4te4covpm.cloudfront.net/sites/default/files/imagecache/dotd_main_image/9781783553716.png" alt="" title="" data-original="//d1ldz4te4covpm.cloudfront.net/sites/default/files/imagecache/dotd_main_image/9781783553716.png" class="bookimage imagecache imagecache-dotd_main_image" itemprop="url" style="opacity: 1;">						</a>
#         					</div>
#         					<div class="dotd-main-book-summary float-left">
#         						<div class="eighteen-days-countdown-bar">
#         							Time is running out to claim this free ebook
#         							<span class="packt-js-countdown" data-countdown-to="1502751600">10:10:34</span>
#         						</div>
#         						<div class="dotd-title">
#         							<h2>
#         															GitHub Essentials														</h2>
#         						</div>
#         						<br>
#
#         													<div>
#         							Version Control Systems are essential for collaborative software development, which is in turn a great way to hone your abilities and learn new skills. Today's eBook will get you working with the immensely popular, web-based GitHub - it has over 14 million users and is the largest host of source code in the world with over 35 million repositories. Learn how to create a repository, manage team access, effectively use the issue tracker, create project documentation, schedule and release versions of your software, build a community around your project with GitHub tools, build free static websites for your projects, and more. Unleash the power of GitHub’s collaborative development workflow with this eBook!							</div>
#         												<div class="dotd-main-book-form cf">
#         							<div class="dots-main-book-price float-left"></div>
#         							<div class="float-left free-ebook">
#         								                                    <form action="/freelearning-claim/23013/21478" id="free-learning-form" method="POST">
#                                                 <div id="packt-freelearning-submit-claim" class="twelve-days-claim">
#                                                     <div class="book-claim-token-inner">
#                                                         <div class="book-claim-token-logo"></div>
#                                                         <div class="book-claim-token-separator"></div>
#                                                         <input id="free-learning-claim" class="form-submit" value="Claim Your Free eBook" type="submit">
#                                                     </div>
#                                                 </div>
#                                                 <div id="popup-recaptcha"><div class="grecaptcha-badge" style="width: 256px; height: 60px; transition: right 0.3s ease 0s; position: fixed; bottom: 14px; right: -186px; box-shadow: 0px 0px 5px gray;"><div class="grecaptcha-logo"><iframe src="https://www.google.com/recaptcha/api2/anchor?k=6LeAHSgUAAAAAKsn5jo6RUSTLVxGNYyuvUcLMe0_&amp;co=aHR0cHM6Ly93d3cucGFja3RwdWIuY29tOjQ0Mw..&amp;hl=pl&amp;v=r20170808164053&amp;size=invisible&amp;cb=e7e0ccx32wd8" title="widżet reCAPTCHA" scrolling="no" sandbox="allow-forms  allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups allow-popups-to-escape-sandbox" width="256" height="60" frameborder="0"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid #c1c1c1; margin: 10px 25px; padding: 0px; resize: none;  display: none; "></textarea></div></div>
#                                             </form>
#         															</div>
#         						</div>
#         					</div>
#
#         				</div>
#         			</div>"""
#         this.soup = BeautifulSoup(content)
#
#
#     def test_prepare_soup(self):
#         pass

if __name__ == '__main__':
    unittest.main()
