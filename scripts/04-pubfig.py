#!/usr/bin/env python

##################################################################
# Publication quality figure setup
#
# 1. Dependency:
#  1.1 matplotlib
#
# 2. Usage:
#  2.1 Make a folder in the site-packages folder of python,
#      e.g. $HOME/anaconda2/lib/python2.7/site-packages/user
#  2.2 Copy this file to that folder
#  2.3 Create a __init__.py file to make it a module
#
# 3. Troubleshooting:
#  3.1 Error : matplotlib - Font family [u'sans-serif'] not found
#  3.2 Solution:
#   (1) sudo apt-get install msttcorefonts -qq
#   (2) delete the content of .cache/matplotlib
##################################################################

def setup(labelfont=16, tickfont=16, showminorticks=False):
    from matplotlib import rcParams
    # canvas setup
    rcParams['axes.labelsize']=labelfont
    rcParams['axes.linewidth']=2
    # x ticks setup
    rcParams['xtick.labelsize']=tickfont
    rcParams['xtick.direction']='in'
    rcParams['xtick.top']=True
    rcParams['xtick.minor.visible']=showminorticks
    rcParams['xtick.major.width']=2
    rcParams['xtick.major.size']=5
    rcParams['xtick.minor.top']=True
    rcParams['xtick.minor.width']=1.5
    rcParams['xtick.minor.size']=4
    # y ticks setup
    rcParams['ytick.labelsize']=tickfont
    rcParams['ytick.direction']='in'
    rcParams['ytick.right']=True
    rcParams['ytick.minor.visible']=showminorticks
    rcParams['ytick.major.width']=2
    rcParams['ytick.major.size']=5
    rcParams['ytick.minor.right']=True
    rcParams['ytick.minor.width']=1.5
    rcParams['ytick.minor.size']=4
    # font family
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['Times New Roman']
    rcParams['mathtext.fontset'] = 'cm'

def save(img_name):
    from matplotlib import pyplot
    pyplot.savefig(img_name, dpi=300, bbox_inches='tight')

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    setup()
    x = np.linspace(-100, 100, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()