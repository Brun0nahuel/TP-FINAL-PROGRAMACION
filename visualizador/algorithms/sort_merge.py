items = []
n = 0
tam_sublista = 1
inicio_rango = 0
sub_inicio = 0
sub_fin = 0
cursor_i = 0
cursor_j = 0
fase = "division"

def init(vals):
    global items, n, tam_sublista, inicio_rango, sub_inicio, sub_fin, cursor_i, cursor_j, fase
    items = list(vals)
    n = len(items)
    tam_sublista = 1
    inicio_rango = 0
    sub_inicio = 0
    sub_fin = 0
    cursor_i = 0
    cursor_j = None
    fase = "division"

def step():
    global items, n, tam_sublista, inicio_rango, sub_inicio, sub_fin, cursor_i, cursor_j, fase

    while True:

        if tam_sublista >= n:
            return {"a": None, "b": None, "swap": False, "done": True}

        if fase == "division":

            if inicio_rango >= n:
                tam_sublista *= 2
                inicio_rango = 0
                continue

            sub_inicio = inicio_rango
            sub_fin = min(inicio_rango + 2 * tam_sublista, n) - 1

            if sub_fin <= sub_inicio:
                inicio_rango += 2 * tam_sublista
                continue

            fase = "ordenar_sublista"
            cursor_i = sub_inicio + 1
            cursor_j = None

            return {"a": sub_inicio, "b": sub_fin, "intercambio": False, "terminado": False}

        elif fase == "ordenar_sublista":

            if cursor_i > sub_fin:
                inicio_rango = sub_fin + 1
                fase = "division"
                continue

            if cursor_j is None:
                cursor_j = cursor_i

                if cursor_j <= sub_inicio or items[cursor_j - 1] <= items[cursor_j]:
                    cursor_i += 1
                    cursor_j = None
                    continue
                elif cursor_j == sub_inicio:
                    cursor_i += 1
                    cursor_j = None
                    continue

            if cursor_j > sub_inicio and items[cursor_j - 1] > items[cursor_j]:

                items[cursor_j - 1], items[cursor_j] = items[cursor_j], items[cursor_j - 1]

                a_idx = cursor_j - 1
                b_idx = cursor_j

                cursor_j -= 1

                return {"a": a_idx, "b": b_idx, "swap": True, "done": False}

            else:
                cursor_i += 1
                cursor_j = None
                continue
