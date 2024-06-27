def levenshtein_distance(src, target):
    result = []
    del_cost = 0
    ins_cost = 0
    sub_cost = 0
    for _ in range(len(src)+1):
        temp = [0]*(len(target)+1)
        result.append(temp)
    for i in range(len(target) + 1):
        result[0][i] = i
    for i in range(len(src) + 1):
        result[i][0] = i
    for idx in range(1, len(src)+1):
        for jdx in range(1, len(target) + 1):
            if (result[idx][jdx-1] == result[idx-1][jdx]) and (src[idx-1] == target[jdx-1]):
                result[idx][jdx] = result[idx-1][jdx-1]
            else:
                del_cost = result[idx - 1][jdx] + 1
                ins_cost = result[idx][jdx - 1] + 1
                sub_cost = result[idx - 1][jdx - 1] + 1
                result[idx][jdx] = min(del_cost, ins_cost, sub_cost)
    return result[-1][-1]


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([line.strip().lower() for line in lines]))
    return words
