---
title: "How To: About Digraphs"
date: 2010-12-09
author: Andreas Florath <rmtoo@florath.net>
---

Status
------

(as of version 15)

rmtoo uses digraph data structure for internal data handling.  The
most obviously used digraph data structures are the requirements
dependencies and the topics.

A set of requirements is represented as one digraph.  The requirements
themselves are the nodes.  The edges are created based on the 'Depends
On' field. 

The topic description is represented by another digraph.  Each topic
is a node.  The edges are created based on the 'SubTopic' field.


Discussion
----------

Both digraphs are build based on different ideas:

The requirements digraph is build upon the fact that a node knows all
incoming edges.  The topic digraph is build based on the fact, that a
node knows all outgoing edges.

There is no reason why this is done this way for the requirements -
except the historic one: it always was done in this way.

But there is a reason why the topic digraph is build in the way it is:
Topics might be reused from different topic sets.  A topic can be seen
as a chapter which can be included into different books.  The
description of the book includes a list which chapters to use.  The
chapter itself should not know all the books where it is included.

After realizing this confusing setup, there is only a small step to
ask, why the requirements are organized in the way they are.  In my
opinion the topic solution is much cleaner and the requirements should
be implemented in this way.

It's getting more complicated: one person in the rmtoo forum asks to
change the topic way of describing dependencies.


Pros and Cons
-------------

A list of pros and cons is therefore needed about possible solutions: 

## Outgoing Only

(The way topics are currently implemented.)
* ++Goto (instead of come-from) thinking
* +No need to change a solution when it is used in another context
* +Typical way of thinking (at least for me)
* +Problem and Solution in one file 
* +Give the customer what he needs


## Incoming Only

(The way requirements are currently implemented.)
? 


## Incoming and Outgoing Mixed

* +Different projects can use different ways of description
   dependencies 
* -Not consistent: a member of one team may be confused
   working on requirements from another team.
* -Give the customer what he wants


## Sepatate Data Structure for edges

(Idea: Have a description for edges - separated from the nodes.) 
* ++Relations can be changed without changing the content (nodes).
* -Need for additional files / descriptions


Solution
--------

Currently no solution concept is available.

-> Request for comments! <-

-> Request for discussion <-

