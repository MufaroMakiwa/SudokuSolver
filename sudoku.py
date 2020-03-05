#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 01:34:57 2020

@author: mufaromakiwa
"""
bo=[[2,5,0,0,0,3,0,9,1],
    [3,0,9,0,0,0,7,2,0],
    [0,0,1,9,2,6,3,0,0],
    [0,0,0,5,6,8,0,0,3],
    [0,1,0,0,4,0,0,0,0],
    [6,0,3,0,0,0,0,5,0],
    [1,3,2,0,0,0,0,7,0],
    [0,0,0,7,3,4,0,6,0],
    [7,6,4,0,1,0,0,0,0]]

bo=[[0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]]

def print_board(bo):

    for i in range(len(bo)+1):
        if i==len(bo):
            print(' - - - - - - - - - - - - -')
            break
        if i%3==0:
            print(' - - - - - - - - - - - - -')

        for j in range(len(bo[i])+1):
            if j==len(bo[i]):
                print(' |')
                break
            if j%3==0:
                print(' | '+str(bo[i][j]), end='')
            else:
                print(' '+str(bo[i][j]), end='')


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j]==0:
                return (i, j) # row, column


def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i]==num and pos[1]!=i:
            return False

    for i in range(len(bo)):
        if bo[i][pos[1]]==num and pos[0]!=i:
            return False

    box_x=pos[1]//3
    box_y=pos[0]//3


    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if bo[i][j]==num and (i, j)!=pos:
                return False

    return True

def solve(bo):
    
    find=find_empty(bo)
    if not find:
        return True
    
    else:
        row, col=find
    
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col]=i

            if solve(bo):
                return True
            
            bo[row][col]=0
    
    return False

if solve(bo):
    print_board(bo)