#

pandoc -s --mathjax --slide-level=1 -V theme:night -t revealjs sapporo20140709.md | sed -e 's/center: true/center: false/' > sapporo20140709.html

