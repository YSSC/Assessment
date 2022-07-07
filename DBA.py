list_record = [["Set B", "Kyle Leonard", 5, 240.60],
               ["Set A","Noah Park",3,300.30],
               ["Set E","Desmund Kalid",6,90.85],
               ["Set D","Daryl Law",2,110.40],
               ["Set C","Anya Forgers",3,150.90]]


def menuchoices():
    print("0. Display choices")
    print("1. Display all records")
    print("2. Sort record by Customer Name using Bubble sort")
    print("3. Sort record by Package Name using Selection sort")
    print("4. Sort record by Package Cost using Insertion sort")
    print("5. Search record by Customer Name using Linear Search and update record")
    print("6. Search record by Package Name using Binary Search and update record")
    print("7. List records range from $X to $Y. e.g $100-200")
    print("8. Quicksort Number of Pax")

def bubbleSort(list_record):
    pos = 1
    list_length = len(list_record)

    for i in range(0, list_length):
        for j in range(0, list_length-i-1):
            if (list_record[j][pos] > list_record[j + 1][pos]):
                temp = list_record[j]
                list_record[j]= list_record[j + 1]
                list_record[j + 1]= temp

    for index, tuple in enumerate(list_record):
        element_one = tuple[0]
        element_two = tuple[1]
        element_three = tuple[2]
        element_four = tuple[3]
        print(element_one, element_two,element_three,element_four)

