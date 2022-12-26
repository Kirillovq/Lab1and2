def mel(num):
    count = 0
    while num != 0:
      count = max(count, num % 10)
      num //= 10
    return count


print(mel(6900))