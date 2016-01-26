#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil

#Constants
TICKS = ['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
GREY_HEAT = [chr(27) + '[48;5;' + str(n) + 'm' + ' ' for n in range(232,255)]
NORMAL = chr(27) + '[0m'
SUPERSCRIPT = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
SUBSCRIPT = ['₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉']

class EightPlot:
    def __init__(self):
        pass

    def sparkline(self, label, data):
        """
        Plots sparkline chart given a list of float data
        """
        max_data = max(data)
        min_data = min(data)

        max_label = ''.join([SUPERSCRIPT[int(digit)] for digit in str(int(max_data))])
        min_label = ''.join([SUBSCRIPT[int(digit)] for digit in str(int(min_data))])

        interval_width = ceil((max_data-min_data) / 7.0) if max_data > min_data\
                else ceil(max_data / 7.0)

        output = ''.join([TICKS[int(round((each-min_data) / interval_width))]
                         if round(each) != 0 else TICKS[0] for each in data])

        print '%7.7s %70s\t %6s%-7s' % (label, output, min_label, max_label)
        
    def heatline(self, label, data):
        """
        Plots heatline chart given a list of float data
        """
        max_data = max(data)
        min_data = min(data)
    
        interval_width = ceil((max_data-min_data) / 22.0) if max_data > min_data\
                else ceil(max_data / 22.0)
    
        output = ''.join([GREY_HEAT[int(round((each-min_data) / interval_width))]
                         if round(each) != 0 else GREY_HEAT[0] for each in data])
    
        print '%7.7s %70s%s' % (label, output, NORMAL)