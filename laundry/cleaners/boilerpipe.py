from __future__ import absolute_import

from boilerpipe.extract import Extractor


def clean(html_content):
    extractor = Extractor(extractor="ArticleExtractor",
                          html=html_content)
    return extractor.getText()
