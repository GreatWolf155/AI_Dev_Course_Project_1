#I did not put too much effort into naming things well,
# but i did check that each part works properly

#if not explicitly requested to make a function for an example,
#then i did not make a function for it

#The first few functions run automatically
#with the given data from the homework dataset

def ex_1():
    for i in range (12,25):
        print(i)

def ex_2():
    for i in range (7,32):
        if i%2 == 1:
            print(i)

def ex_3():
    for i in range (10,-21, -1):
        if i%2 == 0:
            print(i)

def ex_4():
    for i in range (1, 46):
        fizz = buzz = ""
        if i%3 == 0:
            fizz = "Fizz"
        if i%5 == 0:
            buzz = "Buzz"
        if fizz or buzz != "":
            print(f"{fizz}{buzz}")

def ex_5(arr):
    result = 0
    for num in arr:
        result += num
    return result

def ex_6_1(objects, change):
    for object in objects:
        if change in object.keys():
            object.pop(change)
    return objects

def ex_6_2(objects):
    for dict in objects:
        for key, value in dict.items():
            print(f"{key}: {value}")

def ex_6_3(objects): #receives an array of dictionaries (people)
    #This was a horrible exercise and I never want to do it again (XnX)
    #I kept getting results from Gemini to use a second function,
    #to keep things simple, but that was not part of the assignment
    sorted_list = []
    array = objects.copy()
    while array:
        oldest_person = None
        oldest_age = -1  # Initialize with a value lower than any expected age
        for dictionary in array: #Find the oldest person
            current_age = dictionary['age']
            if current_age >= oldest_age: #Check if the current person is older than the current "oldest_person"
                oldest_age = current_age
                oldest_person = dictionary
        if oldest_person:
            sorted_list.append(oldest_person)  # Append it to the new sorted list
            array.remove(oldest_person)  # Remove it from the original list
    return sorted_list

def ex_7_1(pets):
    cats = []
    for dict in pets:
        for key, value in dict.items():
            if value == "cat":
                cats.append(dict)
    print(cats)

def ex_7_2(pets, animal):
    for dict in pets:
        for key, value in dict.items():
            if key == "animal_type" and value == animal:
                print(dict.get("names"))

def ex_7_3(pets, name):
    for dict in pets:
        if name not in dict.get("names"):
            dict.get("names").append(name)

def ex_8_1(student):
    for key, value in student.items():
        print(f"{key}: {value}")

def ex_8_2(student, hobby):
    if hobby not in student.get("hobbies"):
        student.get("hobbies").append(hobby)
    ex_8_1(student)

def ex_8_3(student, hobby):
    if hobby in student.get("hobbies"):
        student.get("hobbies").remove(hobby)
        ex_8_1(student)

def print_matrix(matrix):
    str_print = []
    for row in matrix:
        for col in row:
            item = str(col) #because otherwise it's an int
            str_print.append(item)
    print(" ".join(str_print))

def zero_count(matrix):
    count = 0
    for row in matrix:
        for col in row:
            if col == 0:
                count += 1
    return count

def find_dup(arr):
    dupes = []
    for num in arr:
        if arr.count(num) > 1:
            if num not in dupes:
                dupes.append(num)
    return dupes

def new_reverse(arr):
    new_arr = []
    while True:
        if arr:
            new_arr.append(arr[-1])
            arr.pop(-1)
        else:
            break
    return new_arr

def sum_arrays(arr1, arr2):
    sum_array = []
    for i in range(0, len(arr1)):
        sum_array.append(arr1[i] + arr2[i])
    return sum_array

def check_palindrome(string1, string2):
    str1_pal = str2_pal = False
    str1 = list(string1.lower().strip())
    str2 = list(string2.lower().strip())
    str1.reverse()
    str2.reverse()
    if str1 == list(string1.lower().strip()):
        str1_pal = True
    if str2 == list(string2.lower().strip()):
        str2_pal = True
    print(f"{str1_pal} (for first_str)\n"
          f"{str2_pal} (for second_str)")

def find_str_dupes(arr):
    dupes = []
    while arr:
        if arr[0] not in dupes:
            dupes.append(arr[0])
        arr.pop(0)
    return dupes

