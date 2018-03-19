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
    rows = []
    for d in data:
        numpy = '`' + d['numpy'] + '`' if d['numpy'] is not None else ''
        if isinstance(d['pytorch'], dict):
            content = d['pytorch']['content']
            is_code = d['pytorch']['is_code']
        elif d['pytorch'] is None:
            content = ''
            is_code = False
        else:
            content = d['pytorch']
            is_code = True
        pytorch = '`' + content + '`' if is_code else content
        rows.append([numpy, pytorch])

    content = '%s %s\n\n' % ('#' * h, title.capitalize())
    content += tabulate.tabulate(rows, headers=headers, tablefmt='pipe')
    content += '\n\n'
    return content


def get_contents():
    # keep order in yaml file
    yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        lambda loader, node: \
            collections.OrderedDict(loader.construct_pairs(node)))

    yaml_file = osp.join(here, 'conversions.yaml')
    data = yaml.load(open(yaml_file))
    contents = []
    for title, data in data.items():
        section = get_section(title, data)
        contents.append(section)
    return '\n'.join(contents)


here = osp.dirname(osp.abspath(__file__))


def main():
    template = open(osp.join(here, 'README.md.in')).read()
    template = string.Template(template)
    readme = template.substitute(contents=get_contents())
    print(readme)


if __name__ == '__main__':
    main()
