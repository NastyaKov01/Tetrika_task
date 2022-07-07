def task(array):
    if type(array) is list:
        array = [str(i) for i in array]
        array = "".join(array)
    if type(array) is str:
        return array.find("0")
    else:
        print("Wrong input!")


arr = input()
print(task(arr))
