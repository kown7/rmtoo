---
title: Famous Why Interview
---

QUESTION 1 
Rmtoo comes without a graphical interface and in exchange, it uses a
command line tool optimized for handling requirements. Why this
decision?

rmtoo is based on the long history of *nix commands: Let one thing do
one thing.  In the *nix environment there are lots and lots small
commands - each doing one thing - but perfectly, quickly and
applicable in many different applications and environments.

rmtoo handles requirements - nothing more - nothing less.  It does not
deal with things like version control, history handling, branching or
baselining.  There are other good tools around which do this (such as
svn, mercurial or git): so there is no need to reinvent the wheel.

The exact same argument applies to the GUI: there are lots of good
editing applications which are able to edit requirements.  There are
also lots of good programs for converting text files into graphs or
PDFs.

Selecting which program to use must be the choice of the user - not of
the requirements management tool.

At the moment, rmtoo interfaces with nearly a dozen other
applications: emacs, Open Office, graphviz, LaTeX, make, Ganttproject,
... and there are more to come.

One additional reason for this decision is that rmtoo is used in
continuous build environments - where the requirements and all the
requirements artifacts are stored in the same place as the source code
and the artifacts are automatically generated.  In this scenario, a
command line tool is mandatory - there is no way to handle it with a
GUI.

-----

QUESTION 2
Rmtoo is a powerful management tool. How can Rmtoo help a developer
handle its projects? 
 
The central idea behind rmtoo is that all requirements depend on other
requirements. Therefore rmtoo forces a developer to work in a
structured way.  When a developer solves a problem he splits up one
requirement into many 'steps' or 'solutions'.  When viewing this on
the next, higher level of abstraction, it's quite clear that these
'steps' or 'solutions' are also requirements.

A developer therefore turns the requirements he gets (e.g. from the
marketing department) into more and more requirements - until they are
'bite-sized' chunks that can be directly implemented.  Therefore rmtoo
forces the developer to think before he implements anything.

It has been proven useful for the developer to have the requirements
and the sources side-by-side - generally in a single version control
system.

-----

QUESTION 3
Can you tell us more about Rmtoo supported formats?

There is only one input format: text files.  This can be seen as the
database rmtoo operates on.

With rmtoo it is possible to either output (almost) everything in one
document or have only certain aspects of the requirements displayed.
The basis for document style output are 'Topics'.  These are a
meta-output descriptions of the document.  They make it possible to
have exactly the same content in, for example, a PDF document or HTML
pages.  It is also possible to define other topics which only include
specific themes.  It is therefore very easy to print out a
requirements document for a vendor which only delivers a small part of
your project - without the need to send him the whole document, which
may include confidential information.

Currently supported output formats are: 
* LaTeX document files with support for PDF creation including links to
  dependent requirements.
* Backlog files which can be used in SCRUM - also in LaTeX format.
* graphviz files which can be rendered in a graphic format like png,
  jpg. 
* HTML files including links to dependent requirements.
* XML files for interfacing with many other applications.
* GanttProject files: each requirement gets one line, dependencies and
  topics are used for project dependencies.
* Current requirement version as simple txt file.
* Pricing sheet in Open Office format.

AND: rmtoo is easily extensible.  Writing a small, new output module
can be done within hours - even complicated ones can be created in a
couple of days.
 
-----

QUESTION 4
Rmtoo received several important awards and it becomes more and more
popular with every day that passes. Are you happy with this success?
How do you image Rmtoo future? 

To date, rmtoo has been downloaded about 2500 times from the sites we
control.  There is also quite a high percentage of responses from the
community.  As far as I know, rmtoo is currently used in projects
in different technologies all over the world.

Of course it's nice when others like the ideas which have been
incorporated into rmtoo.  It seems that a niche in requirements
management tools has been found and that the rmtoo approach is needed
and rmtoo is useful.

The future of rmtoo heavily depends on the community and on
customers.  Their feedback directly influences the roadmap.  All
features which are currently available are actually used.

The next few releases will concentrate on documentation and testing.
At the moment there is a lot of documentation - but some small parts
are still missing.  Also, the current test suite 'only' covers about
92% of the code.  After finishing these things rmtoo might be placed
on some well known requirements management tool lists.

Also, there are a lot of requests for new features - so there are
enough things waiting on the road map for at least 10 releases. 

-----

QUESTION 5
Beside Rmtoo, is there any other project you are currently working on?
If yes, can you give us a few details about that project? 

Of course - I can give you some details.  

One project is to build a 'low power' office server.  The server is
designed so that it will not consume more than 30W power.  The server
will be the 'backend' server for a small office, handling things like:
high availability backup and file server using RAID6, Wlan access
point, SIP phone system (for Wlan and cable SIP phones).  Last but not
least it must be affordable - so only standard components are used.
It is not yet clear if this will be turned into a 'product'.  More
details can be found on the company's blog at
http://outer-rim.gnu4u.org - when looking for the server project,
there is a category 'SOHO'.

There are some more projects to come - but it is too early to talk
about them.

----

Published at '' (TBD).
