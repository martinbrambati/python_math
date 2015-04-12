def solution(linked_list):
    """
        Returns the lenght of a linked_list.
    """
    current_element = linked_list[0]
    lenght = 0
    while(current_element != -1):
        lenght += 1
        current_element = linked_list[current_element]

    return lenght

print(solution([1, 4, -1, 3, 2]))
