import random
## https://www.pluralsight.com/guides/running-shell-commands-with-flask
## Install Vienna RNA in <virtual environment>/Scripts folder
import os
import subprocess
from js_example import converter as cv

def gen():
    return(subprocess.Popen('RNAfold -p -d2 --noLP < hhr.txt',
                            shell=True, stdout=subprocess.PIPE).stdout.read())


def gen2():
    return(subprocess.Popen('RNAfold -p -d2 --noLP -C --enforceConstraint < hhr_constraint.txt',
                            shell=True, stdout=subprocess.PIPE).stdout.read())


def run(stem2_loop, stem1_side_1):
    core1 = 'CUGAUGAG'

    stem1_length = len(stem1_side_1)
    stem1_side_2 = []

    bases = ['A', 'C', 'U', 'G']

    complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}

    for i in (stem1_side_1):
        stem1_side_2.append(complement[i])

    stem2_length = random.randint(4, 10)
    stem2_loop_length = len(stem2_loop)
    stem2_side_1 = []
    stem2_side_2 = []
    stem3_loop_length = len(stem2_loop)/2 + 2
    bases = ['A', 'C', 'U', 'G']

    complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
    core2 = 'CGAAAC'

    for i in range(stem2_length):
        base = random.choice(bases)
        stem2_side_1.append(base)
        stem2_side_2.append(complement[base])


########################################################################################

    stem3_length = random.randint(4, 10)

    stem3_side_1 = []
    stem3_side_2 = []
    stem3_loop = []

    bases = ['A', 'C', 'U', 'G']

    complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
    core3 = 'GUA'

    for i in range(stem3_length):
        base = random.choice(bases)
        stem3_side_1.append(base)
        stem3_side_2.append(complement[base])
##############33 LOoop 3###############
    #base = random.choice(bases)
    for i in range(6):
        #base = random.choice(bases)
        stem3_loop.append(complement[stem2_loop[(stem2_loop_length)-i-1]])

    seq = "".join(stem1_side_1) + core1 + "".join(stem2_side_1) + "".join(stem2_loop) + "".join(stem2_side_2[::-1]) + core2 + "".join(
        stem3_side_1) + "".join(stem3_loop) + "".join(stem3_side_2[::-1]) + core3 + "".join(stem1_side_2[::-1])

    constrain = ["." for _ in range(
        len(stem1_side_1)+len(core1)+len(stem2_side_1))]
    constrain += ["x" for _ in range(len(stem2_loop))]
    l = len(seq) - len(constrain)
    constrain += ["." for _ in range(l)]

    return seq, constrain, stem1_side_2[::-1]


def find_diff(fold1, fold2, l):
    count = 0
    for i in range(len(fold1)):
        if fold1[i] != fold2[i]:
            count += 1

    if count >= l-1:
        return True
    else:
        return False


def convgen(stem2_loop, stem1_side_1):
    count = 0

    if os.path.exists("hhr_out.txt"):
        os.remove("hhr_out.txt")

    while True:
        seq, constrain, conv_output = run(stem2_loop, stem1_side_1)

        with open('hhr.txt', 'w') as f:
            f.write('>seq1\n')
            f.write(seq)

        with open('hhr_constraint.txt', 'w') as f:
            f.write('>seq1\n')
            f.write(seq+'\n')
            f.write("".join(constrain)+"\n")

        s = gen()
        print(s)
        ed1 = s[s.index(b'ensemble diversity') + 19:]

        mfe1 = s[s.index(b' ('):]
        mfe1 = mfe1[2:mfe1.index(b')')]
        fold1 = s[len(seq)+6:s.index(b' (')]

        s2 = gen2()
        print(s)
        mfe2 = s2[s2.index(b' ('):]
        mfe2 = mfe2[2:mfe2.index(b')')]
        fold2 = s2[len(seq)+6:s2.index(b' (')]

        mfe = float(mfe1) - float(mfe2)

        ed1 = ed1[:-2]
        ed2 = s2[s2.index(b'ensemble diversity') + 19:]
        ed2 = ed2[:-2]

        flag = find_diff(fold1, fold2, len(stem2_loop))
        if float(ed1) < 10 and float(ed2) < 10 and mfe > -10 and mfe < -6 and flag:
            with open('hhr_out.txt', 'a') as f:
                f.write(seq+"\n")
                f.write("".join(constrain)+"\n")
                count += 1

                if count == 1:
                    return True, seq, constrain, conv_output, str(fold1), str(fold2), str(ed1), str(ed2), str(mfe1), str(mfe2)

        # else:
        #    return False, seq, constrain, conv_output,fold1,fold2,ed1,ed2,mfe1,mfe2

            # break
