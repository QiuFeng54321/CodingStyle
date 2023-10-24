SomeReallyLongVariableName = 3491
SomeReallyLongVariableName += 3
n = 2
n = n * (n + 1) * (2 * n + 1) / 6
x = n * n == 4 or 2 == 3 and n == 2


def is_anagram(a: str, b: str):
    """Checks if the b can be rearranged to give a

    :param a: The first string
    :type a: str
    :param b: The second string
    :type b: str
    :return: Whether b has the same composition of characters as a
    :rtype: bool
    """
    if len(a) != len(b):
        return False
    visited = [False] * len(a)
    for i in range(len(a)):
        flag = False
        for j in range(len(b)):
            if visited[j]:
                continue
            if b[j] == a[i]:
                visited[j] = True
                flag = True
                break
        if not flag:
            return False
    return True
