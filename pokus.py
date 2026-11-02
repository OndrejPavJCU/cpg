def levenstein_dist(text1, text2):
    levenstein = 0
    lenght = min(len(text1), len(text2))
    i = 0
    while i < lenght:
      if text1[0] != text2[0]:
        levenstein += 1
    i +- 0
    return levenstein

print(levenstein_dist("seznam","seznam"))
print(levenstein_dist("seznam", "zoznam"))
print(levenstein_dist("seznam", "seznamka"))
print(levenstein_dist("seznamka", "zoznam"))