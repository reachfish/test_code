def test1():
    def buildConnection(param):
        """build a connection string
           returns string"""
        return ";".join([ "%s:%s" %(k,v) for k, v in param.items()])

    params = { "server" : "local", "os" : "cygwin", "user" : "yujun" }
    print buildConnection(params)


if __name__ == "__main__":
    test1()
