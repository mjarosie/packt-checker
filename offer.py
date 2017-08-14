def extract_image_url(soup, image_class):
    tag = soup.find(class_=image_class)
    return 'http:' + tag['src']


def extract_description(soup, title_class):
    tag = soup.find(class_=title_class)
    title = str.strip(tag.h2.string)

    # Go to the next <div> - this is where the description is.
    tag = get_next_tag(tag)

    # Description of the book is placed within classless <div> tags,
    # between <div class="dotd-title"> and <div class="dotd-main-book-form cf">
    description = ''
    while 'class' not in tag.attrs or 'dotd-main-book-form' not in tag['class']:
        description = description + str.strip(tag.get_text()) + '\n'
        # Find the next <div> tag.
        tag = get_next_tag(tag)

    return title, description


def get_next_tag(tag):
    """Helper function that """
    for sibling in tag.next_siblings:
        if sibling == '\n':
            continue
        tag = sibling
        break
    return tag


def create_offer(soup, image_class='bookimage', title_class='dotd-title'):
    image_url = extract_image_url(soup, image_class)
    title, desc = extract_description(soup, title_class)
    return {'image_url': image_url, 'title': title, 'desc': desc}
