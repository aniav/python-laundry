from __future__ import absolute_import

import justext


def clean(html_content):
    paragraphs = justext.justext(html_content, "English")
    clean_paragraphs = [p.text for p in paragraphs]
    text = "\n\n".join(clean_paragraphs)

    return text
