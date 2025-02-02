def display_pattern_while():
  i = 1
  while i <= 7:
    j = 0
    if i % 2 != 0:  
      while j < i:
        print(i, end="")
        j += 1
      print()
    elif i == 6:
        while j < i:
            print(i, end="")
            j += 1
        print()
    i += 1
display_pattern_while()