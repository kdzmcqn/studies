def deco(num):
    def foo1(fun):

        print("lolol")  # lalaktawan after ng first exec
        print(fun(4))

        def foo2(num2):

            def foo3(lol):  # pinaka bumabalot. always exec every use
                print(fun(lol))

            foo3(num)

            return fun(num + num2)

        return foo2

    return foo1


@deco(1)
def square(numba):
    return numba**2

n = square(2)
print(n)
b = square(7)
print(b)

dd = square(9)
print(dd)
ee = square(10)
print(ee)







def decodeco(numnum): # numnum = args ng deco
    print("----decodeco----") #  wag na maglagay under decodeco
    print(numnum)  # pati na rin sa foofoo1
    # unless lagyan mo ng foofoo1() bago magreturn sa decodeco
    def foofoo1(beepbepp): # beepbepp = mismong object na dinedeco
        print("----foofoo1----")
        print(beepbepp)
        def booboo1(bumbum):  #bumbum = args ng object na dinedeco/// callables dapat
            print("----booboo1----")  # dito ka mag decorate
            print("***wooo decorations***")
            print(bumbum)

            # def lalaland(jazz):  # jazz = wala, lugar ng args ng lalaland lang
            #     print("----lalaland----") # so not necessary na to at all
            #     print(jazz)

            print(beepbepp(bumbum - numnum))
            print("***more decos***")

            #pwede magreturn none kung mag pprint ka rin
            #return beepbepp(bumbum - numnum)
        # di pwede mag booboo1() dito
        # print(booboo1) pwede pero panget
        return booboo1
    # try mo lagyan foofoo1()
    # foofoo1(3)
    return foofoo1


@decodeco(5)
def cube(raise3):
    return raise3**3

qq = cube(7)
print(qq, " none kasi eto mismo yung print na outside sa mga functions")

zz = cube(10)
print(zz, " none kasi eto mismo yung print na outside sa mga functions")