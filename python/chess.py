# 1 point if wins, 0 poins if looses, 0.5 points if drew 
# given number of points, number of games and number od loss
# return how many games were won and how many ended in a draw


def chess(points: int, numGames: int, numLoss: int) -> int:
    # calculate how many points were not gained fully
    # max number of points == number of total games
    not_gained = numGames - points - numLoss

    # calculate number of games ended in a draw (1*won_games + 0.5*draw = 14 points)
    # 0.5*draw = not_gained
    draw = int(2 * not_gained)

    # calculate number of won games 
    won = numGames - draw - numLoss

    return (f'{won} games are won and {draw} games ended in a draw')        

if __name__ == '__main__':
    print(chess(10.5, 15, 1))
    print(chess(10.5, 18, 2))
    print(chess(11.5, 15, 1))
    