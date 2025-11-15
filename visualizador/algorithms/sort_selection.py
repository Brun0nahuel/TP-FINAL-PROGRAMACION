items = []
n = 0
i = 0
j = 0
min_idx = 0
fase = "buscar"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase

    if i >= n - 1:
        return {"done": True}

    if fase == "buscar":
        
        if j == i + 1:
            min_idx = i
        
        if j >= n:
            fase = "swap"
        
        else:
            j_actual = j
            
            if items[j] < items[min_idx]:
                min_idx = j
            
            j = j + 1
            
            return {"a": min_idx, "b": j_actual, "swap": False, "done": False}

    if fase == "swap":
        
        swapped = False
        a = i
        b = min_idx

        if min_idx != i:
            items[i], items[min_idx] = items[min_idx], items[i]
            swapped = True
        
        i = i + 1
        min_idx = i
        j = i + 1
        fase = "buscar"

        return {"a": a, "b": b, "swap": swapped, "done": False}