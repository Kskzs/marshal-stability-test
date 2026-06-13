# -*- coding: utf-8 -*-
import sys,os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import coverage
from whitebox.marshal_wrapper import full_cycle

cov = coverage.Coverage(source=["whitebox.marshal_wrapper"])
cov.start()

full_cycle(123)
full_cycle("test")


cov.stop()
cov.save()
cov.report()
cov.html_report(directory="html_report")
