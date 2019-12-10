import functools

def cerca (testo,stringa):
    for st in testo.split():
        if st==stringa:
            return True
    return False

def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args,**kwargs):
        generator=function(*args,**kwargs)
        next(generator)
        return generator
    return wrapper

@coroutine
def reporter(stringhe,files):
    while True:
        found,i= (yield)
        if found==True:
            print("La stringa {} e' presente nel file {}:".format(stringhe[i], files[i]))
        else:
            print("La stringa {} non e' presente nel file {}:".format(stringhe[i], files[i]))

@coroutine
def cercatore(ricevitore,stringa):
    while True:
        testo,i=(yield)
        found=cerca(testo,stringa)
        ricevitore.send((found,i))

def procTesto(files,stringhe,concurrency):
    ricevitore=reporter(stringhe,files)
    cercatori=dict()
    for stringa in stringhe:
        cercatori[stringa]=cercatore(ricevitore,stringa)
    try:
        for i,(file,stringa) in enumerate(zip(files,stringhe)):
            o=open(file)
            testo=o.read()
            cercatori[stringa].send((testo,i))
    finally:
        for c in cercatori.values():
            c.close()
        ricevitore.close()

def main():
    files=["file1.txt","file2.txt","file3.txt","file4.txt"]
    stringhe=["capra","st1","st12","st11"]
    procTesto(files,stringhe,6)

if __name__=="__main__":
    main()
