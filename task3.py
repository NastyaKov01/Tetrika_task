def find_intersect(start1, end1, start2, end2):
    # the function returns the intersection of
    # segments [start1, end1] and [start2, end2]
    if start1 <= end2 and end1 >= start2:
        return min(end1, end2) - max(start1, start2)
    else:
        return 0


def merge_intervals(intervals, lesson):
    # the function merges intersections
    ind_max = len(intervals)
    start_ind = 0
    while intervals[start_ind + 1] < lesson[0]:
        start_ind += 2
    while intervals[ind_max-2] > lesson[1]:
        ind_max -= 2
    start = max(lesson[0], intervals[start_ind])
    end = min(lesson[1], intervals[start_ind+1])
    new_intervals = list()
    for ind in range(start_ind + 2, ind_max, 2):
        cur_start = max(lesson[0], intervals[ind])
        cur_end = min(lesson[1], intervals[ind+1])
        intersect = find_intersect(start, end, cur_start, cur_end)
        if intersect != 0:
            start = min(start, cur_start)
            end = max(end, cur_end)
        else:
            new_intervals.append((start, end))
            start = cur_start
            end = cur_end
    new_intervals.append((start, end))
    return new_intervals

def appearance(intervals):
    # the function returns the total time
    # of pupil and tutor spent together
    total_time = 0
    new_tutor = merge_intervals(intervals['tutor'], intervals['lesson'])
    new_pupil = merge_intervals(intervals['pupil'], intervals['lesson'])
    tut_max = len(new_tutor)
    pup_max = len(new_pupil)
    for tut_ind in range(tut_max):
        for pup_ind in range(pup_max):
            total_time += find_intersect(new_pupil[pup_ind][0],
                                         new_pupil[pup_ind][1],
                                         new_tutor[tut_ind][0],
                                         new_tutor[tut_ind][1])
    return total_time


tests = [
    {
        'data': {'lesson': [1594663200, 1594666800],
                 'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                 'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
        'answer': 3117
    },
    {
        'data': {'lesson': [1594702800, 1594706400],
                'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
                'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
        'answer': 3577
    },
    {
        'data': {'lesson': [1594692000, 1594695600],
                 'pupil': [1594692033, 1594696347],
                 'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
        'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
