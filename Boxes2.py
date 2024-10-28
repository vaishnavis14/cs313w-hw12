#  File: Boxes.py

#  Description:

#  Student Name: Vaishnavi Sathiyamoorthy

#  Student UT EID:

#  Partner Name: Pranav Kasibhatla

#  Partner UT EID: pvk249

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import sys


# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes(box_list):
    if len(box_list) <= 1:
        return 1, 1
    else:
        first = [1, box_list[0][0], box_list[0][1], box_list[0][2], 1, 1, 1, [1]]
        lst = memo(box_list, 1, [first])
        fitted_boxes = []
        # print(lst)
        for i in range(len(lst)):
            fitted_boxes.append(lst[i][7])

        num_sets = fitted_boxes
        index = len(num_sets) - 1
        while index >= 0:
            i = len(num_sets) - 2
            while i >= 0:
                is_in = True
                if num_sets[i] != num_sets[index]:
                    for k in range(len(num_sets[i])):
                        if num_sets[i][k] not in num_sets[index]:
                            is_in = False
                            break
                    if is_in == True:
                        num_sets.pop(i)
                        if index > i:
                            index -= 1
                    else:
                        i -= 1
                else:
                    i -= 1

            index -= 1

        if lst[len(lst) - 1][5] == 1:
            return 1, len(box_list)
        else:
            for i in range(len(lst)):
                print(lst[i])
            for i in range(len(num_sets)):
                print(num_sets[i])
            return lst[len(lst) - 1][5], len(num_sets)


def memo(box_list, box, mem):
    if len(mem) == len(box_list):
        return mem
    elif box > len(mem) - 1:
        inside = False
        index = box - 1

        while not inside:
            fit = does_fit(box_list[index], box_list[box])
            if fit == True:
                inside = True
                break
            if index == 0:
                index = box
                break
            index -= 1

        n_i = 0
        if index == box:
            n_i = 1
        else:
            n_i = 1 + mem[index][4]

        max_now = 0
        if n_i > mem[box - 1][5]:
            max_now = n_i
        else:
            max_now = mem[box - 1][5]

        r_i = 0
        if n_i == 1:
            r_i = box + 1
        else:
            r_i = index + 1

        boxes_inside = []
        if n_i == 1:
            boxes_inside.append(box + 1)
        else:
            boxes_inside = [box + 1]
            other_boxes = mem[index][7]
            boxes_inside += other_boxes

        mem.append([box + 1, box_list[box][0], box_list[box][1], box_list[box][2], n_i, max_now, r_i, boxes_inside])
        return memo(box_list, box + 1, mem)
    else:
        return mem[box]


# returns True if box1 fits inside box2
def does_fit(box1, box2):
    if (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2]):
        return True
    elif (box1[2] < box2[0] and box1[0] < box2[1] and box1[1] < box2[2]):
        return True
    elif (box1[1] < box2[0] and box1[2] < box2[1] and box1[0] < box2[2]):
        return True
    else:
        return False


def main():
    # read the number of boxes
    line = sys.stdin.readline()
    line = line.strip()
    num_boxes = int(line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range(num_boxes):
        line = sys.stdin.readline()
        line = line.strip()
        box = line.split()
        for j in range(len(box)):
            box[j] = int(box[j])
        box.sort()
        box_list.append(box)

    # print to make sure that the input was read in correctly
    # print (box_list)
    print()

    # sort the box list
    box_list.sort()

    # print the box_list to see if it has been sorted.
    # print (box_list)
    print()

    # get the maximum number of nesting boxes and the
    # number of sets that have that maximum number of boxes
    max_boxes, num_sets = nesting_boxes(box_list)

    # print the largest number of boxes that fit
    print(max_boxes)

    # print the number of sets of such boxes
    print(num_sets)


if __name__ == "__main__":
    main()


