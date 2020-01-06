# Design pattern strutturali

# Decorator

Un decoratore prende in input una funzione o una classe e la restituisce ma con ulteriori funzionalità.
Un decoratore di classe è talvolta considerato un'alternativa all'ereditarietà.

Una vista generica del decoratore di funzione è il seguente:

    def **decoratore**(func):
        # 'wrapper' eredita __name__ e __docs__ di 'func' (non è essenziale)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            **business logic pre-chiamata (spesso elabora attributi)**
            res = func(*args, **kwargs)
            **business logic post-chiamata (spesso elabora risultato)**
            return res # oppure qualcos altro
        return wrapper

    @**decoratore**
    def **funzione base**():
        **business logic**

Esempio di decoratore che converte in float i parametri e il risultato della chiamata alla funzione che decora.

    def tutto_float(func):
        def wrapper(*args, **kwargs):
            new_args = [float(arg) for arg in args]
            return float(func(*new_args, **kwargs))
        return wrapper

    @tutto_float
    def media(a, b, *altri):
        numeri = (a, b) + altri
        return sum(numeri) / len(numeri)

Ecco un decoratore di classe 'ingrassante'.

    def ingrassa(classe):
        for i in range(1000):
            setattr(classe, "attr_" + str(i), "nutella")
        return classe

    @ingrassa
    class X:
        pass

    print(X.__dict__)
    >>> {... 'attr_0': 'nutella', 'attr_1': 'nutella', 'attr_2': 'nutella', ...}

Il difficile compito di invertire questo decoratore viene affrontato duramente, anche dai programmatori più esperti.

## Adapter

Un Adapter crea un livello di astrazione capace di far comunicare due interfacce che sono incompatibili.

Esempio: un client che può solo invocare metodi "execute", e altre classi che dispongono solo di metodi
Un client che esegue solo il metodo "execute" di qualsiasi oggetto e

Situazione reale:
* c'è un client che esegue solamente il metodo "execute" di quasiasi oggetto;
* c'è una classe che dispone solo del metodo play;
* non è possibile modificare il codice sorgente delle due classi

Tramite un Adapter, è possibile wrappare la classe che contiene "play" e farla chiamare durante la chiamata

L'Adapter sarà un oggetto con un metodo "execute" che internamente chiama il metodo "play".
Questo si può implementare:
* associando uno-a-uno il metodo "execute" a "play" usando un dizionario;
* incapsulando la classe con il metodo "play" in una classe che chiama quest'ultimo tramite il metodo "execute".

Metodo con il dizionario associativo:

    class Adapter:
        def __init__(self, obj, adapted_methods):
            self.__dict__.update(adapted_methods)
    synth = Synthesizer("Moog")
    adapter = Adapter(synth, {"execute": synth.play})
    adapter.execute() # uguale a synth.play()

Metodo con l'incapsulazione:

    # non si può modificare
    class ClasseInnocente:
        def __init__(self, canzone):
            self.canzone = canzone
        def suona(self):
            print("suono '" + self.canzone + "' innocentemente")

    # neanche questa
    def funzione_ignara(oggetti):
        for oggetto in oggetti:
            oggetto.lancia()

    innocente1 = ClasseInnocente("Stairway to Heaven")
    innocente2 = ClasseInnocente("Panic Attack")
    innocente3 = ClasseInnocente("A Little Piece of Heaven")

    class Adapter():
        def __init__(self, obj):
            self.obj = obj
        def lancia(self):
            self.obj.suona()

    adapter1 = Adapter(innocente1)
    adapter2 = Adapter(innocente2)
    adapter3 = Adapter(innocente3)

    candidati = [adapter1, adapter2, adapter3]

    funzione_ignara(candidati)

## Proxy

Il Proxy incapsula una classe che compie una grande mole di lavoro, decidendo arbitrariamente quando farlo svolgere.
Si dice che il Proxy sia uno caso particolare di State in cui un solo stato è contemplato.

Ecco un semplice Proxy stupido:

    class Implementation:
        def f(self):
            print("f")
        def g(self):
            print("g")
        def h(self):
            print("h")

    class Proxy:
        def __init__(self):
            self.__impl = Implementation()
        def f(self):
            self.__impl.f()
        def g(self):
            self.__impl.g()
        def h(self):
            self.__impl.h()

