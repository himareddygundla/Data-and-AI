class display:
    def show(self,*args):
        if len(args) == 1:
            print("one:",args[0])
        elif len(args) == 2:
            print("two:",args[0],args[1])
        else:
            print("none")

d=display()
d.show(10)  
d.show("sum",20)
d.show("s")
d.show()