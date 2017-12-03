from advent1Data import puzzle

def captcha(numbers):
    sum = 0
    i = 0
    while i < len(numbers):
        num = numbers[i]
        nextNum = numbers[(i+1) % len(numbers)]
        if num == nextNum:
            sum += int(num)
        i+=1
    print(sum)

captcha(puzzle)
