import pickle, picklerick
f = open('student.dat', 'wb')
s = picklerick.Student('andro is the name')
pickle.dump(s, f)
f.close

# unpickle
pl = open('student.dat', 'rb')
try:
    lp = pickle.load(pl)
except EOFError:
    print('ran out of input')
lp.display()
pl.close()