# -- coding: utf-8 --
import sys

def foo():
    def buildConnection(param):
        """build a connection string
           returns string"""
        return ";".join([ "%s:%s" %(k,v) for k, v in param.items()])

    params = { "server" : "local", "os" : "cygwin", "user" : "yujun" }
    print buildConnection(params)

def dictFun():
    d = {"name" : "reach", "age" : 20}

    #删除单个元素
    del d["name"]
    #清空
    d.clear()

    #key只能是不可改变的值，如整数、字符串、tuple; 用list时会报错
    d[(1,2)] = 1 
    #d[[1,2]] = 1 #异常

def listFun():
    lst = [1,2,2,3,4]

    #index查找第一次出现，找不到时会抛异常
    print lst.index(1)
    #lst.index(0) --抛异常

    #remove删除的是第一次出现
    lst.remove(2)
    #lst.remove(0) #抛异常

    #pop删除最后一个元素并返回
    print lst.pop() 

def tupleFun():
    t = (1,2,3,4)

    #tuple没有list中相应的函数，只有in和分割
    #t.index(1) #抛异常
    print 1 in t, -1 in t

def boolFun():
    #0,空串"", 空list[],空tuple(),空dict{} 都为false
    for var in [0, "", [], (), {}]:
        print "%s is %s"%(var, "True" if var else "False") 



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
