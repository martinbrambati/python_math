def equilibrium(array):
    """ A zero-indexed array A consisting of N integers is given. An equilibrium index
        of this array is any integer P such that 0 ≤ P < N and the sum of elements of
        lower indices is equal to the sum of elements of higher indices, i.e.
        A[0] + A[1] + ... + A[P−1] = A[P+1] + ... + A[N−2] + A[N−1].
        Sum of zero elements is assumed to be equal to 0. This can happen if P = 0 or
        if P = N−1.

        For example, consider the following array A consisting of N = 8 elements:
        A[0] = -1
        A[1] = 3
        A[2] = -4
        A[3] = 5
        A[4] = 1
        A[5] = -6
        A[6] = 2
        A[7] = 1

        P = 1 is an equilibrium index of this array, because:
        A[0] = −1 = A[2] + A[3] + A[4] + A[5] + A[6] + A[7]
        P = 3 is an equilibrium index of this array, because:

        A[0] + A[1] + A[2] = −2 = A[4] + A[5] + A[6] + A[7]
        P = 7 is also an equilibrium index, because:

        A[0] + A[1] + A[2] + A[3] + A[4] + A[5] + A[6] = 0
        and there are no elements with indices greater than 7.

        P = 8 is not an equilibrium index, because it does not fulfill the condition 0 ≤ P < N.

        Write a function:

        def solution(a)

        that, given a zero-indexed array A consisting of N integers, returns any of
        its equilibrium indices. The function should return −1 if no equilibrium index exists.

        For example, given array A shown above, the function may return 1, 3 or 7, as explained above.

        Assume that:

        N is an integer within the range [0..100,000];
        each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
        Complexity:

        expected worst-case time complexity is O(N);
        expected worst-case space complexity is O(N), beyond input storage
        (not counting the storage required for input arguments).
        Elements of input arrays can be modified.
        """

    left_sum, right_sum = {}, {}

    for key, val in enumerate(array):
        if key == 0:
            left_sum[key] = 0
            right_sum[len(array) - 1] = 0
        else:
            left_sum[key] = array[key - 1] + left_sum[key - 1]
            right_sum[len(array) - key - 1] = array[len(array) - key] + right_sum[len(array) - key]

    return_keys = []

    for key, val in enumerate(array):
            if left_sum[key] == right_sum[key]:
                return_keys.append(key)

    if len(return_keys) > 0:
        return return_keys

    return -1


assert(equilibrium([-1, 3, -4, 5, 1, -6, 2, 1]) == [1, 3, 7])
assert(equilibrium([-1, 3]) == -1)
assert(equilibrium([-1, 1, -1, 0, 0]) == [0, 1, 2])
assert(equilibrium([2, -1, 1, -1, 0, 0]) == -1)
assert(equilibrium([]) == -1)
assert(equilibrium([1]) == [0])
assert(equilibrium([-2, 147, 483, 147, 483, 647]) == -1)
