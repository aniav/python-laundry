from __future__ import absolute_import

from goose import Goose
from goose.configuration import Configuration


def clean(html_content):
    config = Configuration()
    config.enable_image_fetching = False
    extractor = Goose(config=config)

    article = extractor.extract(raw_html=html_content)

    return article.cleaned_text
