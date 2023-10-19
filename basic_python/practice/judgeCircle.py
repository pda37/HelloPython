def judgeCircle(moves):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')


print(judgeCircle('UDUDRLRL'))