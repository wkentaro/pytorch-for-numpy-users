#!/usr/bin/env python

from __future__ import print_function

import glob
import os
import os.path as osp
import subprocess

import yaml


def parse(data, parsed=None):
    if parsed is None:
        parsed = []

    for _, datum in data.items():
        if isinstance(datum, dict):
            for _ in parse(datum):
                yield _
        else:
            for item in datum:
                for key in item:
                    item_k = item[key]
                    if isinstance(item_k, dict):
                        content = item_k['content']
                        is_code = item_k.get('is_code', True)
                        if item_k.get('skip_test', False):
                            continue
                    else:
                        content = item_k
                        is_code = True
                    if is_code and content is not None:
                        yield key, content


def main():
    here = osp.dirname(osp.abspath(__file__))

    with open(osp.join(here, 'conversions.yaml')) as f:
        data = yaml.load(f)

    for fname in glob.glob(osp.join(here, 'tests/*.py')):
        os.remove(fname)

    for i, (key, content) in enumerate(parse(data)):
        if key == 'numpy':
            code = '''\
import numpy as np


def test_%04d():
    x = np.array([[1, 2, 3], [4, 5, 6]])
%s
'''
        elif key == 'pytorch':
            code = '''\
import torch


def test_%04d():
    x = torch.tensor([[1, 2, 3], [4, 5, 6]])
%s
'''
        else:
            raise ValueError

        content = '\n'.join(' ' * 4 + l for l in content.splitlines())
        code = code % (i, content)

        test_file = osp.join(here, 'tests/test_%04d.py' % i)
        with open(test_file, 'w') as f:
            f.write(code)

    cmd = 'pytest -vs tests'
    print('+ %s' % cmd)
    subprocess.call(cmd, shell=True)


if __name__ == '__main__':
    main()
