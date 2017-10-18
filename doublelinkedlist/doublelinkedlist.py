#!/usr/bin/env python
# coding=utf-8
"""
# doublelinkedlist : A Python Library to sdouble linked lists

Summary :
    Support for double linked lists and utility functions, including iteraton, inclusion testing, indexing, slicing etc

Use Case :
    A want a double linked list so that I can prove the concept

Testable Statements :
    ...
"""

from version import __version__

__author__ = "Tony Flury anthony.flury@btinternet.com"
__created__ = "04 Jul 2017"

class Node():
    """ Sub class for all Nodes on the list - use as a mixin only"""
    def _attach(self, parent, next_node, prev_node):
        self._next = next_node
        self._prev = prev_node
        self._parent = parent

    def next(self):
        """Go to the next node"""
        return self._next if parent._forward else self._prev

    def previous(self):
        """Go to the previous node"""
        return self._prev if parent._forward else self._next
 
class LinkedList():

    class iterator():
        """ iterator to support iterator protocol"""
        def __init__(self, parent, forward):
            self._current = None
            self._forward = forward
            self._parent = parent

        def __next__(self):
            """Iterate to the 'next' entry in the list
            The meaning of 'next' depends on the direction"""
            if self._current is None:
                self._current = self._parent._head if\
                                self._forward else self._parent._tail
            else:
                self._current = self._current._next if\
                                self._forward else self._current._prev

            if self._current is None:
                raise StopIteration
            else:
                return self._current


        def __iter__(self):
            return self.iterator( parent=self, forward=self._forward)
  
    def __init__(self):
        """Initialise a linked list"""
        self._head = None
        self._tail = None
        self._forward = True

        def reverse(self):
            """Change direction of the list"""
            self._forward = not self._forward

    def append(self, node):
        """Add a Node to the end of the list (i.e. where self._tail is)"""
        if not self._forward:
            self.prepend(node)

        node._attach(parent=self,
                    next_node = None,
                    prev_node = self._tail)

        if self._tail:
          self._tail._next = node

        self._tail = node

        if self._head is None:
          self._head = node

    def prepend(self, node):
        """Add a Node to the startof the list (i.e. where self._head is)"""
        if not self._forward:
            self.append(node)

        node._attach(parent=self,
                    next_node = self._head,
                    prev_node = None)

        if self._head:
          self._head._prev = node

        self._head = node

        if self._tail is None:
          self._tail = node

    def insert_after(self, node, new_node):
        """Insert a node after another node"""
        if new_node is None:
            self.prepend(new_node)
        elif new_node is self._tail:
            self.append(new_node)
        else:
            new_node._attach( parent = self,
                next_node = node._next,
                prev_node = node)
            node._next = new_node
            new_node._next._prev = new_node
