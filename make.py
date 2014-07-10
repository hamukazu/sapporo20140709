#!/usr/bin/env python
# -*- coding:utf-8 -*-

infile="sapporo20140709.md"
outfile="sapporo20140709.html"
templatefile="remark.template"

from jinja2 import Template
ifp=open(infile,"r")
tfp=open(templatefile,"r")
templ=Template(unicode(tfp.read(),"utf-8"))
mdtext=unicode(ifp.read(),"utf-8")
ifp.close()
tfp.close()
doc=templ.render(mdtext=mdtext)
ofp=open(outfile,"w")
ofp.write(doc.encode("utf-8"))
ofp.close()

