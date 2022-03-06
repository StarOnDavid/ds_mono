import json
from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

PACKAGE_PATH = Path.cwd()
OUT_PATH = PACKAGE_PATH / 'out'


def create_page(content, template_name):

    template_loader = FileSystemLoader(searchpath="./create_page/templates")
    env = Environment(
        loader=template_loader,
        autoescape=select_autoescape()
    )
    template = env.get_template(template_name)

    return template.render(content)
