"""
test main for profiler.py
by: christian fuller
"""

from profiler import Profiler
from algorithms import *

p = Profiler()
p.test(selectionSort, size = 10000, comp = True, exch = True, trace = False, case = "worst")
p.test(bubbleSort, size = 10000, comp = True, exch = True, trace = False, case = "worst")
p.test(insertionSort, size = 10000, comp = True, exch = True, trace = False, case = "worst")
p.test(quickSort, size = 10000, comp = True, exch = True, trace = False, case = "worst")
p.test(mergeSort, size = 10000, comp = True, exch = True, trace = False, case = "worst")