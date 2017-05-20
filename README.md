# PyTorch for Numpy users.

[![Build Status](https://travis-ci.com/wkentaro/pytorch-for-numpy-users.svg?token=zM5rExyvuRoJThsnqHAF&branch=master)](https://travis-ci.com/wkentaro/pytorch-for-numpy-users)

[PyTorch](https://github.com/pytorch/pytorch.git) version of [_Torch for Numpy users_](https://github.com/torch/torch7/wiki/Torch-for-Numpy-users).

## Types

| Numpy        | PyTorch              |
|:-------------|:---------------------|
| `np.float32` | `torch.FloatTensor`  |
| `np.float64` | `torch.DoubleTensor` |
| `np.int8`    | `torch.CharTensor`   |
| `np.uint8`   | `torch.ByteTensor`   |
| `np.int16`   | `torch.ShortTensor`  |
| `np.int32`   | `torch.IntTensor`    |
| `np.int64`   | `torch.LongTensor`   |

## Constructors

### Ones and zeros

| Numpy              | PyTorch                                |
|:-------------------|:---------------------------------------|
| `np.empty((2, 3))` | `torch.Tensor(2, 3)`                   |
| `np.empty_like(x)` | `x.new(x.size()).type(x.type())`       |
| `np.eye`           | `torch.eye`                            |
| `np.identity`      | `torch.eye`                            |
| `np.ones`          | `torch.ones`                           |
| `np.ones_like`     | `torch.ones(x.size()).type(x.type())`  |
| `np.zeros`         | `torch.zeros`                          |
| `np.zeros_like`    | `torch.zeros(x.size()).type(x.type())` |


