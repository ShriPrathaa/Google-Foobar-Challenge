def solution(g):
    if len(g) < len(g[0]) :
        g = [[row[i] for row in g] for i in range(len(g[0]))]
    ruleset = generate_ruleset()
    preimage = [[p, 1] for p in generate_row_preimage(g[0], ruleset)]
    for row in g[1:]:
        next_preimage = generate_row_preimage(row, ruleset)
        preimage = [[np, sum([p[1] for p in preimage
                              if p[1] != 0 and p[0][1] == np[0]])]
                    for np in next_preimage]
    result = sum([p[1] for p in preimage])
    return result

def generate_ruleset() :
    gas = [[[1, 0], [0, 0]],
           [[0, 1], [0, 0]],
           [[0, 0], [1, 0]],
           [[0, 0], [0, 1]]]
    no_gas = [[[0, 0], [0, 0]],
              [[1, 1], [0, 0]],
              [[1, 0], [1, 0]],
              [[1, 0], [0, 1]],
              [[0, 1], [1, 0]],
              [[0, 1], [0, 1]],
              [[0, 0], [1, 1]],
              [[1, 1], [1, 0]],
              [[1, 1], [0, 1]],
              [[1, 0], [1, 1]],
              [[0, 1], [1, 1]],
              [[1, 1], [1, 1]]]
    ruleset = [gas, no_gas]
    return ruleset

def generate_row_preimage(row, ruleset) :
    preimage = ruleset[0] if row[0] else ruleset[1]
    for cell in row[1:] :
        rule = ruleset[0] if cell else ruleset[1]
        preimage = [[p[0] + [r[0][1]], p[1] + [r[1][1]]]
                    for p in preimage for r in rule
                    if p[0][-1] == r[0][0] and p[1][-1] == r[1][0]]
    return preimage



