MODULES =					\
	Config.py				\
	Color.py				\
	DB.py					\
	Debug.py				\
	Entry.py				\
	Node.py					\
	Trace.py				\
	Options.py

check:
	for i in $(MODULES) ; do \
		echo "Testing $$i" ; \
		python $$i ; \
	done

clean:
	rm -f *.pyc
	rm -f *~