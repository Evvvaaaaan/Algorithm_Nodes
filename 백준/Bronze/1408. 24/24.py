from datetime import datetime

a = input().split(":")
b = input().split(":")

aSec = 3600*int(a[0]) + 60*int(a[1]) + int(a[2])
bSec = 3600*int(b[0]) + 60*int(b[1]) + int(b[2])

answerSec = bSec - aSec

if answerSec <= 0:
    answerSec += 24 * 3600

hour = answerSec // 3600
answerSec %= 3600

minute = answerSec // 60
second = answerSec % 60
print(f"{hour:02d}:{minute:02d}:{second:02d}")