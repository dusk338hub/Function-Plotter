
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QMessageBox
import re
from PyQt5 import QtCore, QtGui, QtWidgets

def validInputs(function,minX,maxX):
    answer="true"
    try: # check if the minimum and maximum value valid (integer)
        forCheckingMinX = int(minX)
        forCheckingMaxX = int(maxX)
    except Exception:
        answer = "Please enter a valid values for minimum and maximum"
        return answer
    if forCheckingMinX>forCheckingMaxX:
        answer="The minimum must be smaller than the maximum"
    if function=="": #
        answer="please enter the function "
    if minX=="" or maxX=="":
        answer="The maximum and maximum must be given "
    toMatch = "(-)?(\d+$)|((-)?(\d+[+-])?(\d+[\*\/])?[xX](\^\d+)?([+-](\d+)?([\*\/][xX](\^\d+)?)?)*)*$"
    matched = re.match(toMatch, function)
    if not matched:
        answer="Please enter a valid function"
    return answer