Ecco un esempio super-esplicativo di Proxy (alcune operazioni le esegue subito mentre altre le svolge in ritardo):

    class ComeDovreiEssere:
        def pulisci_la_stanza(self):
            print("ok pulisco mamma...")
        def fai_il_letto(self):
            print("certo che faccio il letto mamma...")

    class ComeSonoSolitamente:
        def __init__(self):
            self.come_dovrei_essere = ComeDovreiEssere()
            self.li_faccio_dopo = []
        def pulisci_la_stanza(self):
            self.come_dovrei_essere.pulisci_la_stanza()
        def fai_il_letto(self):
            self.li_faccio_dopo.append(ComeDovreiEssere.fai_il_letto)
        def dai_forza(self):
            for lo_faccio_dopo in self.li_faccio_dopo:
                lo_faccio_dopo(self.come_dovrei_essere)

    umbi = ComeSonoSolitamente()
    umbi.fai_il_letto()
    umbi.pulisci_la_stanza()
    umbi.pulisci_la_stanza()
    umbi.fai_il_letto()
    umbi.fai_il_letto()
    umbi.dai_forza()

    >>> ok pulisco mamma...
    >>> ok pulisco mamma...
    >>> certo che faccio il letto mamma...
    >>> certo che faccio il letto mamma...
    >>> certo che faccio il letto mamma...

A rappresentare il comportamento del proxy può essere, per esempio, il senso di responsabilità verso il proprio spazio
personale incapsulato nella mia svogliatezza durante caldi pomeriggi estivi.

# Design pattern creazionali

## Singleton

Il Singleton è una soluzione piuttosto utilizzata in Informatica. Viene usato quando:

* è necessario l'esistenza di una sola istanza di una classe nello stesso momento;
* si vuole controllare l'accesso concorrente a una risorsa condivisa.

Esempi di utilizzo:

* realizzare thread pool e connection pool;
* memorizzare informazioni su un file di configurazione esterno.


    class Singleton:
        class __impl:
            def __init__(self):
                pass
        __instance = None
        def __init__(self):
            if Singleton.__instance is None:
                Singleton.__instance = Singleton.__impl()
        def __getattr__(self, attr):
            return getattr(self.__instance, attr)
        def __setattr__(self, attr, value):
            return setattr(self.__instance, attr, value)

# Design pattern comportamentali

## Chain of Responsibility

Implementazione tramite **classi**:

    class NullHandler:
        def __init__(self, successor=None):
            self.__successor = successor
        def handle(self, event):
            if self.__successor is not None:
                self.__successor.handle(event)

    class **name of handler**(NullHandler):
        def handle(self, event):
            if **event is suitable**:
                **business logic for that event**
            else:
                super().handle(event)

    chain = MousePressedHandler(
                KeyPressedHandler(
                    KeyReleasedHander(
                        GlobalHander())))

    chain.handle(**whatever event you want**)

