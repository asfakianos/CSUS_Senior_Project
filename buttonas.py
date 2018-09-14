# button.py
# Written by Alexander Sfakianos
# October 4th, 2016
# Creates button class for factory.py and blackjack.py

from graphics import *
from math import *


class Buttons:
   """Allows buttons to be created on demand with location and text."""

   def __init__(self, win, center, width, height, label):
      self.xMod, self.yMod = width / 2, height / 2
      self.xC, self.yC = center.getX(), center.getY()
      self.xMin = self.xC - self.xMod
      self.xMax = self.xC + self.xMod
      self.yMin = self.yC - self.yMod
      self.yMax = self.yC + self.yMod
      pt1 = Point(self.xMin, self.yMin)
      pt2 = Point(self.xMax, self.yMax)
      self.outline = Rectangle(pt1, pt2)
      self.outline.setFill('lightgray')
      self.outline.draw(win)
      self.label = Text(center, label)
      self.label.draw(win)
      self.deactivate()

   def clicked(self, pt):
      wasClicked = False
      if self.xMin <= pt.getX() and self.xMax >= pt.getX():
         if self.yMin <= pt.getY() and self.yMax >= pt.getY():
            if self.active == True:
               wasClicked = True
      return wasClicked

   def getLabel(self):
      return self.label.getText()

   def setLabel(self, label):
      self.label.setText(label)

   def activate(self):
      self.label.setFill('black')
      self.outline.setWidth(2)
      self.active = True

   def deactivate(self):
      self.label.setFill('darkgrey')
      self.outline.setWidth(1)
      self.active = False

   def remove(self):
      """Undraws the given button"""
      self.outline.undraw()
      self.label.undraw()

   def buttonMove(self, pt):
      """Moves the button to the given point"""
      newX, newY = pt.getX(), pt.getY()
      moveX, moveY = newX - self.xC, newY - self.yC
      self.outline.move(moveX, moveY)
      self.label.move(moveX, moveY)
      self.xC, self.yC = newX, newY
      self.xMin = self.xC - self.xMod
      self.xMax = self.xC + self.xMod
      self.yMin = self.yC - self.yMod
      self.yMax = self.yC + self.yMod
