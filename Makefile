RSYNC=rsync -rupE
DESTDIR=$(SR_CODE_BASE)/snaproute/src/out/bin
RMDIRFORCE=rm -rf



COMPS=cmdln-2.0.0\
	functools32-3.2.3-2\
	jsonref-0.1\
	jsonschema-2.5.1\
	pip-9.0.1\
	requests-2.11.1\
	urllib3-1.16\
	vcversioner-2.16.0.0\
	setuptools-28.2.0\
	inotify-0.2.8\
	websocket_client-0.40.0\
	pyasn1-0.2.3\
	pysnmp-mibs-0.1.6\
	pysnmp-4.3.5\
	netaddr-0.7.19\
	pexpect-4.2.1\
	Jinja2-2.9.6\
	MarkupSafe-1.0\
	asn1crypto-0.22.0\
	cffi-1.10.0\
	cryptography-2.0.3\
	enum34-1.1.6\
	idna-2.6\
	ipaddress-1.0.18\
	natsort-5.1.0\
	pycparser-2.18\
	pyOpenSSL-17.2.0\
	python-dateutil-2.6.1\
	six-1.10.0

all: install
exe:
clean:
	$(RMDIRFORCE) $(DESTDIR)/cmdln-2.0.0
	$(RMDIRFORCE) $(DESTDIR)/functools32-3.2.3-2
	$(RMDIRFORCE) $(DESTDIR)/jsonref-0.1
	$(RMDIRFORCE) $(DESTDIR)/jsonschema-2.5.1
	$(RMDIRFORCE) $(DESTDIR)/pip-9.0.1
	$(RMDIRFORCE) $(DESTDIR)/requests-2.11.1
	$(RMDIRFORCE) $(DESTDIR)/urllib3-1.16
	$(RMDIRFORCE) $(DESTDIR)/vcversioner-2.16.0.0
	$(RMDIRFORCE) $(DESTDIR)/setuptools-28.2.0
	$(RMDIRFORCE) $(DESTDIR)/inotify-0.2.8
	$(RMDIRFORCE) $(DESTDIR)/websocket_client-0.40.0
	$(RMDIRFORCE) $(DESTDIR)/pyasn1-0.2.3
	$(RMDIRFORCE) $(DESTDIR)/pysnmp-mibs-0.1.6
	$(RMDIRFORCE) $(DESTDIR)/pysnmp-4.3.5
	$(RMDIRFORCE) $(DESTDIR)/netaddr-0.7.19
	$(RMDIRFORCE) $(DESTDIR)/pexpect-4.2.1
	$(RMDIRFORCE) $(DESTDIR)/Jinja2-2.9.6
	$(RMDIRFORCE) $(DESTDIR)/MarkupSafe-1.0
	$(RMDIRFORCE) $(DESTDIR)/asn1crypto-0.22.0
	$(RMDIRFORCE) $(DESTDIR)/cffi-1.10.0
	$(RMDIRFORCE) $(DESTDIR)/cryptography-2.0.3
	$(RMDIRFORCE) $(DESTDIR)/enum34-1.1.6
	$(RMDIRFORCE) $(DESTDIR)/idna-2.6
	$(RMDIRFORCE) $(DESTDIR)/ipaddress-1.0.18
	$(RMDIRFORCE) $(DESTDIR)/natsort-5.1.0
	$(RMDIRFORCE) $(DESTDIR)/pycparser-2.18
	$(RMDIRFORCE) $(DESTDIR)/pyOpenSSL-17.2.0
	$(RMDIRFORCE) $(DESTDIR)/python-dateutil-2.6.1
	$(RMDIRFORCE) $(DESTDIR)/six-1.10.0

install: $(COMPS)
	$(RSYNC) cmdln-2.0.0 $(DESTDIR) 
	$(RSYNC) functools32-3.2.3-2 $(DESTDIR) 
	$(RSYNC) jsonref-0.1 $(DESTDIR) 
	$(RSYNC) jsonschema-2.5.1 $(DESTDIR) 
	$(RSYNC) pip-9.0.1 $(DESTDIR)
	$(RSYNC) requests-2.11.1 $(DESTDIR) 
	$(RSYNC) urllib3-1.16 $(DESTDIR) 
	$(RSYNC) vcversioner-2.16.0.0 $(DESTDIR)
	$(RSYNC) setuptools-28.2.0 $(DESTDIR)
	$(RSYNC) inotify-0.2.8 $(DESTDIR)
	$(RSYNC) websocket_client-0.40.0 $(DESTDIR)
	$(RSYNC) pyasn1-0.2.3 $(DESTDIR)
	$(RSYNC) pysnmp-mibs-0.1.6 $(DESTDIR)
	$(RSYNC) pysnmp-4.3.5 $(DESTDIR)
	$(RSYNC) netaddr-0.7.19 $(DESTDIR)
	$(RSYNC) pexpect-4.2.1 $(DESTDIR)
	$(RSYNC) Jinja2-2.9.6 $(DESTDIR)
	$(RSYNC) MarkupSafe-1.0 $(DESTDIR)
	$(RSYNC) asn1crypto-0.22.0 $(DESTDIR)
	$(RSYNC) cffi-1.10.0 $(DESTDIR)
	$(RSYNC) cryptography-2.0.3 $(DESTDIR)
	$(RSYNC) enum34-1.1.6 $(DESTDIR)
	$(RSYNC) idna-2.6 $(DESTDIR)
	$(RSYNC) ipaddress-1.0.18 $(DESTDIR)
	$(RSYNC) natsort-5.1.0 $(DESTDIR)
	$(RSYNC) pycparser-2.18 $(DESTDIR)
	$(RSYNC) pyOpenSSL-17.2.0 $(DESTDIR)
	$(RSYNC) python-dateutil-2.6.1 $(DESTDIR)
	$(RSYNC) six-1.10.0 $(DESTDIR)

