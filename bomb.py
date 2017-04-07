""" BOMB CLASS """
import threading, sys, random, time, pickle
from datetime import datetime
class Bombs:
    mines = set()
    empty_remain = 0
    mines_number = 0
    @staticmethod
    def create(self, columns, rows, density,pointer):
        """
        This method creates the maps for bombs.
        :param self:
        :param columns:
        :param rows:
        :param density:
        :return:
        """
        mines_number = int(density * columns * rows)
        empty_remain = int(columns * rows - mines_number)
        self.mines = set()
        while len(self.mines) < mines_number:
            self.mines.add((random.randrange(columns),
                             random.randrange(rows)))
        # print "------ mines ------"
        # print self.mines
        # print "Total mines:" + str(mines_number)
        # print "Total empty:" + str(empty_remain)

    @staticmethod
    def open(self, xy, pointer):
        """
        This will check xy if it is a mine.
        If Mine it will return a 1
        Else it will count the mines around the cell and return the value (Unused)

        :param self:
        :param xy:
        :return:

        Average case: O(1)
        Worst Case: O(n)
        """
        num = pointer
        # print "------ START, BOMB::open ------\n"

        if xy in self.mines:
            # print "------ BOOM! ------\n"
            # print "------ END, BOMB::open ------\n"
            return True
        else:
            # print "Total mines around = " + str(num.calculatepoint(num,xy,self))
            # print "------ END, BOMB::open ------\n"
            return False

    @staticmethod
    def dumpmap(self,pointer):
        """
        Call this function to create seedfile to load mines.

        We require the pointer to bombs for it to be able to call data from
        :param self:
        :return:
        """
        timestr = time.strftime("%Y%m%d-%H%M%S")
        thefile = open(timestr, 'w')
        print "Seed file created "+str(timestr)
        with open(str(timestr), 'wb') as fp:
             tosave = []
             tosave.append(pointer.columns)
             tosave.append(pointer.rows)
             tosave.append(pointer.xymap)
             tosave.append(self.mines)
             pickle.dump(tosave, fp)
        return timestr
        #for item in self.mines:
        #    print>> thefile, item

    @staticmethod
    def dumpmap2(self, pointer):
        """
        Call this function to create seedfile to load mines.

        We require the pointer to bombs for it to be able to call data from
        :param self:
        :return:
        """
        timestr = time.strftime("laststate")
        thefile = open(timestr, 'w')
        print "Seed file created " + str(timestr)
        with open(str(timestr), 'wb') as fp:
            tosave = []
            tosave.append(pointer.columns)
            tosave.append(pointer.rows)
            tosave.append(pointer.xymap)
            tosave.append(self.mines)
            tosave.append(pointer.opened)
            print str(pointer.opened)
            pickle.dump(tosave, fp)
        return timestr
        # for item in self.mines:
        #    print>> thefile, item

    @staticmethod
    def read(self, name, pointer, pointer2):
        """
        Call this and Pass the seed file name here in args to load mine files

        We require the pointer to mainmap and num for it to be able to set data for them
        :param self:
        :param name:
        :return:
        """
        mappointer = pointer
        numpointer = pointer2
        self.mines = set()
        try:
            with open(name, 'rb') as fp:
                loadeddata = set()
                loadeddata = pickle.load(fp)
                mappointer.columns = loadeddata[0]
                print "Read Col: " + str(loadeddata[0])
                mappointer.rows = loadeddata[1]
                print "Read Row: " + str(loadeddata[1])
                mappointer.xymap = loadeddata[2]
                self.mines = loadeddata[3]
        except:
            print "Failed to load "+str(name)
        print "------ mines::READ::xymap ------"
        print mappointer.xymap
        print "------ mines::READ ------"
        print self.mines
        print "Total mines:" + str(len(self.mines)) +" Loaded!"
        numpointer.recalculatepoint(numpointer, mappointer) # Init neighbouring cell arrays

    @staticmethod
    def readstate(self, name, pointer, pointer2):
        """
        Call this and Pass the seed file name here in args to load mine files

        We require the pointer to mainmap and num for it to be able to set data for them
        :param self:
        :param name:
        :return:
        """
        mappointer = pointer
        numpointer = pointer2
        self.mines = set()
        try:
            with open(name, 'rb') as fp:
                loadeddata = set()
                loadeddata = pickle.load(fp)
                mappointer.columns = loadeddata[0]
                print "Read Col: " + str(loadeddata[0])
                mappointer.rows = loadeddata[1]
                print "Read Row: " + str(loadeddata[1])
                mappointer.xymap = loadeddata[2]
                self.mines = loadeddata[3]
                print str(mappointer.preopened)
                mappointer.preopened = loadeddata[4]
                print str(mappointer.preopened)
        except:
            print "Failed to load " + str(name)

        print "------ mines::READ::xymap ------"
        print mappointer.xymap
        print "------ mines::READ ------"
        print self.mines
        print "Total mines:" + str(len(self.mines)) + " Loaded!"
        numpointer.recalculatepoint(numpointer, mappointer)  # Init neighbouring cell arrays