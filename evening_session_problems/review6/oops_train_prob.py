# Due to unforseen circumstances in Suburbia, the trains will be delayed by a further 10 minutes.
# Create a function that will help to plan out and manage these delays! Create a function called manage_delays that
# does the following:
# Parameters will be the train object, a destination and number of minutes the delay is.
# Increment to the train object's expected_time by the delay, if the destination given is in the train object's
# destinations.
# Examples
# trains = [
#   Train(["Townsville", "Suburbia", "Urbantska"], "13:04"),
#   Train(["Farmsdale", "Suburbia", "Lakeside Valley"], "13:20"),
#   Train(["Suburbia", "Townsville", "Lakeside Valley"], "13:22")
# ]
# for t in trains:
#     manage_delays(t, "Lakeside Valley", 60)
# trains[0].expected_time ➞ "13:04"
# trains[1].expected_time ➞ "14:20"
# trains[2].expected_time ➞ "14:22"




# class Train:
#     def _init_(self, destinations, expected_time):
#         self.destinations = destinations
#         self.expected_time = expected_time
#
#
# def manage_delays(t, destination, delay_minutes):
#     if destination in t.destinations:
#         delay_hrs = str(delay_minutes / 60)
#         h1, m1 = map(int, delay_hrs.split('.'))
#         h2, m2 = map(int, t.expected_time.split(':'))
#         t.expected_time = f'{h1 + h2}:{m1 + m2}'
#         return t
#     return t
#
#
# trains = [
#     Train(["Townsville", "Suburbia", "Urbantska"], "13:04"),
#     Train(["Farmsdale", "Suburbia", "Lakeside Valley"], "13:20"),
#     Train(["Suburbia", "Townsville", "Lakeside Valley"], "13:22")
# ]
#
# for tr in trains:
#     a = manage_delays(tr, "Lakeside Valley", 60)
# print(trains[0].expected_time)
# print(trains[1].expected_time)
# print(trains[2].expected_time)


def bucketize(a_str, n):
    a_list = a_str.split(" ")
    a = []
    b = ''
    # for j in range(len(a_str)):
    for b_str in a_list:
        if len(b) + len(b_str) <= n:
            b += " " + b_str if b else b_str
        else:
            a.append(b)
            b = b_str
    if b :
        a.append(b)

    # print(b)
    return a