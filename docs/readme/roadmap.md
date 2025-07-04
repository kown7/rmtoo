---
title: Roadmap
no_header: true
---

This is a description of the next and next-next generation of to be
implemented features.

There is no exact time line because the amount of time spend for this
tools changes from time to time (depending on many factors).

Also the version number shown here might change: if there are other
requests from customers those will be done first.  Also it might be
that from time to time there is a bug-fix release of rmtoo.

The history of this file, i. e. the already implemented features can
be found the appropriate release notes.

v24
===
* Create ready to use VM for AWS EC2.
* Include requirements of rmtoo and EMailClient into python package.
* Fix: Emacs highlighting on GUI VM

IMPORTANT
=========
* Design GUI
  - Server
  - Clients
  - Protocoll / Interface
* Add requirements from Roadmap.
* Rethink about the modules: they should also run (at least partially)
  for the topic based output.  Is there a way to unify this?

OTHER / LATER
=============
o Think about GUI
* Add support for Tasks / Issues
  ( -> import from Bugzilla? )
* If possible:
  Add GUI for creating and modifying a configuration.
* Check Web-Site for user features / bugs
  - Fix (small) bugs
  - Add feature request requirements
* Man page: (???)
  + graph
  + graph2
  + EfEU
* Add to FAQ: max level of topic inclusion.
* Add changes to presentation
* More testcases
* Archive old versions from slashdot to flonatel.de
  (leave only last three versions on slashdot)
* Add tasks to rmtoo
  (Maybe import possibility from Bugzilla.)
* Draw overview picture for current Sprint (a la 'Paper' overview with
  'Chosen', 'In Progress' and 'Finished'.
* Now that the finished date and duration is available, gantt output
  should be extended to use this.
* SCRUM Burndown diagram
* Due Date for all requirements as optional
* Requirement: prosponed, withdrawn as additional state of a requirement
* For later 'gantt' export:
  start-date, end-date, ...
* Design issue: (from WEB)
  If the intent of the original heuristic was to discover disconnected
  (i.e. floating) topics, the checks should definitely be adjusted to
  also count sub-topics and parent topics, as parent-child connections
  are of course valid connections, too.
* Build a server which can serve as the interface to different GUIs
  (e.g. native gtk, WEB, ...)
  - Build gtk GUI
  - Build WEB GUI
* Include sub-graphs in the PDF and HTML documentation
  - Topic based (all reqs of a topic)
  - req based (all reqs dependend and depend on one req)
  - Try to implement this is a generic way that makes it
    possible to include dot files from within a requirement.
    (If this is not possible, add this to the OTHER / LATER
    features.)
  * Adapt man pages
  * Adapt presentation
* It often happens that one requirement is resolved into two different
  'types' of solutions:
  1) The genral properties of all 'direct' solutions
  2) The direkt solutions.
  There is currently no way to differ between those two different
  'types' of requirements. It should be elaborated if these are really
  two 'types' or if this can be described with the current implemented
  features. 
* Long Term Evolution: It's all about data storage and who (which
  program) can access (read, write, change, ...) which data.
  - Write requirements
  - Discuss with other projects (ganttproject, freemind, ...)
  - Storage vs. Bus-System
  - Verfügbarkeit
  - Ausfallsicherheit
  - Colaboration
  - Concurrency
* Add makefile dependencies: .rmtoo_dependencies depends
  on the ConfigX.py file.
* output level in 'prios.py' must be configurable
* traceability of changes
  - Dependent on changes: list all depended requirements which must
    be checked.
* Add change marks for at last latex output:
  - specify one additional version number from which the difference is
    made
  - Mark
    + Additions
    + Changes
    + Deletions
    (Should be not that hard when creating the difference based on the
    requirements - but also the topics must be included)
* Translations / Intenationalization
  - Input: possible define a new set of tags - one for each language.
* Topic includereqs: There is the need to at least specify ONE
  requirement which is located before all others.
* Add version number to rmtoo -v or something
* Add roadmap feature
* Add ToDo list feature
* History in document: specify two versions and create automatically a
  list of all changed requirements.
* Clean up code (XXX, ToDo, ...)
* Use MemLog instead of print.
* 'The only requirement management tool which comes with the
  requirements for the tool'. 
* A requirement cannot be 'finished' if on of the dependent is not
  finished. 
* Add glossary
* Add man page for glossary
* Add glossary to presentation
* Emacs mode for editing topic (tic) files.
* Better list of preconditions
  (When is what needed? Version?)



Long Term Evolution or This will be another project
============================

Interaction between programs
----------------------------
The *nix base idea is: let one thing do one thing (but this very
well).  Examples: mostly all commands in /bin and /usr/bin.  They
all work on plain text files and every program has exactly one
functionality. 

When looking to mostly all other areas of data processing, the
interaction of different programs is very, very limited - which
depends on the file format.  Complex programs (like office word
processor) work on complex data.  Mostly each program has it's own
file format.  The file format is mostly not interchangeable with other
programs - and if so, it's mostly hard to convert and often some
aspects are lost during conversion.

Another aspect is, that mostly all programs work on the input data in
a way that they think they 'own' the data. When programs cannot deal
with data, they tend to either complain about corrupted input files or
they ignore the unknown parts in the way that when saving the read-in
data in a program those unknown parts are not contained any more.
Others just rename internally used labels and attributes in a way that
it is impossible to find the original elements after one of those
programs worked on them. Example: OpenOffice Calc.

