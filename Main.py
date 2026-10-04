class myclass:

    __privatevar=27

    def __privmeth(self):
        print("This is a private class")

    def hello(self):
        print("This is a private variable value",myclass.__privatevar)

foo=myclass()
foo.hello()
foo.__privmeth()

