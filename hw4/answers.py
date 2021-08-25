r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""
from itertools import product

# ==============
# Part 1 answers


def part1_pg_hyperparams():
    hp = dict(
        batch_size=32, gamma=0.99, beta=0.5, learn_rate=1e-3, eps=1e-8, num_workers=2,
    )
    # TODO: Tweak the hyperparameters if needed.
    #  You can also add new ones if you need them for your model's __init__.
    # ====== YOUR CODE: ======
    hp['batch_size'] = 16
    hp['gamma'] = 0.99
    hp['beta'] = 0.5
    hp['learn_rate'] = 1e-3
    hp['eps'] = 1e-8
    hp['num_workers'] = 1
    # ========================
    return hp


def part1_aac_hyperparams():
    hp = dict(
        batch_size=32,
        gamma=0.99,
        beta=1.0,
        delta=1.0,
        learn_rate=1e-3,
        eps=1e-8,
        num_workers=2,
    )
    # TODO: Tweak the hyperparameters. You can also add new ones if you need
    #   them for your model implementation.
    
    # ====== YOUR CODE: ======
    hp['batch_size'] = [8,16,32]
    hp['gamma'] = [0.99]
    hp['critic_hidden_dims'] = [[256],[256,128],[256,128,64],[128,64]]
    hp['beta'] = [1]
    hp['delta'] = [1.0]
    hp['learn_rate'] = [1e-2,5e-3,1e-3]
    hp['eps'] = [1e-8]
    hp['num_workers'] = [0]
    keys, values = zip(*hp.items())
    for bundle in product(*values):
        d = dict(zip(keys, bundle))
        yield d
    # ========================
    return None


part1_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""


part1_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""


part1_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""
