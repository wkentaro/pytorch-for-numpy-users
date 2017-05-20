#!/usr/bin/env python

import collections
import os.path as osp

import tabulate
import yaml


TEMPLATE = '''\
# PyTorch for Numpy users

[![Build Status](https://travis-ci.com/wkentaro/pytorch-for-numpy-users.svg?token=zM5rExyvuRoJThsnqHAF&branch=master)](https://travis-ci.com/wkentaro/pytorch-for-numpy-users)

[PyTorch](https://github.com/pytorch/pytorch.git) version of [_Torch for Numpy users_](https://github.com/torch/torch7/wiki/Torch-for-Numpy-users).

{contents}
'''


here = osp.dirname(osp.abspath(__file__))


def get_contents():
    # keep order in yaml file
    yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        lambda loader, node: \
            collections.OrderedDict(loader.construct_pairs(node)))

    yaml_file = osp.join(here, 'conversions.yaml')
    data = yaml.load(open(yaml_file))
    contents = ''
    for section, data in data.items():
        headers = ['Numpy', 'PyTorch']
        rows = []
        for d in data:
            rows.append([
                '`' + d['numpy'] + '`',
                '`' + d['pytorch'] + '`',
            ])
        contents += '''
## {title}

{table}\n'''.format(
            title=section.capitalize(),
            table=tabulate.tabulate(rows, headers=headers, tablefmt='pipe'),
        )
    return contents


print(TEMPLATE.format(contents=get_contents()))
