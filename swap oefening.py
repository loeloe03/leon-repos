lijst = ['one', 'two', 'tree']

def swapFS(lijst):
    if len(lijst) > 1:
        lijst[0], lijst[1] = lijst[1], lijst[0]
    return lijst

print(swapFS(lijst))