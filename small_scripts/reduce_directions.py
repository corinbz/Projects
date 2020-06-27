

def dirReduc(arr):
    result = arr
    not_valid = [
        ["NORTH", "SOUTH"],
        ["SOUTH", "NORTH"],
        ["WEST", "EAST"],
        ["EAST", "WEST"]
    ]
    running = True
    while running:
        running = False
        for i in range(len(arr) -1):
            if arr[i:i+2] in not_valid:
                del result[i:i+2]
                running = True

    print(result)


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
dirReduc(a)
