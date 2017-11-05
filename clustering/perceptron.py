#!/usr/bin/env python
# -*- coding: utf-8 -*-import sys
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt

class Perceptron(object):
    """docstring for Perceptron."""
    def __init__(self,data,pivot=1,d=3,r=1):
        self.r = r
        self.w = np.ones(d)
        self.data = data
        self.pivot = pivot

    def show(self):
        print self.data

    def __minFit(self,i):
        return np.subtract(self.w, self.data[i]*((self.r)) )

    def __maxFit(self,i):
        return np.add(self.w, self.data[i]*((self.r)) )

    def __processData(self):
        change = False
        for i in range(0,len(self.data)):
            fsal = np.dot(self.data[i], self.w)
            print fsal
            if i < self.pivot:
                if fsal >= 0:
                    print "cambio"
                    change = True
                    self.w =self.__minFit(i)
                    print self.w
            else:
                if fsal <= 0:
                    print " clase 2 cambio"
                    change = True
                    self.w =self.__maxFit(i)
                    print self.w
        print "##### fin de iteracion  ######"
        return change

    def process(self):
        end = True
        while(end):
            if not self.__processData():
                end = False
        return self.w

if __name__ == '__main__':
    data  = []
    data.append(np.array([0,0,1]))
    data.append(np.array([0,1,1]))
    data.append(np.array([1,0,1]))
    data.append(np.array([1,1,1]))
    p = Perceptron(data)
    p.show()
    p.process()
