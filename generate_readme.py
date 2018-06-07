#!/usr/bin/env python

import collections
import os.path as osp
import string

import tabulate
import yaml


def get_section(title, data, h=2):
    if not isinstance(data, list):
        content = '%s %s\n\n' % ('#' * h, title.capitalize())
        for sub_title, sub_data in data.items():
            content += get_section(sub_title, sub_data, h=h+1)
        return content

    headers = ['Numpy', 'PyTorch']
    keys = ['numpy', 'pytorch']
    rows = []
    for d in data:
        row = []
        for key in keys:
            if isinstance(d[key], dict):
                content = d[key]['content']
                is_code = d[key]['is_code']
            elif d[key] is None:
                content = ''
                is_code = False
            else:
                content = d[key]
                is_code = True
            if is_code and content:
                if len(content.splitlines()) > 1:
                    content = '<pre>\n{}</pre>'.format(content)
                else:
                    content = '<code>{}</code>'.format(content)
            row.append(content)
        rows.append(row)

    content = '%s %s\n\n' % ('#' * h, title.capitalize())
    content += tabulate.tabulate(rows, headers=headers, tablefmt='html')
    content += '\n\n'
    return content


def get_contents():
    # keep order in yaml file
    yaml.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        lambda loader, node:
            collections.OrderedDict(loader.construct_pairs(node)),
    )

    yaml_file = osp.join(here, 'conversions.yaml')
    with open(yaml_file) as f:
        data = yaml.load(f)
    contents = []
    for title, data in data.items():
        section = get_section(title, data)
        contents.append(section)
    return '\n'.join(contents)


here = osp.dirname(osp.abspath(__file__))


def main():
    with open(osp.join(here, 'README.md.in')) as f:
        template = f.read()
    template = string.Template(template)
    readme = template.substitute(contents=get_contents())
    print(readme)


if __name__ == '__main__':
    main()
