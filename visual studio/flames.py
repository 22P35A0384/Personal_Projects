def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()
    common_letters = set(name1).intersection(set(name2))
    flames_count = len(name1) + len(name2) - 2 * len(common_letters)
    flames = "flames"
    while len(flames) > 1:
        split_index = flames_count % len(flames) - 1
        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames = flames[:len(flames) - 1]
    return flames

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")
print(flames_game(name1, name2))
