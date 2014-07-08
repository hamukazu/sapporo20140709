#

pandoc -s --mathjax --slide-level=1 -V theme:default -M center:false -M transitionSpeed:fast -t revealjs sapporo20140709.md > sapporo20140709.html
