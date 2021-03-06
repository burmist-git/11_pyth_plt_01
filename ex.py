#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date        : Fri Dec  4 13:54:00 CET 2020
Autor       : Leonid Burmistrov
Description : Simple reminder-training example.

'''

import numpy as np
import math
import matplotlib.pyplot as plt

def printinfo(func):
    def wrapper():
        print("")
        print("Simple reminder-training example. Function name : {} --> ".format(func.__name__))
        func()
    return wrapper

@printinfo
def plot_errorbar():
    fig = plt.figure()
    x = np.arange(10)
    y = 2.5 * np.sin(x / 20 * np.pi)
    yerr = np.linspace(0.05, 0.2, 10)
    
    plt.errorbar(x, y + 3, yerr=yerr, label='both limits (default)')
    
    plt.errorbar(x, y + 2, yerr=yerr, uplims=True, label='uplims=True')
    
    plt.errorbar(x, y + 1, yerr=yerr, uplims=True, lolims=True,
                 label='uplims=True, lolims=True')
    
    upperlimits = [True, False] * 5
    lowerlimits = [False, True] * 5
    plt.errorbar(x, y, yerr=yerr, uplims=upperlimits, lolims=lowerlimits,
                 label='subsets of uplims and lolims')
    
    plt.legend(loc='lower right')    
    
    plt.show()

@printinfo
def plot_scatter():
    
    np.random.seed(19680801)
    x = np.random.random(100)*5
    y = np.random.random(100)*5

    fig = plt.figure(num=None, figsize=None, dpi=None, facecolor=None,
                     edgecolor=None, frameon=True, clear=False)
    fig.add_axes([0.1, 0.1, 0.85, 0.85])
    
    plt.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None,
                vmin=None, vmax=None, alpha=None, linewidths=None,
                edgecolors=None, plotnonfinite=False, data=None)

    plt.title('The title')
    plt.xlim(-0.5, 5.5)
    plt.ylim(-0.5, 5.5)
    plt.xlabel('The x lable')
    plt.ylabel('The y lable')
    plt.show()

@printinfo
def plot_subplot01():

    np.random.seed(19680801)
    x1 = np.random.random(100)*5
    y1 = np.random.random(100)*5
    x2 = np.random.random(100)*5
    y2 = np.random.random(100)*5

    # using the variable axs for multiple Axes
    fig, axs = plt.subplots( nrows=2, ncols=1,
                             sharex=False, sharey=False,
                             squeeze=True, subplot_kw=None,
                             gridspec_kw=None,
                             figsize=(10,12))
    #plt.tight_layout()

    # 
    axs[0].plot(x1, y1)
    axs[0].set_xbound(-0.5,5.5)
    axs[0].set_ybound(-0.5,5.5)
    axs[0].set_title('The title 0')
    axs[0].set_xlabel('The x lable 0')
    axs[0].set_ylabel('The y lable 0')
    axs[0].set_position([0.05,0.55,0.9,0.40])
    #
    axs[1].scatter(x2, y2)
    axs[1].set_xbound(-0.5,5.5)
    axs[1].set_ybound(-0.5,5.5)
    axs[1].set_title('The title 1')
    axs[1].set_xlabel('The x lable 1')
    axs[1].set_ylabel('The y lable 1')
    axs[1].set_position([0.05,0.05,0.9,0.40])
    #
    print(type(axs))
    print(type(axs[0]))
    
    plt.show()    

def getHistBins(nBins,xMin,xMax):
    binW = (xMax - xMin)/nBins
    return [xMin + binW*i for i in range(nBins+1)]

def generateHistData(nn,x0,sigma):
    return [sigma[i]*np.random.randn(nn[i], 1) + x0[i] for i in range(len(nn))]

@printinfo
def plot_hist():

    classType = [0,1]
    nn    = [10000,1000]
    x0    = [10,11]
    sigma = [0.1,0.1]
    
    '''
    classType = [0,1,2,3,4]
    nn    = [100,500,1000,5000,10000]
    x0    = [0,1,2,3,4]
    sigma = [0.3,0.3,0.8,0.2,10.0]
    '''
    
    nPlots=len(nn) + 2
    ncols=math.ceil(nPlots**(0.5))
    nrows=int(nPlots/ncols)+math.ceil(nPlots/ncols-int(nPlots/ncols))
    print(ncols)
    print(nrows)
    
    nBins = 300
    nSigma = 4
    xMin = int(np.array(x0).min() - math.ceil(nSigma*np.array(sigma).max()))
    xMax = int(np.array(x0).max() + math.ceil(nSigma*np.array(sigma).max()))
    #xMin = 8
    #xMax = 12
    bins = getHistBins(nBins,xMin,xMax)
    print(len(bins))
    print(xMin)
    print(xMax)
    print(nSigma*np.array(sigma).max())
    
    data = generateHistData(nn,x0,sigma)
    datay = [classType[i]*np.ones(nn[i]) for i in range(len(x0))]
    
    # using the variable axs for multiple Axes
    fig, axs = plt.subplots( nrows=nrows, ncols=ncols,
                             sharex=False, sharey=False,
                             squeeze=True, subplot_kw=None,
                             gridspec_kw=None,
                             figsize=(18,8))
    plt.tight_layout()

    for i in range(nrows):
        for j in range(ncols):
            plotID=i*ncols + j
            if(plotID<len(nn)):
                axs[i,j].hist(data[plotID], bins=bins)
            elif (plotID == len(nn)):
                axs[i,j].hist(np.vstack(data), bins=bins)                
            elif (plotID == (len(nn)+1)):
                axs[i,j].scatter(np.vstack(data),np.hstack(datay))                
    
    plt.show()
    
def main():
    plot_errorbar()
    plot_scatter()
    plot_subplot01()
    plot_hist()
    
if __name__ == "__main__":
    main()
