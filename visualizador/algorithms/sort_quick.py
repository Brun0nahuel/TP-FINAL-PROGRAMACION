items = []
n = 0
stack = []
phase = "new"
start = end = i = j = pivot = None

def init(vals):
    global items, n, stack, phase, start, end, i, j, pivot
    print(f"[Python] init() llama                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    do con {len(vals)} valores")
    items = list(vals)
    n = len(items)
    stack = [(0, n - 1)] if n > 1 else []
    phase = "new"
    start = end = i = j = pivot = None
    print(f"[Python] init() completado. n = {n}, Pila inicial: {stack}")

def step():
    global items, n, stack, phase, start, end, i, j, pivot

    if phase == "new":
        if not stack:
            print("[Python] Ordenamiento terminado.")
            return {"a": 0, "b": 0, "swap": False, "done": True}
            
        start, end = stack.pop()
        print(f"[Python] Nueva partición: start={start}, end={end}")

        if start >= end:
            phase = "new"
            return {"a": start, "b": end, "swap": False, "done": False}
        
        pivot = items[end]
        i = start
        j = start
        phase = "compare"
        
        return {"a": end, "b": end, "swap": False, "done": False}

    if phase == "compare":
        if j < end:
            res = {}
            if items[j] <= pivot:
                items[i], items[j] = items[j], items[i]
                res = {"a": i, "b": j, "swap": True, "done": False}
                print(f"[Python] Swap de comparación ({i},{j}) -> {items}")
                i += 1
            else:
                res = {"a": j, "b": end, "swap": False, "done": False}
            
            j += 1
            return res
        
        else:
            phase = "pivot"
            print(f"[Python] Comparación terminada. Siguiente fase: pivot (i={i})")
            return {"a": i, "b": end, "swap": False, "done": False}

    if phase == "pivot":
        items[i], items[end] = items[end], items[i]
        pivot_index = i
        print(f"[Python] Pivote colocado en {pivot_index}. Lista parcial: {items}")

        if start < pivot_index - 1:
            stack.append((start, pivot_index - 1))
        if pivot_index + 1 < end:
            stack.append((pivot_index + 1, end))
        
        print(f"[Python] Pila actualizada: {stack}")

        phase = "new"
        
        return {"a": i, "b": end, "swap": True, "done": False}
