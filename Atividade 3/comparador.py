import time

with open('arq.txt', 'r', encoding='utf-8-sig') as f:
    numeros = list(map(int, f.read().split()))


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    return quick_sort([x for x in arr if x < pivot]) + \
           [x for x in arr if x == pivot] + \
           quick_sort([x for x in arr if x > pivot])


def medir(nome, funcao, dados):
    tempos = []
    resultado = None
    print(f"\nAlgoritmo: {nome}")
    for i in range(1, 6):
        copia = dados.copy()
        inicio = time.perf_counter()
        resultado = funcao(copia)
        elapsed = time.perf_counter() - inicio
        tempos.append(elapsed)
        print(f"  Execução {i}: {elapsed:.6f}s")
    print(f"  Média: {sum(tempos)/len(tempos):.6f}s")
    return resultado


medir("Bubble Sort", bubble_sort, numeros)
ordenado = medir("Quick Sort", quick_sort, numeros)

with open('arq-ordenado.txt', 'w') as f:
    f.write(' '.join(map(str, ordenado)))

print("\narq-ordenado.txt salvo.")