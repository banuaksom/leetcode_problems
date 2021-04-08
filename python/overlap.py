from __future__ import print_function


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def overlap(intervals):
    intervals.sort(key = lambda x: x.start)
    
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]

        if interval.start <= end:
            return True
        else:
            start = interval.start
            end = interval.end
    
    return False

if __name__ == '__main__':
    print(overlap([Interval(1, 4), Interval(5, 5), Interval(6, 9)]))