"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import sys
import first
import thinkstats2

def Mode(hist):
    """Returns the value with the highest frequency.

    hist: Hist object

    returns: value from Hist
    """
    p, x = max([(p, x) for x, p in hist.Items()])
    return x


def AllModes(hist):
    """Returns value-freq pairs in decreasing order of frequency.

    hist: Hist object

    returns: iterator of value-freq pairs
    """
    return sorted(hist.Items(), key=lambda item: item[1], reverse=True)


def showdiff(varname, series1, series2):
    """
    prints difference description of two series
    Args:
        varname:
        series1:
        series2:

    Returns:
        difference of mean between series
    """
    len1 = len(series1)
    len2 = len(series2)

    mean1 = series1.mean()
    mean2 = series2.mean()
    mean0 = (mean1 * len1 + mean2 * len2) / (len1 + len2)

    var1 = series1.var()
    var2 = series2.var()
    var0 = (var1 * len1 + var2 * len2) / (len1 + len2)

    diff = mean1 - mean2
    pctdmean = diff / mean0 * 100
    d = thinkstats2.CohenEffectSize(series1, series2)

    print("\nDifference for " + varname)
    print("Mean: Firsts {0:f}, Others {1:f}, Both {2:f}".format(mean1, mean2, mean0))
    print("Variance: Firsts {0:f}, Others {1:f}, Both {2:f}".format(var1, var2, var0))
    print("Mean Difference: {0:f}".format(diff))
    print("Diff percent relative to both mean {0:f}".format(pctdmean))
    print("Cohen d: {0:f}".format(d))

    return diff


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    live, firsts, others = first.MakeFrames()
    hist = thinkstats2.Hist(live.prglngth)

    # test Mode    
    mode = Mode(hist)
    print('Mode of preg length', mode)
    assert(mode == 39)

    # test AllModes
    modes = AllModes(hist)
    assert(modes[0][1] == 4693)

    # MetisDSp Q1. Excercise 2-4 Explore totalwgt_lb for first babies vs. others
    # df = nsfg.ReadFemPreg()
    # live = df[df.outcome == 1] # DataFrame of all live births
    # firsts = live[df.birthord==1] # DataFrame of first babies
    # others = live[df.birthord>1] # DataFrom of others
    lb_diff = showdiff("totalwgt_lb", firsts.totalwgt_lb, others.totalwgt_lb)
    print("Difference: {0:f} ozs".format(lb_diff * 16))

    weeks_diff = showdiff("prglngth", firsts.prglngth, others.prglngth)
    print("Difference: {0:f} days".format(weeks_diff * 7))
    print("Difference: {0:f} hours".format(weeks_diff * 7 * 24))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
