#!/usr/bin/env python

# Load Libraries:{{{
import numpy as np ############################# Linear Algebra Library
from scipy.optimize import fsolve
import scipy ############################# Linest
from scipy import stats ################## Statistic Functions
import matplotlib ######################## Plotting
# Import Publication Style Fonts for Figures:
matplotlib.use('Agg')
fontfamily={'family':'sans-serif','sans-serif':['Arial']}
from matplotlib import pyplot as plt
plt.rc('font', **fontfamily)
import matplotlib.cm as cm

# }}}

# Simple Plot:{{{

def simple_plot(x,y,xlabel='x',ylabel='y',name=None,size=111,Type='scatter',
        color=False,fig_size=(12,10),invert_x_axis=False,fit=False,order=None,
        xLine=None,yLine=None,
        annotate_text=None,text_x=0,text_y=0,
        annotate_x=0,annotate_y=0,
        arrow='->'):
    '''
    Returns a plot and saves it to the working directory
    unless stated otherwise.
    x = numpy array
    y = numpy array
    xlabel,ylabel,name = strings
    size = axis size
    color = color of line
    fig_size = (x,y)
    '''
    marks = ['o','D','2','>','*',',',"4","8","s",
             "p","P","*","h","H","+","x","X","D","d"]
    colors = ['k','b','g','r','c','m','y',
              'k','b','g','r','c','m','y']

    fig = plt.figure(figsize=fig_size)
    ax = fig.add_subplot(size)

    if Type=='scatter':
        if color==False:
            ax.scatter(x,y,color='k')
        else:
            ax.scatter(x,y,color=color)

    if Type=='line':
        if color==False:
            ax.plot(x,y,'k')
        else:
            ax.plot(x,y,color)
    if fit==True:
        ax.plot(x,y,label="_nolegend_")
        z = np.polyfit(x, y, order)
        n_coeff = len(z)
        #################################################
        p = np.poly1d(z)
        ax.plot(x,p(x),"k--",label="_nolegend_")
        # the line equation:
        print 'LINEST data:'
        if order==1:
            print "y=%.6f*x+(%.6f)"%(z[0],z[1])
            print scipy.stats.linregress(x,y)
        elif order==2:
            print "y=%.6f*x**2.+(%.6f)*x+(%.6f)"%(z[0],z[1],z[2])
        elif order==3:
            print "y=%.6f*x**3.+(%.6f)*x**2.+(%.6f)*x+(%.6f)"%(z[0],z[1],z[2],z[3])
        elif order==4:
            print "y=%.6fx**4.+(%.6f)*x**3.+(%.6f)*x**2.\
                    +(%.6f)*x+(%.6f)"%(z[0],z[1],z[2],z[3],z[4])
        else:
            print 'You need to add a greater order of polynomials to the script'

        print scipy.stats.chi2(y)
        print scipy.stats.ttest_ind(x, y, axis=0, equal_var=True)
        #eq = "y=%.6fx+(%.6f)"%(z[0],z[1])

    ax.set_xlabel('%s'%xlabel, fontsize=16)
    ax.set_ylabel('%s'%ylabel, fontsize=16)
    # Does the x-axis need to be reverse?
    if invert_x_axis==True:
        plt.gca().invert_xaxis()
    # Setting the ticks and tick marks
    ticks = [ax.xaxis.get_minor_ticks(),
             ax.xaxis.get_major_ticks()]
    marks = [ax.get_xticklabels(),
            ax.get_yticklabels()]
    for k in range(0,len(ticks)):
        for tick in ticks[k]:
            tick.label.set_fontsize(16)
    for k in range(0,len(marks)):
        for mark in marks[k]:
            mark.set_size(fontsize=16)
            mark.set_rotation(s=15)
    if annotate_text != None:
        ax.annotate(r'%s'%annotate_text,
                xy=(annotate_x,annotate_y),xytext=(text_x,text_y),
                arrowprops=dict(facecolor='black', arrowstyle=arrow),
                fontsize=16)
    if xLine!=None:
        ax.axhline(xLine)
    if yLine!=None:
        ax.axhline(yLine)
    fig.tight_layout
    if name==None:
        pass
    else:
        fig.savefig('%s'%name)
    fig.show()


# }}}

# 1 by 2 plot:{{{

