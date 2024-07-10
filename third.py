"""
Поскольку нужно отсортировать числа, о которых нет дополнительной информации,
 то специфические сортировки по типу bucket sort и
  поразрядной сортировки с ассимптотической сложностью О(n) в среднем нам не подойдут.
   Поэтому рассмотрим сортировки со сложностью O(n*log(n)).
    Быстрая сортировка нам не подходит потому что
     она не проверяет уже отсортированные подмассивы,
      а также в худшем случае (при выборе неудачного опорного элемента)
       сложность составит O(n^2), поэтому выбираем Timsort,
        она проверяет отсортированные подмассивы и в худшем случае будет работать за O(n*log(n)).
"""


def get_min_run(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return r + n


def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def merge(arr, l, m, r):
    len1, len2 = m - l + 1, r - m
    left = []
    right = []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
    i, j, k = 0, 0, l
    while i < len1 or j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1


def tim_sort(arr):
    n = len(arr)
    min_run = get_min_run(n)
    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort(arr, start, end)
    size = min_run
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2


array = [4, 3, 5, 1, 5, 1, 7, 345, 12, 34, 1, 5, 7]
tim_sort(array)
print(array)
