def student_info():
    dips_details = {
        'Name' : 'Dip',
        'Course': 'DevOps',
        'Batch' : 'B2201',
        'Result': {
            'iam': 50,
            's3' : 40,
            'cf' : 55,
            'py' : 42
        },
    }
    print(dips_details.get('Namee'))
    print(dips_details['Name'])
    iam_result = dips_details.get('Result')
    print(type(iam_result))

    print(iam_result['iam'])

if __name__ == "__main__":
    student_info()



