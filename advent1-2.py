from advent1Data import puzzle

def captcha2(numbers):
    length = len(numbers)
    half = int(length/2)
    sum = 0

    d = 0
    while d < length:
        num = numbers[d]
        nextNum = numbers[(d + half) % length]
        if num == nextNum:
            sum += int(num)
        d+=1

    print(sum)

captcha2(puzzle)
