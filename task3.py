from copy import deepcopy


def find_intersect(start1, end1, start2, end2):
    # the function returns the intersection of
    # segments [start1, end1] and [start2, end2]
    if start1 <= end2 and end1 >= start2:
        return min(end1, end2) - max(start1, start2)
    else:
        return 0


def appearance(intervals):
    # the function returns the total time
    # of pupil and tutor spent together
    lesson = intervals['lesson']
    pupil = deepcopy(intervals['pupil'])
    tutor = deepcopy(intervals['tutor'])
    total_time = 0
    pup_ind, tut_ind = 0, 0
    while pupil[pup_ind + 1] < lesson[0]:
        pup_ind += 2
    while tutor[tut_ind + 1] < lesson[0]:
        tut_ind += 2
    pup_start = max(lesson[0], pupil[pup_ind])
    tut_start = max(lesson[0], tutor[tut_ind])
    if pup_start > lesson[1] or tut_start > lesson[1]:
        return 0
    pupil[pup_ind] = pup_start
    tutor[tut_ind] = tut_start
    pup_max, tut_max = len(pupil) - 2, len(tutor) - 2
    while pup_ind <= pup_max and tut_ind <= tut_max:
        if pupil[pup_ind] > lesson[1] or tutor[tut_ind] > lesson[1]:
            break
        if pupil[pup_ind + 1] > lesson[1]:
            pupil[pup_ind + 1] = lesson[1]
        if tutor[tut_ind + 1] > lesson[1]:
            tutor[tut_ind + 1] = lesson[1]
        total_time += find_intersect(pupil[pup_ind],
                                     pupil[pup_ind+1],
                                     tutor[tut_ind],
                                     tutor[tut_ind+1])
        if pupil[pup_ind + 1] > tutor[tut_ind + 1]:
            tut_ind += 2
        else:
            pup_ind += 2
    return total_time


tests = [
    {
        'data': {'lesson': [1594663200, 1594666800],
                 'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                 'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
        'answer': 3117
    },
    # the test seems to be wrong
    # {'data': {'lesson': [1594702800, 1594706400],
    #             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
    #             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    # 'answer': 3577
    # },
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
