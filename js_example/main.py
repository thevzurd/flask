import random
from js_example import converter as cv
import json


def main(inp, out):
    bases = ['A', 'C', 'U', 'G']
    if not inp:
        l = random.randint(10, 20)
        inp = [random.choice(bases) for _ in range(l)]

    if not out:
        l = random.randint(10, 20)
        out = [random.choice(bases) for _ in range(l)]

    _, seq, constrain, conv_output, fold1, fold2, ed1, ed2, mfe1, mfe2 = \
        cv.convgen(inp, out)

    data = {}
    data['Sequence'] = seq
    data['Inactive'] = fold1
    data['Inactive MFE'] = mfe1
    data['Inactive ED'] = ed1
    data['Active'] = fold2
    data['Active MFE'] = mfe2
    data['Active ED'] = ed2
    data['Input'] = "".join(inp)
    data['Output'] = "".join(out)

    with open('output.json', 'w') as f:
        json.dump(data, f)

    print('>1')
    print(seq)
    print(fold1)
    print('>2')
    print(seq)
    print(fold2)


if __name__ == '__main__':
    main("", "")
