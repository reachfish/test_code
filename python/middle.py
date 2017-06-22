# -- coding: utf-8 --
import sys

def helpFun():
    def info(object, spacing=10, collapse=1): 
        """Print methods and doc strings.
        Takes module, class, list, dictionary, or string."""
        methodList = [method for method in dir(object) if callable(getattr(object, method))]
        processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
        print "\n".join(["%s %s" %   \
            (method.ljust(spacing),  \
            processFunc(str(getattr(object, method).__doc__))) \
            for method in methodList])

    lst = []
    info(lst)

"""
*args, **kwargs
    list args, dict args
"""
def argFun():
    #*args, **kwargs
    def foo(arg1, arg2, arg3):
        print 'arg1', arg1
        print 'arg2', arg2
        print 'arg3', arg3

    args = ("a", "ab", "abc")
    kwargs = { "arg1": "x", "arg2" : "xy", "arg3" : "xyz" }

    foo(*args)
    foo(**kwargs)

    #default argument is evaluate once when the function is define, not each time when is called
    def add1(val, target=[]):
        target.append(val)
        print target
        return target

    def add2(val, target=None):
        if target is None:
            target = []

        target.append(val)
        print target
        return target

    add1(1)
    add1(2)
    add1(3)  #[1,2,3]

    add2(1)
    add2(2)
    add2(3)  #[3]

"""
iterable
   method: 实现__getitem__或 __iter__函数
iterator 
   method: 实现__next__函数
generator 
   属于iterator，通过yield来产生，可以实现为函数
"""
def iterFun():
    #generator
    def generator_fun():
        for i in range(3):
            yield i, i * i
    

    #0 0   1 1   2 4
    for k, v in generator_fun():
        print k, v

    #fibon generator
    def fibon(n):
        a = b = 1
        for i in range(n):
            yield a  
            a, b = b, a+b

    #[1,1,2,3,5]
    for v in fibon(5):
        print v

"""
Map
    map(func, input_list) 相当于返回 func(v)    

Filter
    filter(func, input_list) 相当于返回 if func(v): v

Reduce
    reduce(func, input_list) 相当于返回所有的func的汇集结果
"""
def mapReduceFunc():
    #map 1
    ls = list(map(lambda(x): x**2, [1,2,3,4]))
    print ls  #[1,4,9,16]

    #map 2
    def mul(x): return x * x
    def add(x): return x + x
    funcs = [mul, add]
    ls = list(map(lambda x : x(5), funcs))
    print ls #[10, 25]

    #filter 
    ls = list(filter(lambda x:x<3, [1,2,3,4]))
    print ls #[1,2]

    #reduce 
    result = reduce(lambda x, y: x + y, [1,2,3,4])
    print result  #10

"""
Decorator
"""
def decoratorFun():
    #decorator func with argument
    def decoFoo(family):
        def decorator_fun(f):
            def wrapfunc(name):
                return f("%s %s"%(family, name))

            return wrapfunc
        return decorator_fun

    @decoFoo("Lee")
    def func(name):
        return "My Name is {0}".format((name))

    print func("Koo")

    #decorator class
    class Logit(object):
        def __init__(self, logfile):
            self.logfile = logfile

        def __call__(self, func):
            def wrap(*args, **kwargs):
                logstring = "calling func %s" % func.__name__
                print(self.logfile, logstring)
                func(*args, **kwargs)

            return wrap

    @Logit("log/call.log")
    def foo():
        pass

    foo()

"""
slots 
    tell python not to use dict, and only allocate spaces for fixed set of attributes
"""
def slotFun():
    class C(object):
        __slots__ = {"name", "age"}

    c = C()
    c.name = "Joo"
    c.sex = "M" #err

        
if __name__ == "__main__":
    for cmd in sys.argv[1:]:
        function = None
        try:
            function = eval(cmd)
        except NameError:
            print "action '%s' is invalid" %cmd
        assert function, "action %s is invalid" %(cmd)

        print "=========================="
        print "Fun: %s" % cmd
        print "=========================="
        function()

