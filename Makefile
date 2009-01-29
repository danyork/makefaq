# Makefile for makefaq
#
# $Id: Makefile,v 1.3.2.3 2004/02/29 10:53:08 dyork Exp $

PROJECT = makefaq
VERSION= 2.6

INSTALLPATH = /usr/local/bin

MANPATH = /usr/local/man

DOCPATH = /usr/share/doc

DOCDIR = $(DOCPATH)/$(PROJECT)-$(VERSION)

DOCS = BUGS ChangeLog CREDITS INSTALL LICENSE README TODO UPGRADING faq.html


help:
	@echo 
	@echo "This makefile has the following targets: "
	@echo 
	@echo "   install - copies the program, man page and docs to locations:"
	@echo "         program  -> ${INSTALLPATH}"
	@echo "         man page -> ${MANPATH}"
	@echo "         docs     -> ${DOCDIR}"
	@echo "   man - copies just the manpage to $(MANPATH)"
	@echo "   dist - builds a tarball and zip file"
	@echo 
	@echo "Note that you may need root privileges to access these directories"
	@echo "Modify the paths in Makefile if necessary."
	@echo 

install: man
	@echo -n "Copying makefaq.py to $(INSTALLPATH)..."
	@cp -p makefaq.py $(INSTALLPATH)
	@echo "done."
	@echo -n "Copying documentation to ${DOCDIR}..."
	@rm -rf $(DOCDIR)
	@mkdir $(DOCDIR)
	@cp -p $(DOCS) $(DOCDIR)
	@echo "done."

man: makefaq.1
	@echo -n "Copying man page to $(MANPATH)/man1..."
	@cp -p $(PROJECT).1 $(MANPATH)/man1
	@echo "done."
	
dist: 
	@echo "Make sure you are running this from a directory EXPORTED out of CVS."
	@echo "Otherwise the tarball and zip file will include the CVS subdir."
	@echo
	./makefaq.py 
	./makefaq.py -c text
	rm -f /tmp/$(PROJECT)-$(VERSION).tgz
	rm -f /tmp/$(PROJECT)-$(VERSION).zip
	rm -rf /tmp/$(PROJECT)-$(VERSION)
	mkdir /tmp/$(PROJECT)-$(VERSION)
	cp * /tmp/$(PROJECT)-$(VERSION)
	(cd /tmp; tar czf /tmp/$(PROJECT)-$(VERSION).tgz ${PROJECT}-${VERSION})
	(cd /tmp; zip -r /tmp/$(PROJECT)-$(VERSION).zip ${PROJECT}-${VERSION})
	ls -l /tmp/$(PROJECT)-$(VERSION).*

