from __future__ import absolute_import

from newspaper import Article
from newspaper.configuration import Configuration


def clean(html_content):
    config = Configuration()
    config.fetch_images = False

    # TODO: allow URL passing
    article = Article("http://example.com", config=config)
    article.set_html(html_content)
    article.is_downloaded = True
    article.parse()

    return article.text
