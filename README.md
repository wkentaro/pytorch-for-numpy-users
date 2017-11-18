# PyTorch for Numpy users.

[![Build Status](https://travis-ci.com/wkentaro/pytorch-for-numpy-users.svg?token=zM5rExyvuRoJThsnqHAF&branch=master)](https://travis-ci.com/wkentaro/pytorch-for-numpy-users)

[PyTorch](https://github.com/pytorch/pytorch.git) version of [_Torch for Numpy users_](https://github.com/torch/torch7/wiki/Torch-for-Numpy-users).

## Types

| Numpy        | PyTorch              |
|:-------------|:---------------------|
| `np.ndarray` | `torch.Tensor`       |
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

### From existing data

| Numpy                        | PyTorch                             |
|:-----------------------------|:------------------------------------|
| `np.array([[1, 2], [3, 4]])` | `torch.Tensor([[1, 2], [3, 4])`     |
| `x.copy()`                   | `x.clone()`                         |
| `np.fromfile(file)`          | `torch.Tensor(torch.Storage(file))` |
| `np.frombuffer`              |                                     |
| `np.fromfunction`            |                                     |
| `np.fromiter`                |                                     |
| `np.fromstring`              |                                     |
| `np.loadtxt`                 |                                     |
| `np.concatenate`             | `torch.cat`                         |

### Numerical ranges

| Numpy                  | PyTorch                   |
|:-----------------------|:--------------------------|
| `np.arange(10)`        | `torch.range(0, 9)`       |
| `np.arange(2, 3, 0.1)` | `torch.range(2, 2.9, 10)` |
| `np.linspace`          | `torch.linspace`          |
| `np.logspace`          | `torch.logspace`          |

### Building matrices

| Numpy     | PyTorch      |
|:----------|:-------------|
| `np.diag` | `torch.diag` |
| `np.tril` | `torch.tril` |
| `np.triu` | `torch.triu` |

### Attributes

| Numpy       | PyTorch        |
|:------------|:---------------|
| `x.shape`   | `x.size()`     |
| `x.strides` | `x.stride()`   |
| `x.ndim`    | `x.dim()`      |
| `x.data`    | `x.data()`     |
| `x.size`    | `x.nelement()` |
| `x.dtype`   | `x.type()`     |

### Indexing

| Numpy                 | PyTorch                        |
|:----------------------|:-------------------------------|
| `x[0]`                | `x[0]`                         |
| `x[:, 0]`             | `x[:, 0]`                      |
| `x[indices]`          | `x[torch.LongTensor(indices)]` |
| `np.take(x, indices)` | `x[torch.LongTensor(indices)]` |
| `x[x != 0]`           | `x[x != 0]`                    |

### Shape manipulation

| Numpy              | PyTorch          |
|:-------------------|:-----------------|
| `x.reshape`        | `x.view`         |
| `x.resize`         | `x.resize_`      |
|                    | `x.resize_as_`   |
| `x.transpose`      | `x.permute`      |
| `x.flatten()`      | `x.view(-1)`     |
| `x.squeeze`        | `x.squeeze`      |
| `x[:, np.newaxis]` | `x.unsqueeze(1)` |

### Item selection and manipulation

| Numpy        | PyTorch                                  |
|:-------------|:-----------------------------------------|
| `np.put`     |                                          |
| `x.repeat`   |                                          |
| `x.tile`     | `x.repeat`                               |
| `np.choose`  |                                          |
| `np.sort`    | `sorted, indices = torch.sort(x, [dim])` |
| `np.argsort` | `sorted, indices = torch.sort(x, [dim])` |
| `np.nonzero` | `torch.nonzero`                          |
| `np.where`   | `torch.nonzero`                          |

### Calculation

| Numpy         | PyTorch                               |
|:--------------|:--------------------------------------|
| `x.min`       | `mins, indices = torch.min(x, [dim])` |
| `x.argmin`    | `mins, indices = torch.min(x, [dim])` |
| `x.max`       | `maxs, indices = torch.max(x, [dim])` |
| `x.argmax`    | `maxs, indices = torch.max(x, [dim])` |
| `x.clip`      | `x.clamp`                             |
| `x.round`     | `x.round`                             |
| `np.floor(x)` | `x.floor()`                           |
| `np.ceil(x)`  | `x.ceil()`                            |
| `x.trace`     | `x.trace`                             |
| `x.sum`       | `x.sum`                               |
| `x.cumsum`    | `x.cumsum`                            |
| `x.mean`      | `x.mean`                              |
| `x.std`       | `x.std`                               |
| `x.prod`      | `x.prod`                              |
| `x.cumprod`   | `x.cumprod`                           |
| `x.all`       | `(x == 1).sum() == x.nelement()`      |
| `x.any`       | `(x == 1).sum() > 0`                  |

### Arithmetic and comparison operations

| Numpy   | PyTorch   |
|:--------|:----------|
| `x.lt`  | `x.lt`    |
| `x.le`  | `x.le`    |
| `x.gt`  | `x.gt`    |
| `x.ge`  | `x.ge`    |
| `x.eq`  | `x.eq`    |
| `x.ne`  | `x.ne`    |



