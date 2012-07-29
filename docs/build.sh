#!/bin/sh
rst2pdf Pious.rst -e preprocess
rm Pious.rst.build_temp
rm *~
