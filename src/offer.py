class Offer:
    def __init__(self, soup, offer_image_url_extracter, offer_description_extracter):
        self._img_url = offer_image_url_extracter(soup)
        self._desc = offer_description_extracter(soup)

    def create_offer(self):
        image_url = extract_image_url(soup, image_class)
        title, desc = extract_description(soup, title_class)
        return {'image_url': image_url, 'title': title, 'desc': desc}
