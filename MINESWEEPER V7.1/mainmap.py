""" MAIN MAP CLASS"""
import threading, sys, random, time
import cPickle as pickle
from datetime import datetime
class Mainmap:
    @staticmethod
    def create(self, columns, rows):
        """
        Create Map
        :param self:
        :param columns:
        :param rows:
        :return:
        """
        self.columns = columns
        self.rows = rows
        self.xymap = set((x, y)
            for x in range(self.columns)
            for y in range(self.rows))
        self.opened = set()  # Resets sets opened. Required to win game
        self.preopened = set()  # Resets sets opened. Required to win game
        # print "------ xymap ------"
        # print self.xymap

    @staticmethod
    def open(self,xy, pointer1, pointer2):
        """
        Call this to open cells, this will call open functions in bombs and add xy into opened set

        :param self:
        :param xy:
        :return:
        """
        newbomb = pointer1
        newnum = pointer2
        self.opened.add(xy)
        # print "------ START, MAINMAP::opened ------"
        # print self.opened
        state = newbomb.open(newbomb,xy, pointer2)
        # print "------ END, MAINMAP::opened ------\n"
        return state