import heapq
import sys


# Задание 1
def sequential_search(arr, target):
    comparisons = 0
    for i, num in enumerate(arr):
        comparisons += 1
        if num == target:
            return i, comparisons
    return -1, comparisons

def binary_search(arr, target):
    comparisons = 0
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons

def interpolation_search(arr, target):
    comparisons = 0
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        mid = low + (high - low) * (target - arr[low]) // (arr[high] - arr[low])
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons


with open("filename.txt", "r") as file:
    data = [int(x) for x in file.read().split()]


user_number = int(input("Введите число для поиска: "))

# Последовательный поиск
sequential_result, sequential_comparisons = sequential_search(data, user_number)
print(f"Последовательный поиск: {sequential_result}, Количество сравнений: {sequential_comparisons}")

# Бинарный поиск
binary_result, binary_comparisons = binary_search(data, user_number)
print(f"Бинарный поиск: {binary_result}, Количество сравнений: {binary_comparisons}")

# Интерполяционный поиск
interpolation_result, interpolation_comparisons = interpolation_search(data, user_number)
print(f"Интерполяционный поиск: {interpolation_result}, Количество сравнений: {interpolation_comparisons}")






# Задание 2
def sequential_search_sequence(arr, sequence):
    comparisons = 0
    for i in range(len(arr) - len(sequence) + 1):
        match = True
        for j in range(len(sequence)):
            comparisons += 1
            if arr[i + j] != sequence[j]:
                match = False
                break
        if match:
            return i, comparisons
    return -1, comparisons

