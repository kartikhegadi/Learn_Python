import shelve

# shelfile=shelve.open('bigdata')
# cats=['zophie','Pooka','Simon','stuff','bigstuff']
# shelfile['pooka']=cats
# shelfile.close()


shelfile = shelve.open('bigdata')
print(type(shelfile))
print(shelfile['cats'])
shelfile.close()
