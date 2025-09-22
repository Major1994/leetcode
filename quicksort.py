def quick_sort(arr, start, end):

    if len(arr) == 0 or len(arr) == 1:
        return arr

    if len(arr) == 2:
        if arr[0] > arr[1]:
            tmp = arr[1]
            arr[0] = arr[1]
            arr[1] = tmp

    if start > end:
        return

    # 取起始指针值做哨兵
    sentinel = arr[start]

    left = start # move to right
    right = end # move to left

    while left < right:
        # 右指针的值大于哨兵，右指针左移
        while arr[right] >= sentinel:
            right -= 1
        # 退出循环时 右指针的值 小于哨兵，把右指针值赋给左指针
        arr[left] = arr[right]

        # 左指针的值小于哨兵，左指针右移
        while arr[left] <= sentinel:
            left += 1
        # 退出循环时 左指针的值 大于哨兵，把左指针值赋给右指针
        arr[right] = arr[left]

    # 循环结束时 左右指针指向同一个位置，
    # 此位置左边小于哨兵值，右边大于哨兵值,
    # 此位置赋哨兵值，为哨兵位
    # 哨兵位的左半只 全部小于 右半只，值域不重叠，可以单独排序
    sentinel_index = left
    arr[sentinel_index] = sentinel


    # 递归调用快速排序，哨兵的左半只和右半只 各自 单独排序
    quick_sort(arr, start, sentinel_index)
    quick_sort(arr, sentinel_index, end)

