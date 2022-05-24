import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.basicConfig(filename='log/log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO
)

def get_student_list():
    student_list = ['John', 'Jack', 'Kack', 'Mac', 234]
    logger.info('Student List: {}'.format(student_list))
    print(student_list)
    logger.info('List Length {}'.format(len(student_list)))
    print()
    
#get_student_list()

if __name__ == "__main__":
    get_student_list()