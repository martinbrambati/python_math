def solution(linked_list):
    """
        Returns the lenght of a linked_list.
    """
    new_list, copy = {}, linked_list[:]
    while(len(copy) > 0):
        if copy[0] != -1:
            new_list[copy[0]] = copy[0]

        del copy[0]

    return len(new_list)

linked = [1, 4, -1, 3, 2]
assert(solution(linked) == 4)
