# Given a list of non-overlapping intervals sorted by their start time
# insert a given interval at the correct position and
# merge all necessary intervals to
# return a list that has only mutually exclusive intervals

def insert(intervals, new_interval):
    merged = []
    start = new_interval[0]
    end = new_interval[1]
    i = 0

    # adding all intevals before new_interval
    while (i < len(intervals) and intervals[i][1] < start):
        merged.append(intervals[i])
        i += 1
  
    # merging all intervals between
    while (i < len(intervals) and intervals[i][0] <= end):
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    merged.append([start, end])

    # adding the rest intervals
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1


    return merged




def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()