def onebytwo(x1,y1,x2,y2,x1label='x',y1label='y',x2label='x',y2label='y',
        Type1='scatter',Type2='scatter',name=None,
        color=False,fit1=False,fit2=False,fig_size=(12,10),size1=211,size2=212,
        order1=None,order2=None,invert_x1_axis=False,invert_x2_axis=False,
        xLine1=None,yLine1=None,xLine2=None,yLine2=None,
        annotate_text1=None,text_x1=0,text_y1=0,
        annotate_x1=0,annotate_y1=0,
        annotate_text2=None,text_x2=0,text_y2=0,
        annotate_x2=0,annotate_y2=0,
        arrow='->'):

    fig = plt.figure(figsize=fig_size)
    ax = fig.add_subplot(111)    # The big subplot
    ax1 = fig.add_subplot(size1)
    ax2 = fig.add_subplot(size2)
    colors = ['k','b','g','r','c','m','y',
              'k','b','g','r','c','m','y']

    ax.tick_params(labelcolor='w', top='off', bottom='off', left='off', right='off')

    if Type1=='scatter':
        if color==False:
            ax1.scatter(x1,y1,c='k')
        else:
            ax1.scatter(x1,y1,c=color)
    if Type1=='line':
        if color==False:
            ax1.plot(x1,y1,'k')
        else:
            ax1.plot(x1,y1,color)

    if fit1==True:
        ax1.plot(x1,y1,label="_nolegend_")
        z = np.polyfit(x1, y1, order1)
        n_coeff = len(z)
        p = np.poly1d(z)
        ax1.plot(x1,p(x1),"k--",label="_nolegend_")
        # the line equation:
        print 'LINEST data:'
        print "y=%.6fx+(%.6f)"%(z[0],z[1])
        print scipy.stats.chi2(y1)
        print scipy.stats.linregress(x1,y1)
        print scipy.stats.ttest_ind(x1, y1, axis=0, equal_var=True)
        eq1 = "$y=%.4Gx+(%.4G)$"%(z[0],z[1])
        x_1,y_1 = np.average([x1]),np.average([y1])
        ax1.annotate('%s'%eq1,
            xy=(x_1,y_1),
            xytext=(x_1,y_1),fontsize=16)

        # Subplot with linear fitting:
    ax1.set_xlabel('%s'%x1label, fontsize=16)
    ax1.set_ylabel('%s'%y1label, fontsize=16)

    if Type2=='scatter':
        if color==False:
            ax2.scatter(x2,y2,c='k')
        else:
            ax2.scatter(x2,y2,c=color)
    if Type2=='line':
        if color==False:
            ax2.plot(x2,y2,'k')
        else:
            ax2.plot(x2,y2,color)
    if fit2==True:
        ax2.plot(x2,y2,label="_nolegend_")
        z = np.polyfit(x2, y2, order2)
        n_coeff = len(z)
        p = np.poly1d(z)
        ax2.plot(x2,p(x2),"k--",label="_nolegend_")
        # the line equation:
        print 'LINEST data:'
        print "y=%.6fx+(%.6f)"%(z[0],z[1])
        print scipy.stats.chi2(y2)
        print scipy.stats.linregress(x2,y2)
        print scipy.stats.ttest_ind(x2, y2, axis=0, equal_var=True)
        eq2 = "$y=%.4Gx+(%.4G)$"%(z[0],z[1])
        x_2,y_2 = np.average([x2]),np.average([y2])
        ax2.annotate('%s'%eq2,
            xy=(x_2,y_2),
            xytext=(x_2,y_2),fontsize=16)

    # Does the x1-axis need to be reverse?
    if invert_x1_axis==True:
        ax1.gca().invert_xaxis()
     # Does the x2-axis need to be reverse?
    if invert_x2_axis==True:
        ax2.gca().invert_xaxis()

    ax2.set_xlabel('%s'%x2label, fontsize=16)
    ax2.set_ylabel('%s'%y2label, fontsize=16)
    ticks = [ax2.xaxis.get_minor_ticks(),ax1.yaxis.get_minor_ticks(),
             ax2.xaxis.get_major_ticks(),ax1.yaxis.get_major_ticks()]
    marks = [ax1.get_xticklabels(),ax2.get_xticklabels(),
            ax1.get_yticklabels(),ax2.get_yticklabels()]
    for k in range(0,len(ticks)):
        for tick in ticks[k]:
            tick.label.set_fontsize(16)
    for k in range(0,len(marks)):
        for mark in marks[k]:
            mark.set_size(fontsize=16)
            mark.set_rotation(s=15)
    if annotate_text1 != None:
        ax1.annotate(r'%s'%annotate_text1,
                xy=(annotate_x1,annotate_y1),xytext=(text_x1,text_y1),
                arrowprops=dict(facecolor='black', arrowstyle=arrow),
                fontsize=16)
    if annotate_text2 != None:
        ax2.annotate(r'%s'%annotate_text2,
                xy=(annotate_x2,annotate_y2),xytext=(text_x2,text_y2),
                arrowprops=dict(facecolor='black', arrowstyle=arrow),
                fontsize=16)
    if xLine1!=None:
        ax1.axhline(xLine1)
    if yLine1!=None:
        ax1.axhline(yLine1)
    if xLine2!=None:
        ax2.axhline(xLine2)
    if yLine2!=None:
        ax2.axhline(yLine2)

    fig.tight_layout()
    if name!=None:
        fig.savefig('%s'%name)
    fig.show()

# }}}


