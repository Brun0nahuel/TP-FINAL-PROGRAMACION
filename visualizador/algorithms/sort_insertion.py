items = []
n = 0
i = 0
j = None

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1
    j = None

def step():
    global items, n, i, j
    if i >= n:
        return {"done": True, "a": None, "b": None, "swap": False}

    if j is None:
        j = i
        return {"done": False, "a": j-1, "b": j, "swap": False}

    if j > 0 and items[j-1] > items[j]:
        items[j-1], items[j] = items[j], items[j-1]   # swap
        j -= 1
        return {"done": False, "a": j, "b": j+1, "swap": True}

    i += 1
    j = None
    return {"done": False, "a": None, "b": None, "swap": False}
