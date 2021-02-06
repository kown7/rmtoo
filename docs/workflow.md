---
title: slToo Workflow
---

# Introduction

A solution is presented to collaboratively work and track requirements is 
presented.

# Motivation

Collaborate on requirements documents with various stakeholders and ensure 
transparency on sources for requirements.

Ensure requirements everything can be edited in an Excel file.

Use freely available open-source tools to replace expensive tools, e.g., Doors.

## Technical Requirements

* Keep the specifications documents and code synchronised
  * Single source of truth
* Automate the generation of documents
  * Always up-to-date documents
  * Document baselining
  

# Workflow

It is assumed that the owner the requirements specification has an initial 
proposal. The generated *xls* and *pdf* documents will be distributed to all 
stakeholders. 

{% include image.html url="assets/images/Workflow-init.png" description="Initial Distribution of Requirements Specifications" %}

Their feedback will be
imported and reviewed. When all feedback has been imported, the various
changes can be merged (`git merge`). If there are merge conflicts or review 
issues, they need to be solved separately.

{% include image.html url="assets/images/Workflow-feedback.png" description="Incorporating Stakeholder Feedback" %}

Generate a new set of documents (new baseline) for review. Repeat this 
process until the project is finished.


# Technical Workflow

The generated documents can then be used to produce a product that satisfies
this requirements. For now, [see here](https://kown7.github.io/pymergevcd/reqdevsecops.html#proposition).


