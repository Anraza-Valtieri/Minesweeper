"""NEIGHBOUR CLASS"""
import threading, sys, random, time
import cPickle as pickle
from datetime import datetime
class Num:
    minesaround = {}
    neighbours = set()

    @staticmethod
    def create(self, pointer):
        """
        This method creates the neighbour maps.
        It creates a set with all surrounding cells of XY for ever cell in the map.

        We require the pointer to mainmap for it to be able to call data from the main map
        :param self:
        :return:
        """
        # For each square, gives the set of its neighbours
        mainmap = pointer
        self.neighbours = {}
        for (x, y) in mainmap.xymap:
            self.neighbours[x, y] = set((nx, ny)
                                        for nx in [x - 1, x, x + 1]
                                        for ny in [y - 1, y, y + 1]
                                        if (nx, ny) != (x, y)
                                        if (nx, ny) in mainmap.xymap)
        # print "------ neighbours ------\n"
        # print self.neighbours
    @staticmethod
    def calculatepoint(self,xy,pointer):
        """
        This method counts the amount of mines around cell XY.
        Returns the value

        We require the pointer to bombs for it to be able to call data from
        :param self:
        :param xy:
        :return:

        s = set A
        t = set B
        Average case: O(min(len(s), len(t))
        Worst Case: O(len(s) * len(t))
        """
        # print "------ START, BOMB::calculatepoint ------"
        c = datetime.now()
        # print self.neighbours
        # print pointer.mines
        #print str(self.neighbours[xy].intersection(pointer.mines))
        self.minesaround[xy] = len(self.neighbours[xy].intersection(pointer.mines)) # O(len(s) * len(t))
        #self.minesaround[xy] = len(self.neighbours[xy] & pointer.mines) # O(len(s) * len(t))
        # print "Mines around are " + str(self.minesaround[xy])
        d = datetime.now()
        delta = d - c
        # print "[calculatepoint]TOTAL Time Taken: " + str(delta.total_seconds() * 1000) + "ms"  # milliseconds
        # print "------ END, BOMB::calculatepoint ------\n"
        return self.minesaround[xy]

    @staticmethod
    def recalculatepoint(self, pointer):
        self.create(self, pointer)
