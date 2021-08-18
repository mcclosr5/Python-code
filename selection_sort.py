def selection_sort(lst):
    comparecount = 0
    movecount = 0
    lo = 0
    hi = len(lst) - 1
    while lo < hi:
        min_index = lo
        max_index = lo
        for j in range(lo + 1, hi + 1):
            comparecount += 1
            if lst[j] < lst[min_index]:
                min_index = j
            elif lst[j] > lst[max_index]: # maybe >= to get stable sort
                max_index = j
                comparecount += 1
            else:
                comparecount += 1
        if max_index == lo:
            max_index = min_index   # We will be moving lst[lo] to min_index, so update max_index first

        # swap min index with lo ... place smallest at the first
        lst[lo], lst[min_index] = lst[min_index], lst[lo]
        movecount += 3
        # swap max index with hi ... place largest at the end
        lst[hi], lst[max_index] = lst[max_index], lst[hi]
        movecount += 3
        lo += 1
        hi -= 1
    return comparecount, movecount