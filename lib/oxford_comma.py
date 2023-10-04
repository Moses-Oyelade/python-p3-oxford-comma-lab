


def oxford_comma(items):
    
    new_list = []
    for index in range(len(items)):
        new_list.append(f"{items[index]}," if index < len(items) -1 else f"and {items[index]}")
        
    return " ".join(new_list)
print(oxford_comma(["man", "woman", "girl", "boy"]))
print(oxford_comma(["kiwi", "durian", "starfruit", "mangos", "dragon fruits"]))
print(oxford_comma(["kiwi", "durian", "starfruit", "mangos", "dragon fruits", "lychees", "pomelos"]))


# def oxford_comma(items: list) -> str:

#     new_list = []
#     for i in range(len(items)):
#         new_list.append(f"{items[i]}," if i < len(items) - 1 else f"and {items[i]}")
        
#     return " ".join(new_list)
# print(oxford_comma(["man", "woman", "girl", "boy"]))