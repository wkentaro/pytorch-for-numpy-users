#!/usr/bin/env python

import collections
import os.path as osp
import string

import yaml

from generate_readme_md import get_section


def get_contents():
    # keep order in yaml file
    yaml.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        lambda loader, node: collections.OrderedDict(
            loader.construct_pairs(node)
        ),
    )

    yaml_file = osp.join(here, "conversions.yaml")
    with open(yaml_file) as f:
        data = yaml.safe_load(f)
    contents = []
    contents.append("<div class='row'>")
    for title, data in data.items():
        section = get_section(title, data)
        section = section.replace(
            "<table>",
            "<div class='table-responsive'>"
            "<table class='table table-bordered table-hover'>",
        )
        section = section.replace("</table>", "</table></div>")
        section = section.replace("<td>", "<td style='width: 50%'>")
        contents.append("<div class='col-md-6'>")
        contents.append(section)
        contents.append("</div>")
    contents.append("</div>")
    return "\n".join(contents)


here = osp.dirname(osp.abspath(__file__))


def main():
    with open(osp.join(here, "index.html.in")) as f:
        template = f.read()
    template = string.Template(template)
    readme = template.substitute(CONTENTS=get_contents())
    print(readme)


if __name__ == "__main__":
    main()
