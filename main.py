#LYIN MYA
#LYM284
#11192838
#COM145
#SECTION04

# CMPT 145 Course material
# Copyright (c) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.
# 
# Synopsis:
#   Defines the Statistics ADT
#   Calculate mean and variance and other statistical summaries  
#   of numeric data.

# Implementation
# Do the calculations without storing all the data!
# Use a Python dictionary as a record to store three quantities:
#   _count':     the number of data values added
#   _avg':       the running average of the values added

# These values can be modified every time a new data value is 
# added, so that the mean and variance can be calculated quickly  
# as needed.  This approach means that we do not need to store  
# the data values themselves, which could save a lot of space.
#
# NOTE: This file does not contain the full ADT as shown in class.  
#       The calculations for var() and sampvar() were removed to 
#       keep the exercise concise.

class Statistics:
    def __init__(self):
        """
        Purpose:
            Initialize a Statistics object instance.
        """
        self.__count = 0      # how many data values seen so far
        self.__avg = 0        # the running average so far
        self.__range = 0 #range seen so far
        self.__mode = 0 #mode seen so far
        self.__max = 0 #max value so far
        self.__min = 0 #min value so far
        self.__list_of_nums = [] #list of numbers so far

    def add(self, value):
        """
        Purpose:
            Use the given value in the calculation of mean and 
            variance.
        Pre-Conditions:
            :param value: the value to be added
        Post-Conditions:
            none
        Return:
            :return none
        """
        self.__list_of_nums.append(value)
        self.__count += 1
        k = self.__count           # convenience
        diff = value - self.__avg  # convenience
        self.__avg += diff / k

        if self.__min is None:
            self.__min = value
            self.__max = value
        else:
            self.__min = min(value, self.__min)
            self.__max = max(value, self.__max)

        self.__range = (self.__max) - (self.__min)

    def mean(self):
        """
        Purpose:
            Return the average of all the values seen so far.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
            Note: if no data has been seen, 0 is returned.
                  This is clearly false.
        """
        return self.__avg

    def count(self):
        """
        Purpose:
            Return the number of values seen so far.
        Post-conditions:
            (none)
        Return:
            The number of values seen so far.
            Note: if no data has been seen, 0 is returned.
                  This is clearly false.
        """
        return self.__count

    def min(self):
        """
        Purpose:
            Return the minimum of all the values seen so far.
        Pre-conditions:
            stat: the Statistics record
        Post-conditions:
            (none)
        Return:
            The minimum of the data seen so far.
            Note: if no data has been seen, None is returned.
        """
        return self.__min

    def max(self):
        """
        Purpose:
            Return the maximum of all the values seen so far.
        Pre-conditions:
            stat: the Statistics record
        Post-conditions:
            (none)
        Return:
            The maximum of the data seen so far.
            Note: if no data has been seen, None is returned.
        """
        return self.__max

    def range(self):
        """
        Purpose:
            Return the range of all the values seen so far.
        Pre-conditions:
            stat: the Statistics record
        Post-conditions:
            (none)
        Return:
            The range of the data seen so far.
            Note: if no data has been seen, None is returned.
        """
        return self.__range

    def mode(self):
        """
        Purpose:
            Return the mode of all the values seen so far.
        Pre-conditions:
            stat: the Statistics record
        Post-conditions:
            (none)
        Return:
            The mode of the data seen so far.
            Note: if no data has been seen, None is returned.
        """
        max_count = (0, 0)
        for num in self.__list_of_nums:
            occurences = self.__list_of_nums.count(num)
            if occurences > max_count[0]:
                max_count = (occurences, num)
        return max_count[1]





stat = Statistics()

stat.add(1)
stat.add(0)
stat.add(2)
print(stat.mode())