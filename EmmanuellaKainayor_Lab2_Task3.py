def find_unique_brute_force(arr):
    for i in range (len(arr)):
        count = 0

        for j in range (len(arr)):
            if arr[i] == arr[j]:
                count += 1

            if count == 1:
                return arr[i]


def find_unique_ON_ON(arr):
    counts = {}

    for num in arr:
        if num not in counts:
            counts[num] = 1

        else:
            counts[num] += 1

    for num in counts:
        if counts[num] == 1:
            return counts[num]

def find_unique_ON_O1(arr):
    result = 0

    for i in range (len(arr)):
        result = result ^ arr[i]

    return result


if __name__ == "__main__":
    tests = [
        [0,2,-4,5,2,0,-4],
        [3,3,3,3,6,6,7],
        [1,1,1,1,1,1,1,1,2],
        [1,0,1,2,4,2,4],
        [3],
    ]

    for arr in tests:
        print("Array:", arr)
        print("Brute force:", find_unique_brute_force(arr))
        print("O(n)/O(n):", find_unique_ON_ON(arr))
        print("O(n)/O(1):", find_unique_ON_O1(arr))
        print()

