SAMPLE = [
    ["02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]],
    ["99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]],
    ["50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]]
]

class Time:
    def __init__(self, time):
        hour, minute, second = list(map(int, time.split(":")))
        self.hour = hour
        self.minute = minute
        self.second = second

    def display(self):
        print(self.hour, self.minute, self.second)

    def addTime(self, other):
        self.second += other.second
        if self.second >= 60:
            self.minute += 1
            self.second -= 60

        self.minute += other.minute
        if self.minute >= 60:
            self.hour += 1
            self.minute -= 60

        self.hour += other.hour

    def is_left(self, other):
        if self.is_equal(other):
            return False

        if self.hour < other.hour:
            return True
        elif self.hour > other.hour:
            return False
        else:
            if self.minute < other.minute:
                return True
            elif self.minute > other.minute:
                return False
            else:
                if self.second < other.second:
                    return True
                elif self.second > other.second:
                    return False

    def is_equal(self, other):
        if self.hour == other.hour and self.minute == other.minute and self.second == other.second:
            return True
        else:
            return False


def solution(play_time, adv_time, logs):
    answer = ''

    pt = Time(play_time)
    at = Time(adv_time)

    logs.sort()
    print(logs)

    st_list = []
    ed_list = []

    for log in logs:
        start, end = list(map(Time, log.split("-")))
        st_list.append(start)
        ed_list.append(end)


    for idx in range(len(logs)):
        adv_start = st_list[idx]
        st_list[idx].hour += 1
        st_list[idx].display()
        adv_start.display()








    return answer


for i in range(len(SAMPLE)):
    print(i+1, "번 케이스")
    play_time, adv_time, logs = SAMPLE[i]
    print(play_time, adv_time, logs)
    print(solution(play_time, adv_time, logs))