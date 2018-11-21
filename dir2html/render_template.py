import sys

from pkg_resources import resource_string, resource_filename


def render_template(template_name, render_dict):
    template_names = {
        'image-template': "resources/image-template.html",
        'album-template': "resources/album-template.html"
    }

    template_file = resource_filename(__name__, template_names.get(template_name, ""))

    with open(template_file) as f:
        rendered_template = f.read()

        for k, v in render_dict.items():
            rendered_template = rendered_template.replace(k, v)

        return rendered_template
