student_list = ['John', 'Dohn', 'Khon', 'Moon', 12]
student_info = ('John', 'Dohn', 'Khon', 'Moon', 'Moon', 12)
# tuple
def get_studnets_name():
    for items in student_list:
        print('First item {}'.format(items))
    print('****************')
    for i in range(2,3):   # 2 #  2 >= range < 3
        print('First item {}'.format(student_list[i]))

    # if condition:    # condition --> True or False
    #     do

    if student_list[0] == 'Joh' or len(student_list[0])==4 : # false and true --> true
        print('A very good boy!!!')
    elif student_list[1] == 'John':
        print('Bad Boy!!!')

    print('Outside if else block')

def tuple_demo():
    print(len(student_info))
    #student_info[6]= 14
    for i in student_info:
        print(i)
    list_of_tuples = [  
                        ('Swordfish', 'Dominic Sena', 2001), 
                        ('Snowden', ' Oliver Stone', 2016), 
                        ('Taxi Driver', 'Martin Scorsese', 1976)
                     ]
    list_of_tuples.remove(('Swordfish', 'Dominic Sena', 2001))
    for i in list_of_tuples:
        print(i)
    list_of_tuples.append(('Swordfish', 'Dominic Sena', 2001))
    list_of_tuples[1] = ('Swordfish', 'Dominic Sena', 2001)

    for i in list_of_tuples:
        print('After append operation {}'.format(i))
    print(x for x in list_of_tuples)

if __name__ == "__main__":
    #get_studnets_name()
    tuple_demo()