Implementazione tramite **coroutines**:

    def coroutine(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            generator = function(*args, **kwargs)
            next(generator)
            return generator
        return wrapper

    @coroutine
    def **name of handler**(successor=None):
        while True:
            event = yield
            if **event is suitable**:
                **business logic for that event**
            elif successor is not None:
                successor.send(event)

    pipeline = mouse_pressed_handler(
                    key_pressed_handler(
                        key_released_handler(
                            global_handler()))

## State

**State-sensitive**: usa un'attributo privato definito, e tutti i metodi si basano su questo per poter determinare il
proprio comportamento.

    class **sensitive**:
        STATO1 = "STATO1"
        STATO2 = "STATO2"
        STATO3 = "STATO3"
        def __init__(self):
            self.stato = **sensitive**.STATO1
        def method1(self):
            if self.stato == **sensitive**.STATO1:
                **business logic method 1 stato 1**
            elif self.stato == **sensitive**.STATO2:
                **business logic method 1 stato 2**
            elif self.stato == **sensitive**.STATO3:
                **business logic method 1 stato 3**
        def method2(self):
            if self.stato == **sensitive**.STATO1:
                **business logic method 2 stato 1**
            elif self.stato == **sensitive**.STATO2:
                **business logic method 2 stato 2**
            elif self.stato == **sensitive**.STATO3:
                **business logic method 2 stato 3**

**State-specific**: lo stato è una proprietà, e viene determinato dal comportamento attuale dei metodi.

    class **specific**:
        STATO1 = "STATO1"
        STATO2 = "STATO2"
        STATO3 = "STATO3"
        def __init__(self):
            self.stato = **specific**.STATO1

        @property
        def stato(self):
            if self.method1 == self.__method1_bl_stato1:
                return **specific**.STATO1
            elif self.method1 == self.__method1_bl_stato2:
                return **specific**.STATO2
            elif self.method1 == self.__method1_bl_stato3:
                return **specific**.STATO3
        @stato.setter
        def stato(self, val):
            if val == **specific**.STATO1:
                self.method1 = self.__method1_bl_stato1
                self.method2 = self.__method2_bl_stato1
            elif val == **specific**.STATO2:
                self.method1 = self.__method1_bl_stato2
                self.method2 = self.__method2_bl_stato2
            elif val == **specific**.STATO3:
                self.method1 = self.__method1_bl_stato3
                self.method2 = self.__method2_bl_stato3

        def __method1_bl_stato1(self):
            **business logic method 1 stato 1**
        def __method1_bl_stato2(self):
            **business logic method 1 stato 2**
        def __method1_bl_stato3(self):
            **business logic method 1 stato 3**

        def __method2_bl_stato1(self):
            **business logic method 2 stato 1**
        def __method2_bl_stato2(self):
            **business logic method 2 stato 2**
        def __method2_bl_stato3(self):
            **business logic method 2 stato 3**

## Observer

    class Observer:
        def update(self, observed):
            **abserver business logic**

    class Observed:
        def __init__(self):
            self.__observers = set()
        def observers_add(self, observer, *observers):
            for observer in itertools.chain((observer,), observers):
                self.__observers.add(observer)
                observer.update(self)
        def observer_discard(self, observer):
            self.__observers.discard(observer)
        def observer_notify(self):
            for observer in self.__observers:
                observer.update(self)

    class **modello osservato**(Observed):
        def __init__(self):
            super().__init__()
            self.__x = None
        @property
        def x(self):
            return self.__x
        @x.setter
        def x(self, value):
            if self.__x != value:
                self.__x = value
                self.observer_notify()

    observer1 = **observer 1**()
    observer2 = **observer 2**()

    model = **modello osservato**()
    model.observers_add(observer1, observer2)

    model.x = 5    # notifying observers
    model.x = 10   # notifying observers
    model.x = 15   # notifying observers

# Altro

## Context Manager

Implementazione tramite **classi**:

    class File:
        def __init__(self, file_name, method):
            self.file_obj = open(file_name, method)
        def __enter__(self):
            return self.file_obj
        def __exit__(self, exc_type, exc_val, exc_tb):
            self.file_obj.close()
    with File("file.txt", "w") as file:
        file.write("Hola amigo!")

Aggiungere comportamento ad esistenti tramite **decoratore contextmanager**.

    from contextlib import contextmanager
    @contextmanager
    def open_file(filename, method):
        f = open(filename, method)
        try:
            yield f
        finally:
            f.close()
    with open_file("file.txt", "w") as file:
        file.write("Hola amigo!")


## Slots

    class **class using slots**:
        __slots__ = ("x", "y", "z")
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z

## Concurrency

Realizzazione tramite il modulo **multiprocessing**.

    import multiprocessing
    def get_results(todos, params, concurrency):
        jobs = multiprocessing.JoinableQueue()
        results = multiprocessing.Queue()
        create_processes(jobs, results, concurrency)
        add_jobs(todos, params, jobs)
        jobs.join()
        return summarize(results)
    def create_processes(jobs, results, concurrency):
        for _ in range(concurrency):
            process = multiprocessing.Process(target=worker, args=(jobs, results))
            process.daemon = True
            process.start()
    def add_jobs(todos, params, jobs):
        for todo in todos:
            jobs.put((todo, params))
    def worker(jobs_jq, results_q):
        while True:
            todo, params = jobs_jq.get()
            **business logic**
            results_q.put(**result of the logic**)
            jobs_jq.task_done()
    def summarize(results_q):
        res = []
        while not results_q.empty():
            result = results_q.get()
            res.append(result)
        return res

Realizzazione tramite il modulo **futures**.

    import concurrent.futures
    def get_results(todos, params, concurrency):
        futures_set = set()
        with concurrent.futures.ProcessPoolExecutor(max_workers=concurrency) as executor:
            for todo in get_jobs(todos):
                future = executor.submit(worker, todo, params)
                futures_set.add(future)
            return wait_for(futures_set)
    def get_jobs(todos):
        for todo in todos:
            yield todo
    def wait_for(futures_set):
        res = []
        for future in concurrent.futures.as_completed(futures_set):
            result = future.result()
            res.append(result)
        return res
    def worker(todo, params):
        **business logic**
        return **result of the logic**

## Ereditarietà multipla

    class A():
        pass
    print(A.__mro__)
    >>> (<class '__main__.A'>, <class 'object'>)

    class B(A):
        pass
    print(B.__mro__)
    >>> (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

    class C():
        pass
    print(C.__mro__)
    >>> (<class '__main__.C'>, <class 'object'>)

    class D(B, C):
        pass
    print(D.__mro__)
    >>> (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>)

L'attributo **\_\_mro__** non è direttamente modificabile, ma è ricomputabile grazie l'attributo **\_\_bases__**.
Questo attributo permette di ridefinire le classi "padri" di una classe, modificando volendo anche l'ordine di ricerca
delle funzioni ereditate.
