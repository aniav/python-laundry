import tika  # NOQA: This will download tika packages and setup the server
from tika import parser


def clean(html_content):
    parsed = parser.from_buffer(html_content)

    return parsed["content"]
