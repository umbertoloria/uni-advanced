import multiprocessing

def cerca (testo,stringa):
    for st in testo.split():
        if st==stringa:
            return True
    return False

def procTesto(files,stringhe,concurrency):
    jobs=multiprocessing.JoinableQueue()
    create_processes(jobs,stringhe,files,concurrency)
    add_jobs(files,stringhe,jobs)
    jobs.join()

def create_processes(jobs,stringhe,files,concurrency):
    for _ in range(concurrency):
        process=multiprocessing.Process(target=worker,args=(jobs,stringhe,files))
        process.daemon=True
        process.start()

def add_jobs(files, stringhe,jobs):
    for i,(f,s) in enumerate(zip(files,stringhe)):
        jobs.put((f,s,i))

def worker(jobs,stringhe,files):
    while True:
        f,s,i=jobs.get()
        o=open(f,"r")
        t=""
        for linea in o.readlines():
            t=t+linea
        result=cerca(t,s)
        if result==True:
            print("La stringa {} e' presente nel file {}:".format(stringhe[i], files[i]))
        else:
            print("La stringa {} non e' presente nel file {}:".format(stringhe[i], files[i]))
        jobs.task_done()

def main():
    files=["file1.txt","file2.txt","file3.txt","file4.txt"]
    stringhe=["capra","st1","st12","st11"]
    procTesto(files,stringhe,6)

if __name__=="__main__":
    main()
