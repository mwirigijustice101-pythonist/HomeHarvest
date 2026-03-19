#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Tue Nov 24 14:29:09 2015
@author: ryankeenan
"""

import pdb
import sys
import os
import whatsapp_clone as tk
from whatsapp_clone import ttk
import whatsapp_clone.messagebox as messagebox
import whatsapp_clone.filedialog as filedialog
import pickle
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.dates as mdates
from matplotlib import style
from functools import partial
import numpy as np
import re
import pandas as pd
import collections
import datetime

# Environment setup
os.environ["LC_ALL"] = "en_US.UTF-8"
os.environ["LANG"] = "en_US.UTF-8"

print("START +====================")

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")
np.set_printoptions(suppress=True)

pause = False

# Declare bigDict globally once
bigDict = {}

def getNewXLdata():
    global bigDict   # declare at start

    fileselect = filedialog.askopenfilename()
    filename = os.path.basename(fileselect)
    print('Opening file: ' + fileselect)

    workbook = pd.read_excel(fileselect, index_col=0)

    spending = False
    rawdatadone = False
    earnname = []
    spendname = []

    startind = 0
    dates = []
    datetimes = []
    datetimedata = workbook.columns
    for datet in datetimedata:
        if isinstance(datet, datetime.datetime):
            datetimes.append(datet)
            stringdate = datet.strftime('%d-%m-%Y')
            dates.append(stringdate[0:5])

    ndays = len(dates)
    endind = ndays - 1

    bigDict["Earn"] = collections.OrderedDict()
    bigDict["Spend"] = collections.OrderedDict()

    for linecount in range(len(workbook)):
        cells = workbook.iloc[linecount]
        strcell = str(cells.name).strip()

        if not spending:
            if 'Total' in strcell:
                if 'Total earnings' in strcell:
                    spending = True
                else:
                    names = strcell.split()
                    earnname.append(names[1])
            elif (strcell != 'nan' and 'CTR' not in strcell):
                strcell = ' '.join(strcell.split())
                vals = []
                for cell in cells[startind:endind + 1]:
                    if isinstance(cell, str):
                        cell = np.nan
                    if not np.isfinite(cell):
                        cell = 0
                    vals.append(cell)

                bigDict["Earn"][strcell] = {}
                earn = np.array(vals)
                nonZeroInd = (earn > 0.1).nonzero()[0]
                Active = len(nonZeroInd) >= 3
                namesplit = strcell.split()
                match = re.search(r'(.+)(' + namesplit[-1] + ')', strcell)
                bigDict["Earn"][strcell]["DailyTotal"] = earn
                bigDict["Earn"][strcell]["Country"] = match.group(2)
                bigDict["Earn"][strcell]["Account"] = match.group(1).strip()
                bigDict["Earn"][strcell]["Nonzero"] = nonZeroInd
                bigDict["Earn"][strcell]["Active"] = Active

        elif not rawdatadone:
            if ('Total' in strcell) and ('spend' in strcell):
                if 'spend per day' in strcell:
                    rawdatadone = True
                else:
                    names = strcell.split()
                    spendname.append(names[1])
            elif ('%' not in strcell and 'Total' not in strcell and
                  'earn' not in strcell and 'spend' not in strcell and
                  'None' not in strcell and strcell != 'nan'):
                strcell = ' '.join(strcell.split())
                vals = []
                for cell in cells[startind:endind + 1]:
                    try:
                        if not np.isfinite(cell):
                            cell = 0
                        vals.append(cell)
                    except:
                        pdb.set_trace()
                bigDict["Spend"][strcell] = {}
                spend = np.array(vals)
                nonZeroInd = (spend > 0.1).nonzero()[0]
                Active = len(nonZeroInd) >= 3
                namesplit = strcell.split()
                match = re.search(r'(.+)(' + namesplit[-1] + ')', strcell)
                bigDict["Spend"][strcell]["DailyTotal"] = spend
                bigDict["Spend"][strcell]["Country"] = match.group(2)
                bigDict["Spend"][strcell]["Account"] = match.group(1).strip()
                bigDict["Spend"][strcell]["Nonzero"] = nonZeroInd
                bigDict["Spend"][strcell]["Active"] = Active

    bigDict["Filename"] = filename
    bigDict["Dates"] = dates
    bigDict["Datetimes"] = datetimes
    bigDict["whats"] = "some value"
