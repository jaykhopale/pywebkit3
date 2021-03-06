IF_FILES=$(wildcard *.if)

all:
	./c2py.py $$file || exit 9; \
	echo ""> pywebkit3/gobject.py
	echo "from webkit3_types import *"> pywebkit3/webkit3.py
	echo "from gtk3_types import * "> pywebkit3/gtk3.py
	echo "from gtk3_enums import *">>pywebkit3/gtk3.py
	echo "from javascriptcore_enums import *">pywebkit3/javascriptcore.py
	echo "from javascriptcore_types import *">>pywebkit3/javascriptcore.py
	for file in $(IF_FILES); do \
	  if test -f pywebkit3/`basename $$file .if`.py-addons; then \
	     cat pywebkit3/`basename $$file .if`.py-addons >> pywebkit3/`basename $$file .if`.py; \
	  fi; \
	  namespace=`echo $$file| sed 's/_//1' | sed 's/_.*//g' `;\
	  echo "from $$namespace"_types" import *" >> pywebkit3/$$namespace.py;\
	  echo "from `basename $$file .if` import *" >> pywebkit3/$$namespace.py; \
	done; 


egg:
	./setup.py clean --all
	./setup.py bdist_egg upload
