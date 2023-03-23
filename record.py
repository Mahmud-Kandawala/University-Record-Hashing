import array

hashTable = [None] * 8011 # Double of 4000 and is Prime 

def hashFunc(num):
    return num % 8011

def Probe(hashTable, record):
    i = 1
    while hashTable[(record + i*i) % 8011] is not None:
        i += 1
    return (record + i*i) % 8011

def Add():
    num = int(input("Enter Student Number: "))
    record = hashFunc(num)
    if hashTable[record] is None:
        hashTable[record] = num
    else:
        record = Probe(hashTable, record)
        hashTable[record] = num
    print("Added Student Record!")

def Output():
    for i in range(len(hashTable)):
        if hashTable[i] is not None:
            print(i, ":", hashTable[i])

def Find():
    num = int(input("Enter Student Number: "))
    record = hashFunc(num)
    if hashTable[record] == num:
        print("Student record found at: Record (Index)", record)
    else:
        i = 1
        while hashTable[(record + i*i) % 8011] != num and hashTable[(record + i*i) % 8011] is not None:
            i += 1
        if hashTable[(record + i*i) % 8011] == num:
            print("Student record found at: Record (Index)", (record + i*i) % 8011)
        else:
            print("Student record Not Found!")

def Delete():
    num = int(input("Enter Student Number: "))
    record = hashFunc(num)
    if hashTable[record] == num:
        hashTable[record] = None
        print("Deleted Student Record!")
    else:
        i = 1
        while hashTable[(record + i*i) % 8011] != num and hashTable[(record + i*i) % 8011] is not None:
            i += 1
        if hashTable[(record + i*i) % 8011] == num:
            hashTable[(record + i*i) % 8011] = None
            print("Deleted Student Record!")
        else:
            print("Student record Not Found!")

while True:
    print("\nMenu:")
    print("1. Add a new student number to the hash table")
    print("2. Print out the hash table")
    print("3. Find a students record using his/her number")
    print("4. Delete a student record using probing")
    print("5. Exit")
    pick = int(input("\nEnter your pick: "))
    if pick == 1:
        Add()
    elif pick == 2:
        Output()
    elif pick == 3:
        Find()
    elif pick == 4:
        Delete()
    elif pick == 5:
        print("Program has ended, Bye!")
        break
    else:
        print("Invalid pick, Try Again!")



### Programs outputs records a little different