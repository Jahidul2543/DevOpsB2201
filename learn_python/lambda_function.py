import sys
import os

"""
Learning Python Function
What is argument in a function? -- > How to pass value in a function
How to return a value from a function?
How to get value from terminal?
What is sys library ?
How to convert str to int? 
How to get a value from a list?
"""


#  Function which works as an entry point is called handler function
#  Event Driven Service - Explain

def add(event, context):
    print('Lambd Event {}:'.format(event))
    a = 2
    b = 3
    c = a + b
    print('Result: {}'.format(c))
    return c


def deduct(event, context):
    # list_of_arg = sys.argv
    # print("List if argument: {}".format(list_of_arg))
    # a = int(list_of_arg[1])  # int,  str --> Command line arg is str type, lets convert it to int
    # print('Type of var  a: {}'.format(type(a)))
    # b = int(list_of_arg[2])
    a = int(os.environ['value1'])
    b = int(os.environ['value2'])
    c = b - a
    print('Result: {}'.format(c))


def multiplication(a, b):
    result = a*b
    print("I am looks like among 1% in your life!!!!!")
    return result


# if __name__ == "__main__":
#     return_value = add()
#     print('Return Value {}'.format(return_value))
#     deduct()
#     returned_value = multiplication(a=200, b=4)
#     print(returned_value)










# import json

# def lambda_handler(event, context):
#     # TODO implement
#     return {
#         'statusCode': 200,
#         'body': json.dumps('Hello from Lambda!')
#     }
