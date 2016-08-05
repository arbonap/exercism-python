def distance(strand1, strand2):
    """ Utilize range(len(string)) on strand1 and compare via index to strand 2. If nucleotides do not match,
        increase the distance by 1. Return final distance
        to calculate Hamming Distance. """
    distance = 0
    for index in range(len(strand1)):
        if strand1[index] != strand2[index]:
            distance += 1
    return distance
