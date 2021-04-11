---
title: README
note: All readme files have no header, otherwise they're in the top bar
---


# Overview

rmtoo is a free and open source requirements management tool.

rmtoo uses a different approach than most other requirements
management tools: it comes as a command line tool which is optimized
for handling requirements. The power of rmtoo lies in the fact that
the development environment can handle the input and output files -
there is no need for a special tool set environment.

Example: if you need to handle baselines (and there often is), rmtoo
can be configured using a revision control system (e.g. git). The
revision control system can handle different revisions, baselining,
tagging, branching and many other things extremely well - there is no
reason to reinvent the wheel and making it less efficient.

Let one thing do one thing.


## Read-Me

The following `README` are available from the original repository

* [Readme-GitPython](readme/Readme-GitPython)
* [Readme-Hacking](readme/Readme-Hacking)
* [Readme-OS-X](readme/Readme-OS-X)
* [Readme-RmtooOnRmtoo](readme/Readme-RmtooOnRmtoo)
* [Readme-Windows](readme/Readme-Windows)

There's also the original *rmtoo* [Roadmap](readme/roadmap). See also
[the plans for 2021]({{ site.baseurl }}{% link _posts/2021-04-11-near-term-roadmap.md %}).


# Unique Feature Set

rmtoo fits perfectly in a development environment using text editors
and command line tools such as emacs, vi, eclipse, make, maven. 

* Use simple text files as input - use your favorite editor
* Many different output formats and artifacts are supported:
  * PDF - with links to dependent requirements
  * HTML - also with links to dependent requirements
  * Requirements dependency graph
  * Requirement count history graph
  * Lists of unfinished requirements including priority and effort
    estimation - e.g. for use in agile project development 
* Fully integrated revision control system: git. Usages: history,
  statistics and baseline handling. 
* A topic based output handling provides a common set of files for
  different types of output (PDF, HTML, ...) 
* Complete support for automatic checking of constraints.
* Analytics modules: Heuristics help to evaluate the quality of
  requirements 
* Modules to support commercial biddings based on a given set of
  requirements 
* Emacs mode files for editing requirements and topics included
* Experimental output in XML
* Fully integrated with Makefile handling of all artifacts
* Fully modular design: additional output requires minimal effort
* During parsing most common problems are detected: all syntax errors
  and also many semantic errors. 
* Fully automated test environment - tests about 95% of the code and
  is shipped with rmtoo packages to check for possible problems in
  different environments. 

rmtoo is not a fully integrated, tries-to-do-everything tool with a
colorful GUI or different database backends. 


## Man Pages

The man pages have been converted to HTML files for the reader's convenience.

[rmtoo-analytics-descwords.7.html](man/rmtoo-analytics-descwords.7.html)\
[rmtoo-analytics-hotspot.7.html](man/rmtoo-analytics-hotspot.7.html)\
[rmtoo-analytics-req-topic-coherence.7.html](man/rmtoo-analytics-req-topic-coherence.7.html)\
[rmtoo-analytics-topic-coherence.7.html](man/rmtoo-analytics-topic-coherence.7.html)\
[rmtoo-analytics.7.html](man/rmtoo-analytics.7.html)\
[rmtoo-art-html.1.html](man/rmtoo-art-html.1.html)\
[rmtoo-art-latex2.1.html](man/rmtoo-art-latex2.1.html)\
[rmtoo-art-oopricing.1.html](man/rmtoo-art-oopricing.1.html)\
[rmtoo-art-prio-lists.1.html](man/rmtoo-art-prio-lists.1.html)\
[rmtoo-art-req-dep-graph.1.html](man/rmtoo-art-req-dep-graph.1.html)\
[rmtoo-art-req-dep-graph2.1.html](man/rmtoo-art-req-dep-graph2.1.html)\
[rmtoo-art-reqs-history-cnt.1.html](man/rmtoo-art-reqs-history-cnt.1.html)\
[rmtoo-art-stats-burndown1.1.html](man/rmtoo-art-stats-burndown1.1.html)\
[rmtoo-art-stats-sprint-burndown1.1.html](man/rmtoo-art-stats-sprint-burndown1.1.html)\
[rmtoo-art-tlp1.1.html](man/rmtoo-art-tlp1.1.html)\
[rmtoo-art-version1.1.html](man/rmtoo-art-version1.1.html)\
[rmtoo-art-xml-ganttproject2.1.html](man/rmtoo-art-xml-ganttproject2.1.html)\
[rmtoo-art-xml1.1.html](man/rmtoo-art-xml1.1.html)\
[rmtoo-config1.5.html](man/rmtoo-config1.5.html)\
[rmtoo-config2.5.html](man/rmtoo-config2.5.html)\
[rmtoo-config3.5.html](man/rmtoo-config3.5.html)\
[rmtoo-config4.5.html](man/rmtoo-config4.5.html)\
[rmtoo-configuration-convert.1.html](man/rmtoo-configuration-convert.1.html)\
[rmtoo-constraints.5.html](man/rmtoo-constraints.5.html)\
[rmtoo-emacs-mode-req.7.html](man/rmtoo-emacs-mode-req.7.html)\
[rmtoo-invoking.1.html](man/rmtoo-invoking.1.html)\
[rmtoo-normalize-dependencies.1.html](man/rmtoo-normalize-dependencies.1.html)\
[rmtoo-pricing-graph.1.html](man/rmtoo-pricing-graph.1.html)\
[rmtoo-req-format.5.html](man/rmtoo-req-format.5.html)\
[rmtoo-template-project.1.html](man/rmtoo-template-project.1.html)\
[rmtoo-testcase-format.5.html](man/rmtoo-testcase-format.5.html)\
[rmtoo-topic-format.5.html](man/rmtoo-topic-format.5.html)\
[rmtoo.7.html](man/rmtoo.7.html)
