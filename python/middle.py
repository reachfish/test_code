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

