default:
	echo "run 'make install' to install applications"
install:
	cp ./deditor.py /usr/local/bin/deditor
	chmod 755 /usr/local/bin/deditor
	cp ./deditor.desktop /usr/share/applications
