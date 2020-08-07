def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    # store number that's repeated
    repeated = dict()

    for array in arrays:
        for num in array:
            if num in repeated:
                repeated[num] += 1
            else:
                repeated[num] = 1

    # print(repeated)
    # return number that have repeated multiple times in the length of the arrays.
    return [number[0] for number in repeated.items() if number[1] == len(arrays)]


if __name__ == "__main__":
    arrays_test = [list(range(1000000, 2000000)) + [1, 2, 3],
                   list(range(2000000, 3000000)) + [1, 2, 3],
                   list(range(3000000, 4000000)) + [1, 2, 3]]

    print(intersection(arrays_test))