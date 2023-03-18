# total_overs(2400) ➞ 400
# total_overs(164) ➞ 27.2
# # 27 overs and 2 balls were bowled by the bowler.
# total_overs(945) ➞ 157.3
# # 157 overs and 3 balls were bowled by the bowler.
# total_overs(5) ➞ 0.5

def total_overs(balls):
    if balls % 6 == 0:
        total_over = balls / 6
        return total_over
    else:
        ball_rem = balls % 6
        over = balls // 6
        total_over = ball_rem / 10 + over
        return total_over


print(total_overs(2400))
print(total_overs(164))