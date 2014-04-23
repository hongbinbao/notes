#!/usr/bin/python
# -*- coding:utf-8 -*-

def decorator(deco_arg):

    def function_wrapper(function):
        def args_wrapper(*argv, **kwargs):
            print "decorator_arg: %s" % deco_arg
            print "before function execute"
            function(*argv, **kwargs)
            print "after function execute"    
        return args_wrapper
    return function_wrapper
    
@decorator("123")
def my_function1(v):
    print "my_function1() called: %s" % v
    
def my_function2(v):
    print "my_function2() called: %s" % v
    
    
print "my_function1 output:"
my_function1("456")

print "\nmy_function2 output:"
decorator("123")(my_function2)("456")
    
###my_function1 output:
###decorator_arg: 123
###before function execute
###my_function1() called: 456
###after function execute

###my_function2 output:
###decorator_arg: 123
###before function execute
###my_function2() called: 456
###after function execute