def selectionSort(theSeq):
    n = len(theSeq)

    for i in range(n - 1):
        # Assume the ith element is the smallest.
        smallNdx = i

        # Determine if any other element contains a smaller value.
        for j in range(i + 1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j

        # Swap the ith value and smallNdx value only if the smallest
        # value is not already in its proper position.
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp


def insertionSort(list_record):
    n = len(list_record)
    # Starts with the first item as the only sorted entry.
    for i in range(0, n):
        # Save the value to be positioned
        value = list_record[i][3]
        value_obj = list_record[i]
        # Find the position where value fits in the
        # ordered part of the list.
        posi = i
        while posi > 0 and value < list_record[posi - 1][3]:
            # Shift the items to the right during the search
            list_record[posi] = list_record[posi - 1]
            posi -= 1

        # Put the saved value into the open slot.
        list_record[posi] = value_obj


def search(arr, n, x):
    for i in range(0, n):
        if ((arr[i][1]).upper() == x):
            return i
    return -1


def binarySearch(arr, l, r, x):
    arr = sorted(list_record)
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if (arr[mid][0].upper()) == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif (arr[mid][0].upper()) > x:
            return binarySearch(arr, l, mid - 1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1

# Quick sort in Python
# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j][2] <= pivot[2]:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)

n = len(list_record)

def menu():
    menuchoices()
    while True:
        try:
            you = int(input("Please choose between 0-8? "))

            if you == 0:
                menuchoices()

            elif you == 1:
                for index, tuple in enumerate(list_record):
                    element_one = tuple[0]
                    element_two = tuple[1]
                    element_three = tuple[2]
                    element_four = tuple[3]
                    print(element_one, element_two, element_three, element_four)
                menu()

            elif you == 2:
                bubbleSort(list_record)
                menu()

            elif you == 3:
                selectionSort(list_record)
                for index, tuple in enumerate(list_record):
                    element_one = tuple[0]
                    element_two = tuple[1]
                    element_three = tuple[2]
                    element_four = tuple[3]
                    print(element_one, element_two, element_three, element_four)
                menu()

            elif you == 4:
                insertionSort(list_record)
                for index, tuple in enumerate(list_record):
                    element_one = tuple[0]
                    element_two = tuple[1]
                    element_three = tuple[2]
                    element_four = tuple[3]
                    print(element_one, element_two, element_three, element_four)
                menu()

            elif you == 5:
                while True:
                    while True:
                        x = input("Enter a NAME to search: ").upper()
                        result = search(list_record, n, x)

                        if (result == -1):
                            print("Name NOT FOUND in Record!!")
                        else:
                            print("Record Found!!")
                            print("Package Name: " + (list_record[result][0]) + ",", "Customer Name:",
                                  (list_record[result][1]) + ",",
                                  "No. of Pax: " + str(list_record[result][2]) + ",", "Package Cost Per Pax:",
                                  "$(" + str(list_record[result][3]) + ")"
                                  )
                            break

                    while True:
                        P_name = str(input("Enter Package Name: "))
                        if P_name.upper() == "SET A":
                            break
                        if P_name.upper() == "SET B":
                            break
                        if P_name.upper() == "SET C":
                            break
                        if P_name.upper() == "SET D":
                            break
                        if P_name.upper() == "SET E":
                            break
                        if P_name.upper() == "SET F":
                            break
                        else:
                            print("Invalid Package Set")

                    while True:
                        C_name = input("Enter Full Name: ")
                        if len(C_name) == 0:
                            print("Empty Full Name. Please try again.")
                        else:
                            break

                    while True:
                        try:
                            Pax_No = int(input("Enter Number of Pax: "))
                            if Pax_No == 0:
                                print("Pax_No cannot be 0. Please try again.")
                            else:
                                break
                        except ValueError:
                            print("Oops!  That was no valid number.  Try again...")

                    if P_name.upper() == "SET A":
                        pack_cost = float(300.30)
                        print(pack_cost)
                    elif P_name.upper() == "SET B":
                        pack_cost = float(240.60)
                        print(pack_cost)
                    elif P_name.upper() == "SET C":
                        pack_cost = float(150.90)
                        print(pack_cost)
                    elif P_name.upper() == "SET D":
                        pack_cost = float(110.40)
                        print(pack_cost)

                    elif P_name.upper() == "SET E":
                        pack_cost = float(90.85)
                        print(pack_cost)

                    elif P_name.upper() == "SET F":
                        pack_cost = float(70.85)
                        print(pack_cost)

                    y = list(list_record)
                    y[result][0] = P_name
                    y[result][1] = C_name
                    y[result][2] = Pax_No
                    y[result][3] = pack_cost

                    # x = list(y)
                    # print(x)

                    print("New Updated Recorded!")
                    for index, tuple in enumerate(list_record):
                        element_one = tuple[0]
                        element_two = tuple[1]
                        element_three = tuple[2]
                        element_four = tuple[3]
                        print(element_one, element_two, element_three, element_four)
                    menu()



            elif you == 6:
                x = input("Enter a PACKAGE NAME to search: ").upper()
                selectionSort(list_record)

                # Function call
                result = binarySearch(list(list_record), 0, len(list_record) - 1, x)

                if result != -1:
                    print("Package Name: " + (list_record[result][0]) + ",", "Customer Name:", (list_record[result][1]) + ",",
                          "No. of Pax: " + str(list_record[result][2]) + ",", "Package Cost Per Pax:",
                          "$(" + str(list_record[result][3]) + ")"
                          )
                else:
                    print("Element is not present in array")
                while True:
                    P_name = str(input("Enter Package Name: "))
                    if P_name.upper() == "SET A":
                        break
                    if P_name.upper() == "SET B":
                        break
                    if P_name.upper() == "SET C":
                        break
                    if P_name.upper() == "SET D":
                        break
                    if P_name.upper() == "SET E":
                        break
                    if P_name.upper() == "SET F":
                        break
                    else:
                        print("Invalid Package Set")

                while True:
                    C_name = input("Enter Full Name: ")
                    if len(C_name) == 0:
                        print("Empty Full Name. Please try again.")
                    else:
                        break

                while True:
                    try:
                        Pax_No = int(input("Enter Number of Pax: "))
                        if Pax_No == 0:
                            print("Pax_No cannot be 0. Please try again.")
                        else:
                            break
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")

                if P_name.upper() == "SET A":
                    pack_cost = float(300.30)
                    print(pack_cost)
                elif P_name.upper() == "SET B":
                    pack_cost = float(240.60)
                    print(pack_cost)
                elif P_name.upper() == "SET C":
                    pack_cost = float(150.90)
                    print(pack_cost)
                elif P_name.upper() == "SET D":
                    pack_cost = float(110.40)
                    print(pack_cost)

                elif P_name.upper() == "SET E":
                    pack_cost = float(90.85)
                    print(pack_cost)

                elif P_name.upper() == "SET F":
                    pack_cost = float(70.85)
                    print(pack_cost)

                y = list(list_record)
                y[result][0] = P_name
                y[result][1] = C_name
                y[result][2] = Pax_No
                y[result][3] = pack_cost

                # x = list(y)
                # print(x)

                print("New Updated Recorded!")
                for index, tuple in enumerate(list_record):
                    element_one = tuple[0]
                    element_two = tuple[1]
                    element_three = tuple[2]
                    element_four = tuple[3]
                    print(element_one, element_two, element_three, element_four)

                menu()

            elif you == 7:
                while True:
                    try:
                        x = float(input('Starting range: $'))
                        y = float(input('Ending range: $'))
                        insertionSort(list_record)
                        count = 0
                        sortedata = {}
                        for i in range(len(list_record)):
                            if x <= list_record[i][3] <= y:
                                sortedata[count] = list_record[i]
                                count += 1

                        for key in sortedata:
                            print("Package Name: " + (sortedata[key][0]) + ",", "Customer Name:", (sortedata[key][1]) + ",",
                                  "No. of Pax: " + str(sortedata[key][2]) + ",", "Package Cost Per Pax:",
                                  "$(" + str(sortedata[key][3]) + ")")
                        menu()
                    except ValueError:
                        print("Oops!  That was no valid number.  Try again...")

            elif you == 8:
                size = len(list_record)
                quickSort(list_record, 0, size - 1)
                for index, tuple in enumerate(list_record):
                    element_one = tuple[0]
                    element_two = tuple[1]
                    element_three = tuple[2]
                    element_four = tuple[3]
                    print(element_one, element_two, element_three, element_four)
                menu()

            else:
                print("Invalid Choice")
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

menu()