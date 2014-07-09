#

pandoc -s --mathjax='mathjax/MathJax.js?config=TeX-AMS-MML_HTMLorMML' --slide-level=1 -V theme:night -M transitionSpeed:fast -t revealjs sapporo20140709.md | sed -e 's/center: true/center: false/' > sapporo20140709.html

