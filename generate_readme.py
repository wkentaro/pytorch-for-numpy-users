#!/usr/bin/env python

import collections
import os.path as osp

import tabulate
import yaml


TEMPLATE = '''\
# PyTorch for Numpy users.

[![Build Status](https://travis-ci.com/wkentaro/pytorch-for-numpy-users.svg?token=zM5rExyvuRoJThsnqHAF&branch=master)](https://travis-ci.com/wkentaro/pytorch-for-numpy-users)

[PyTorch](https://github.com/pytorch/pytorch.git) version of [_Torch for Numpy users_](https://github.com/torch/torch7/wiki/Torch-for-Numpy-users).

{contents}
'''


here = osp.dirname(osp.abspath(__file__))


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
        pytorch = '`' + d['pytorch'] + '`'  if d['pytorch'] is not None else ''
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


print(TEMPLATE.format(contents=get_contents()))
