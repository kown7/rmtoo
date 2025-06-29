---
title: FAQ
---

# Getting Started with rmtoo

* What is the input file format?

  The file should be plain text. The file should contain a sequence
  of details.  Each detail is a group of lines, in name: value
  pairs. For multiline values, indent by one space on the lines
  after the first. It's possible to leave a blank line between
  requirements, for readability.
  Please consult the rmtoo-req-format(5) man page for further
  information.

* What tags are supported?

  Currently the following tags are supported:
    * Class
    * Solved by
    * Description
    * Effort estimation
    * Invented by
    * Invented on
    * Name
    * Owner
    * Priority
    * Rationale
    * Status
    * Type

   For a detailes discussion about the semantic see the
   rmtoo-req-format(5) man page.

* Can I split a large set of requirements into a set of separate files?

  You must - each requirment must go in one file.

* Does a requirement have a unique id?

  Yes - each requirement has an id which is the case sensitive name
  of the file where it's described in - without the suffix.
  Example: file name 'OutputPrio.req' -> id 'OutputPrio'

* Are there any guidelines for the use of 'Id'?

  Just write a unique phrase, the shorter the better.  You can also
  use numbers if you want.
  It's typically easier to handle the requirements when the 'Id'
  gives a hint about the content.

* How do I specify dependencies?

  Give only one *Solved by* field per requirement.
  The value should be the 'Id's of the requirement which solves you
  current requirement.
  You must specify a *Solved by* - except for all leaves (requirements
  which cannot / should not detailed any more).

* How do I put paragraphs in the Rationale?

  To start a new paragraph, write \par at end of the current
  paragraph. (This will automatically converted to the appropriate
  output format.)

* Are there any guidlines for the use of Effort estimation?

  The effort estimation is meant to be a symbolic effort point number
  as used in SCRUM.  Please consult the rmtoo-req-format(5) man page
  for detailed information.

* What units are expected in the Effort estimation field?

  None - this is a symbolic number.  See rmtoo-req-format(5) man
  page.

* What values are valid for the Status field?

  Supported values for the 'Status' field are 'not done' and
  'finished'.  See rmtoo-req-format(5) man page.

* What values are valid for the Type field?

  Supported values are 'master requirement', 'requirement' and
  'design decision'.  Please consult the rmtoo-req-format(5) man page
  for details.

* What does 'Class' do? How should it be used?

  Class can be one of 'implementable' or 'detailable'.  If a
  requirement is at a detail level that it can be implemented, the
  Class should be set to 'implementable'.  In the other case (the
  default) the requirement must be elaborated and some dependent
  requirements must be defined. Please consult the
  rmtoo-req-format(5) man page for details.

* How should I remove a requirement?

  Remove it from the file system (with rm), then remove it from the
  vcs (with 'git rm') then do a checkin.

# Every day usage

* Is is possible to rename the rmtoo directory?

  No - this is not possible.  Mostly all python files assume that the
  top level directory is called 'rmtoo'.

* rmtoo prints `make: *** No rule to make target ...`

  This typically happes when an requirement was removed or
  renamed. In this case the automatically generated dependency file
  must be deleted (typically with `rm .rmtoo_dependencies`) or a
  `make force` will do this for you.

* I cannot compile rmtoo.  What should I do?

  There is no need to compile rmtoo.  It comes as a set of modules.
  You can unpack and just use it.

* I got the error `ImportError: No module named rmtoo.lib.RmtooMain`

  This is a hint, that the PYTHONPATH is not set correctly when using
  the tar packaged version of rmtoo.

* `make test` displays a low test coverage

  The reason for this is currently unknown.
  After removing all (old) .pyc files
      `find . -name "*.pyc" | xargs rm`
  the coverage is correctly computed.

* The requirement looks fine but rmtoo complains about a missing tag

  If you are using some strange line delimiters (such as carriage
  return and linefeed - as used by MSDos), rmtoo cannot parse the
  requirements.  Please convert it to the commonly used file format
  just using line feeds (LF, 0x0A).
