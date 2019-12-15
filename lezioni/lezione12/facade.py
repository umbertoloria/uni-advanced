class Archive:
	def __init__(self, filename):
		self._names = None  # callable che restituisce la listad ei nomi dei file dentro l'archivio
		self._unpack = None  # callable che comprime ed estrare i file dall'archivio
		self._file = None  # variabie che mantiene il file object per poter mantenere aperto l'archivio
		self.filename = filename  # nome dell'archivio

	@property
	def filename(self):
		return self.__filename

	@filename.setter
	def filename(self, name):
		self.close()
		self.__filename = name

	def close(self):
		if self._file is not None:
			self._file.close()
		self._names = self._unpack = self._file = None

	# per far diventare un Context Manager questo archivio, basta mettere __enter__ e __exit__
	def __enter__(self):
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.close()

	def names(self):
		if self._file is None:
			self._prepare()
		return self._names()

	def unpack(self):
		if self._file is None:
			self._prepare()
		self._unpack()

	def _prepare(self):
		if self.filename.endswith((".tar.gz", ".tar.bz2", ".tar.xz", ".zip")):
			self._prepare_tarball_or_zip()
		elif self.filename.endswith(".gz"):
			self._prepare_gzip()
		else:
			raise ValueError("unreadable: {}".format(self.filename))

	def is_safe(self, filename):
		import string
		import re
		return not (filename.startswith(("/", "\\")) or (
				len(filename) > 1 and filename[1] == ":" and filename[0] in string.ascii_letters) or re.search(
			r"[.][.][/\\]", filename))

	def _prepare_tarball_or_zip(self):
		def safe_extractall():
			unsafe = []
			for name in self.names():
				if not self.is_safe(name):
					unsafe.append(name)
			if unsafe:
				raise ValueError("unsafe to unpack: {}".format(unsafe))
			self._file.extractall()

		if self.filename.endswith(".zip"):
			import zipfile
			self._file = zipfile.ZipFile(self.filename)
			self._names = self._file.namelist
			self._unpack = safe_extractall
		else:
			import os
			# filename = "prova/ciao.tar.gz" => suffix = ("prova/ciao.tar", ".gz")
			suffix = os.path.splitext(self.filename)[1]
			import tarfile
			self._file = tarfile.open(self.filename, "r:" + suffix[1:])
			self._names = self._file.getnames
			self._unpack = safe_extractall

	def _prepare_gzip(self):
		import gzip
		self._file = gzip.open(self.filename)
		filename = self.filename[:-3]
		self._names = lambda: [filename]

		def extractall():
			with open(filename, "wb") as file:
				file.write(self._file.read())

		self._unpack = extractall


# Il WITH AS fino ad ora lo abbiamo usato con delle classe che nascono come dei Context Manager: Come per esempio
# scriviamo with open(...) as var che rappresenta il file object del file che abbiamo aperto. Quella è una cosa che è
# supportata naturalmente da Python. Ora vediamo come scrivere dei Context Manager, quindi rendere degli oggetti che non
# sono naturalmente utilizzati nello statement WITH AS e renderli in effetti Context Manager.
with Archive("ciao.zip") as archive:
	print(archive.names())
	archive.unpack()
