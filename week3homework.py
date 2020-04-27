import random

subject_list = ['I','They','We']
verb_list = ['like','have','use','bring']
object_list = ['an apple','an orange','a cup of milk']

def one_sentence():
    print(str(random.choice(subject_list)) + ' ' + str(random.choice(verb_list)) + ' ' + str(random.choice(object_list)))

def singular():
    subject_list_2 =['He', 'She']
    verb_list_2 = ['likes', 'has','uses','brings']
    print(str(random.choice(subject_list_2)) + ' ' + str(random.choice(verb_list_2)) + ' ' + str(random.choice(object_list)) + '.')

one_sentence()
print('and')
singular()
