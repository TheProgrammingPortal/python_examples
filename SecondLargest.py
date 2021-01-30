data = [55, 1, 45, 68, 159, 75, 5, 14, 159]


def find_second_maximum(list1):
    first_max = max(list1[0], list1[1])
    second_max = min(list1[0], list1[1])
    for i in range(2, len(list1)):
        if list1[i] > first_max:
            second_max = first_max
            first_max = list1[i]

        elif list1[i] > second_max and first_max != list1[i]:
            second_max = list1[i]
    return second_max


print("Second maximum number is ", find_second_maximum(data))