def find_str_dupe_minus_pete(arr):
    dupes = []
    while arr:
        if arr[0] not in dupes and arr[0].lower() != 'pete':
            dupes.append(arr[0])
        arr.pop(0)
    return dupes

def test_arr(arr):
    i=1
    index = 1
    while True:
        if i == len(arr) or arr[i] == arr[i - 1]:
            break
        if arr[i] != arr[i - 1]:
            index += 1
        i+=1
    if index == len(arr):
        return -1
    return index



if __name__ == "__main__":

    ex_1()


    ex_2()


    ex_3()


    ex_4()


    # ex_5
    array = [1,13,22,123,49,34,5,24,57,45]
    added = ex_5(array)
    print(added)


    # ex_6
    arr_obj = [
        {"id_num": 1, "first name": "Yosef", "last name": "Greenfield", "age": 29, "country": "Israel", "city": "Karmiel"},
        {"id_num": 2, "first name": "Bibi", "last name": "Netanyahu", "age": 76, "country": "Israel", "city": "Tel Aviv"},
        {"id_num": 3, "first name": "Donald", "last name": "Trump", "age": 79, "country": "USA", "city": "Washington D.C."}
    ]
    change = input("please input a parameter to remove\n")
    arr_obj_2 = ex_6_1(arr_obj, change)
    ex_6_2(arr_obj_2)
    sorted_dict = ex_6_3(arr_obj_2)
    for dict in sorted_dict:
        for key, value in dict.items():
            print(f"{key}: {value}")


    # ex_7
    our_pets = [
        {
            "animal_type": "cat",
            "names": [
                "Meowzer",
                "Fluffy",
                "Kit-Cat"
            ]
        },
        {
            "animal_type": "dog",
            "names": [
                "Spot",
                "Bowser",
                "Frankie"
            ]
        }
    ]
    ex_7_1(our_pets)
    animal_type = input("please input animal type\n")
    ex_7_2(our_pets, animal_type)
    animal_name = input("please input the animal's name\n")
    ex_7_3(our_pets, animal_name)


    # ex_8
    student = {
        'name': 'John',
        'age': 20,
        'hobbies': ['reading', 'games', 'coding'],
    }
    ex_8_1(student)
    hobby = input("please input the hobby to add\n")
    ex_8_2(student, hobby)
    hobby = input("please input the hobby to remove\n")
    ex_8_3(student, hobby)
    student.update({"family_name":"Jefferson"})


    # ex_9
    matrix =[
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    print_matrix(matrix)


    # ex_10
    matrix = [
        [0, 1, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]
    print(zero_count(matrix))


    # ex_11
    arr = [4, 2, 34, 4, 1, 12, 1, 4]
    print(find_dup(arr))


    # ex_12
    arr = input("please input array\n")
    # arr = [43, "what", 9, True, "cannot", False, "be", 3, True]
    new_reverse(arr)


    # ex_13
    first_array = [4, 6, 7]
    second_array = [8, 1, 9]
    sum_arrays(first_array, second_array)


    # ex_14
    first_str = "racecar"
    second_str = "Java"
    check_palindrome(first_str, second_str)


    # ex_15
    count = 1
    while count < 100:
        count *= 2


    # ex_16
    count = 900000
    while count > 50:
        count /= 2


    # ex_17, ex_18
    names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
    print(find_str_dupes(names))


    # ex_19
    names = ['Chris', 'Kevin', 'Naveed', 'Pete', 'Victor', 'Chris', 'Kevin']
    print(find_str_dupe_minus_pete(names))


    # ex_20
    array = [True, False, False, True, True, False]
    print(test_arr(array))
    array = [True, False, True, False, True, True]
    print(test_arr(array))
    array = [True, False, True, False, True, False,]
    print(test_arr(array))


    # ex_21
    while True:
        full_name = input("please input user full name\n")
        name = full_name.split(" ")
        if len(name) == 2 and name[0].isalpha() and name[1].isalpha():
            break
        else:
            print("ERROR\nPlease input first and last name only")
    while True:
        try:
            user_age = int(input("please input user age\n"))
            break
        except ValueError:
            print("ERROR\nPlease input age in numbers")
            continue
    while True:
        user_email = input("please input user email\n")
        email = user_email.split(" ")
        if len(email) == 2:
            break
        else:
            print("ERROR\nPlease input proper email")