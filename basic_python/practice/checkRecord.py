# 学生出勤记录 I
def checkRecord(s: str):
    if s.count('A') > 1 or s.count('LLL') > 0:
        return False
    return True


print(checkRecord('PAPLPLL'))