def init(vals): 
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = n - 1
    j = 0

def step(_=None):
    global items, n, i, j
    if i < 1:
        return {"done": True}
    a = j
    b = j + 1
    swap = False
    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap = True
    j += 1
    if j >= i:
        i -= 1
        j = 0
    return {"a": a, "b": b, "swap": swap, "done": False}

