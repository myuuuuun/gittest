# !/usr/bin/python
# -*- encoding: utf-8 -*-

from __future__ import division, print_function
import math
from random import uniform, normalvariate, shuffle
import numpy as np
import time
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.nan)


def average(probability, asset):
    return np.sum(probability * asset)


def variance(probability, asset):
    ave = average(probability, asset)
    return np.sum(probability * pow(asset - ave, 2))


def std(probability, asset):
    return np.sqrt(variance(probability, asset))


# 資産A, B, Cがあり、状態1〜5がある
# [state1, state2, ..., state5]
probability = np.array([0.2, 0.5, 0.1, 0.15, 0.05])
assetA = np.array([2.56, 1.79, 1.02, 0.26, 0.00])
assetB = np.array([4.73, 1.18, 0.47, 0.47, 0.00])
assetC = np.array([0.00, 0.22, 1.10, 4.39, 0.00])


# 問題2(1) 資産A〜Cの平均と標準偏差
def pro2_1():
    print("Average of assetA: " + str( average(probability, assetA) ))
    print("Average of assetB: " + str( average(probability, assetB) ))
    print("Average of assetC: " + str( average(probability, assetC) ))

    print("SD of assetA: " + str( std(probability, assetA) ))
    print("SD of assetB: " + str( std(probability, assetB) ))
    print("SD of assetC: " + str( std(probability, assetC) ))


#pro2_1()


# 問題2(2) 資産A, Bの組み合わせで達成可能なポートフォリオを図示（横軸標準偏差、縦軸平均）
# p*assetA + (1-p)*assetB とする(0<=p<=1)
def pro2_2():
    aves = []
    stds = []
    for p in np.linspace(0, 1, 21):
        portfolio = p * assetA + (1-p) * assetB
        aves.append(average(probability, portfolio))
        stds.append(std(probability, portfolio))

    print(aves)
    print(stds)

    fig, ax = plt.subplots(figsize=(10, 8))
    plt.title("oppotunity curve of portfolio of asset A & B")

    plt.xlabel("sigma: standard deviation")
    plt.ylabel("mu: average")
    plt.plot(stds, aves, color='b', linewidth=2, label='p*assetA + (1-p)*assetB (0<=p<=1)')
    plt.legend()
    ax.set_ylim(0.8, 2.0)
    ax.set_xlim(0.3, 2.0)
    plt.text(1.57, 1.64, '(1.58, 1.65)\n(p=0. only assetB)', ha = 'left', va = 'top')
    plt.text(0.79, 1.55, '(0.79, 1.55)\n(p=1. only assetA)', ha = 'right', va = 'bottom')
    plt.show()


#pro2_2()


# 問題2(3) 資産A, Bの組み合わせで達成可能なポートフォリオを図示（横軸標準偏差、縦軸平均）
# p*assetA + q*assetB + (1-p-q)*assetC とする(0<=p, q<=p+q<=1)
def pro2_3():
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.title("oppotunity curve of portfolio of asset A & B & C")
    plt.xlabel("sigma: standard deviation")
    plt.ylabel("mu: average")

    # p=(一定)の時のAとBとCの組み合わせで書ける曲線
    plt.plot(0, 0, color='c', label='p*A + q*B + (1-p-q)*C (p=const)')
    for p in np.arange(0, 1.01, 0.02):
        aves = []
        stds = []
        for q in np.arange(0, 1.01-p, 0.02):
            portfolio = p * assetA + q * assetB + (1-p-q) * assetC
            aves.append(average(probability, portfolio))
            stds.append(std(probability, portfolio))
        
        if p == 0:
            plt.plot(stds, aves, color='r', linewidth=2, label='q*B + (1-q)*C (p=0)')

        else:
            plt.plot(stds, aves, color='#88ffff')

        #print(aves)
        #print(stds)
    
    # q=0の時のAとCの組み合わせで書ける曲線
    aves = []
    stds = []
    q = 0
    for p in np.arange(0, 1.02, 0.02):
        portfolio = p * assetA + q * assetB + (1-p-q) * assetC
        aves.append(average(probability, portfolio))
        stds.append(std(probability, portfolio))
    plt.plot(stds, aves, color='g', linewidth=2, label='p*A + (1-q)*C (q=0)')

    # p+q=1の時のAとBの組み合わせで書ける曲線
    aves = []
    stds = []
    for p in np.arange(0, 1.02, 0.02):
        q = 1 - p
        portfolio = p * assetA + q * assetB + (1-p-q) * assetC
        aves.append(average(probability, portfolio))
        stds.append(std(probability, portfolio))
    plt.plot(stds, aves, color='b', linewidth=2, label='p*A + q*B (p+q=1)')

    plt.legend()
    ax.set_ylim(0.8, 2.0)
    ax.set_xlim(0.3, 2.0)
    plt.text(0.79, 1.56, '(0.79, 1.55)\n(p=1, q=0. only assetA)', ha = 'right', va = 'bottom')
    plt.text(1.57, 1.64, '(1.58, 1.65)\n(p=0, q=1. only assetB)', ha = 'left', va = 'top')
    plt.text(1.51, 0.88, '(1.50, 0.88)\n(p, q=0. only assetC)', ha = 'left', va = 'bottom')
    plt.show()


#pro2_3()