def kmp_search(arr, pattern):
    def build_prefix_table(pattern):
        m = len(pattern)
        prefix_table = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and pattern[i] != pattern[j]:
                j = prefix_table[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            prefix_table[i] = j
        return prefix_table

    comparisons = 0
    n, m = len(arr), len(pattern)
    prefix_table = build_prefix_table(pattern)
    i = j = 0
    while i < n:
        comparisons += 1
        if arr[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                return i - m, comparisons
        else:
            if j > 0:
                j = prefix_table[j - 1]
            else:
                i += 1
    return -1, comparisons

def boyer_moore_search(arr, pattern):
    def build_bad_char_table(pattern):
        bad_char_table = dict()
        m = len(pattern)
        for i in range(m - 1):
            bad_char_table[pattern[i]] = m - i - 1
        return bad_char_table

    comparisons = 0
    n, m = len(arr), len(pattern)
    bad_char_table = build_bad_char_table(pattern)
    i = m - 1
    while i < n:
        j = m - 1
        while j >= 0 and arr[i] == pattern[j]:
            comparisons += 1
            i -= 1
            j -= 1
        if j == -1:
            return i + 1, comparisons
        bad_char_shift = bad_char_table.get(arr[i], m)
        i += max(bad_char_shift, m - j)
    return -1, comparisons

# Чтение отсортированных данных из файла
with open("filename.txt", "r") as file:
    sorted_data = [int(x) for x in file.read().split()]

# Заданная пользователем последовательность
user_sequence = [int(x) for x in input("Введите последовательность для поиска: ").split()]

# Последовательный поиск
sequential_result, sequential_comparisons = sequential_search_sequence(sorted_data, user_sequence)
print(f"Последовательный поиск: {sequential_result}, Количество сравнений: {sequential_comparisons}")

# Поиск по алгоритму Кнута-Морриса-Прата
kmp_result, kmp_comparisons = kmp_search(sorted_data, user_sequence)
print(f"Кнута-Морриса-Прата: {kmp_result}, Количество сравнений: {kmp_comparisons}")

# Поиск по алгоритму Боуера-Мура
boyer_moore_result, boyer_moore_comparisons = boyer_moore_search(sorted_data, user_sequence)
print(f"Боуера-Мура: {boyer_moore_result}, Количество сравнений: {boyer_moore_comparisons}")








# Задание 3

def insertion_sort(arr):
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return comparisons

def bubble_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return comparisons

def selection_sort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return comparisons

def shell_sort(arr):
    comparisons = 0
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons += 1
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return comparisons

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    comparisons = 0
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        comparisons += 1
        heapify(arr, i, 0)

    return comparisons

def quick_sort(arr, low, high):
    comparisons = 0
    if low < high:
        pi, comparisons_partition = partition(arr, low, high)
        comparisons += comparisons_partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return comparisons

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    comparisons = 0
    for j in range(low, high):
        comparisons += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1, comparisons


with open("filename2.txt", "r") as file:
    data = [int(x) for x in file.read().split()]


data_insertion = data.copy()
data_bubble = data.copy()
data_selection = data.copy()
data_shell = data.copy()
data_heap = data.copy()
data_quick = data.copy()

# Сортировка вставками
insertion_comparisons = insertion_sort(data_insertion)
print(f"Сортировка вставками. Количество сравнений: {insertion_comparisons}")

# Сортировка пузырьком
bubble_comparisons = bubble_sort(data_bubble)
print(f"Сортировка пузырьком. Количество сравнений: {bubble_comparisons}")

# Сортировка выбором
selection_comparisons = selection_sort(data_selection)
print(f"Сортировка выбором. Количество сравнений: {selection_comparisons}")

# Сортировка Шелла
shell_comparisons = shell_sort(data_shell)
print(f"Сортировка Шелла. Количество сравнений: {shell_comparisons}")

# Пирамидальная сортировка (Heap Sort)
heap_comparisons = heap_sort(data_heap)
print(f"Пирамидальная сортировка. Количество сравнений: {heap_comparisons}")

# Быстрая сортировка
quick_comparisons = quick_sort(data_quick, 0, len(data_quick) - 1)
print(f"Быстрая сортировка. Количество сравнений: {quick_comparisons}")







# Задание 4

# 1) Простое слияние (Simple Merge Sort):

def simple_merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        simple_merge_sort(left_half)
        simple_merge_sort(right_half)

        merge(arr, left_half, right_half)

def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

with open("filename2.txt", "r") as file:
    data = [int(x) for x in file.read().split()]

# Простое слияние
simple_merge_sort(data)

print(data)




# 2) Естественное слияние (Natural Merge Sort):
def natural_merge_sort(arr):
    runs = identify_runs(arr)
    while len(runs) > 1:
        merge_runs(arr, runs)
        runs = identify_runs(arr)

def identify_runs(arr):
    runs = []
    n = len(arr)
    i = 1
    while i < n:
        start = i - 1
        while i < n and arr[i] >= arr[i - 1]:
            i += 1
        runs.append((start, i - 1))
        while i < n and arr[i] <= arr[i - 1]:
            i += 1
    return runs

def merge_runs(arr, runs):
    result = []
    while runs:
        start1, end1 = runs.pop(0)
        start2, end2 = runs.pop(0) if runs else (sys.maxsize, sys.maxsize)
        i = start1
        j = start2

        while i <= end1 or j <= end2:
            if i <= end1 and (j > end2 or arr[i] <= arr[j]):
                result.append(arr[i])
                i += 1
            elif j <= end2:
                result.append(arr[j])
                j += 1

        result.extend(arr[i:end1 + 1])
        result.extend(arr[j:end2 + 1])

    for idx, val in enumerate(result):
        arr[start1 + idx] = val



with open("filename2.txt", "r") as file:
    data = [int(x) for x in file.read().split()]

# Естественное слияние
natural_merge_sort(data)

print(data)




# 3) Многофазная сортировка (Polyphase Merge Sort):


def polyphase_merge_sort(input_files, output_file):
    # Открытие входных и выходного файлов
    input_handles = [open(file, 'r') for file in input_files]
    output_handle = open(output_file, 'w')

    # Чтение первых элементов из каждого файла
    current_values = []
    for handle in input_handles:
        value = handle.readline().strip()
        if value:
            current_values.append((int(value), handle))

    # Использование кучи для эффективного выбора минимального значения
    heapq.heapify(current_values)

    # Многофазное слияние
    while current_values:
        min_value, min_handle = heapq.heappop(current_values)
        output_handle.write(str(min_value) + '\n')

        next_value = min_handle.readline().strip()
        if next_value:
            heapq.heappush(current_values, (int(next_value), min_handle))

    # Закрытие файлов
    for handle in input_handles:
        handle.close()
    output_handle.close()


input_files = ["input_file1.txt", "input_file2.txt", "input_file3.txt"]
output_file = "output_file.txt"
polyphase_merge_sort(input_files, output_file)





