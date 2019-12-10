stati = ["ordinato", "spedito", "ricevuto"]
class Pacco:
    ORDINATO, SPEDITO, RICEVUTO = [0, 1, 2]
    def __init__(self):
        self.statoPacco=Pacco.ORDINATO

    @property
    def statoPacco(self):
        if self.next != self._next:
            return Pacco.RICEVUTO
        if self.pred != self._pred:
            return Pacco.ORDINATO
        if self.pred == self._pred and self.next == self._next:
            return Pacco.SPEDITO

    @statoPacco.setter
    def statoPacco(self, newState):
        if newState == Pacco.ORDINATO:
            self.next = self._next
            self.pred = lambda *args: print("Lo stato del pacco non può tornare indietro perchè è nello stato ",stati[self.statoPacco])
        if newState == Pacco.SPEDITO:
            self.next = self._next
            self.pred = self._pred
        if newState == Pacco.RICEVUTO:
            self.pred = self._pred
            self.next = lambda *args: print("Lo stato del pacco non può andare avanti perchè è nello stato ",stati[self.statoPacco])


    def _pred(self):
        self.statoPacco=self.statoPacco-1
    def _next(self):
        self.statoPacco=self.statoPacco+1

    def stampaStato(self):
        print("Il pacco è " + stati[self.statoPacco])

def main():
	print("\nCreo il pacco")
	pacco=Pacco()
	pacco.stampaStato()
	print("\nInoltro il pacco all'ufficio postale")
	pacco.next()
	pacco.stampaStato()
	print("\nConsegno il pacco al destinatario")
	pacco.next()
	pacco.stampaStato()
	print("\nProvo a passare ad uno stato successivo")
	pacco.next()
	pacco.stampaStato()

if __name__== "__main__":
	main()


"""Il  programma deve stampare:
Creo il pacco
Il pacco e` stato ordinato ma non ancora spedito

Inoltro il pacco all'ufficio postale
Il pacco e` stato spedito ma non ancora ricevuto

Consegno il pacco al destinatario
Il pacco e` stato ricevuto 

Provo a passare ad uno stato successivo
Il pacco e` gia` stato ricevuto
Il pacco e` stato ricevuto 
"""