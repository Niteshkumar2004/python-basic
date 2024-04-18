print("Starting Line")
a=[11,22,33]


try:

    print(a)
except ZeroDivisionErrror:
    print("expecption raised due to zero division error")
except IndexError :
    print("expection raised due to index out of range")
except NameError :
    print("expection raised due to underfined variable")
except:
    print("some exception raised")
else:
    print("no exception raised, everything worked perfectly")
finally:
    print("this is a final block ")
print("this is a block")

