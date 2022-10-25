def print_time_as_ascii(time):
  for i in range(5):
    for char in time:
      print(CHARS_TO_ASCII[char][i], end=" ")
    print()