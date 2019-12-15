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
