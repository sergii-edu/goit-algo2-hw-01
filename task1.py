import random


def find_min_max(arr):
    def helper(left, right):
        if left == right:
            return arr[left], arr[left]

        mid = (left + right) // 2
        min1, max1 = helper(left, mid)
        min2, max2 = helper(mid + 1, right)

        return min(min1, min2), max(max1, max2)

    return helper(0, len(arr) - 1)


if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(10)]
    print(f"Generated numbers: {arr}")

    min_value, max_value = find_min_max(arr)
    print(f"Minimum value: {min_value}, Maximum value: {max_value}")
