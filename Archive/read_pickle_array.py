import pickle
with open ('gen_001/gen_001_0.pickle', 'rb') as fp:
    itemlist = pickle.load(fp)
    print itemlist