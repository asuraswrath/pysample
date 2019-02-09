# -*- coding: UTF-8 -*-

def fib(n:int=100):
    """ print  a  fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end='  ')
        a, b = b, a+b
    print()

def fib1(n:int=100) -> int:
    ''' print a fibonacci series up to n, wraps in list.'''
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def parrot(voltage, state='a stiff', action='voom' ):
    ''' in the same function, dictionaries can deliver
        keyword arguments with the ** operator
    '''
    print("--this parrot wouldn't", action, end='  ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, '!')
d = {'voltage': 'four million', 'state': 'bleedin', 'action': 'VOOM'}

if __name__ == '__main__':
    print('this is fib:')
    fib(1000)
    print('this is fib1:')
    print(fib1(1000))
    parrot(**d)