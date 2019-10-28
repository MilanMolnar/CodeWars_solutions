def snail(array):
    results = []
    while len(array) > 0:
        results += array[0]
        del array[0]

        if len(array) > 0:
            for i in array:
                results += [i[-1]]
                del i[-1]

            if array[-1]:
                results += array[-1][::-1]
                del array[-1]

            for i in reversed(array):
                results += [i[0]]
                del i[0]

    return results
