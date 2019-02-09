# -*- coding:utf-8 -*-

sensitive_words_list = ['asshole', 'fuck', 'shit']

def detect_sensitive_words(string):
    ''' detect sensitive words'''
    #import pdb;pdb.set_trace() 
    words_detected = list(filter(lambda word: word in string.lower(), sensitive_words_list))
    if words_detected:
        name_error_string = 'Sensitive word {0} detected in the string "{1}"'\
        .format(','.join(map(lambda s:'"%s"' %s, words_detected)), string)
        raise NameError(name_error_string)

class CleanerMeta(type):
    ''' the metaclass '''
    def __new__(cls, class_name, bases, attrs):
        #import pdb; pdb.set_trace()
        detect_sensitive_words(class_name)
        #import pdb; pdb.set_trace()
        map(detect_sensitive_words, attrs.keys())
        print('Well done! You are a polite coder')       
        return type.__new__(cls, class_name, bases, attrs)

class APIBase(metaclass=CleanerMeta):
    ''' Base class for derive '''
    #__metaclass__ = CleanerMeta
    print('This is the APIBase')

class TestFuck(APIBase):
    shit = 1

if __name__ == '__main__':
    fuck = TestFuck()
    print(fuck.shit)