---
title: slToo Workflow
---

# Introduction

A solution is presented to collaboratively work on and track requirements.
Furthermore ensure the traceability over all specification items.

# Motivation

On an embedded project some years ago that we inherited from previous
collaborators, there was at least an Excel sheet with various requirements
listed. The origins of this file was shrouded in mystery, but probably
from some web-based ALM tool that definitely didn't ship with the code.

All changes made by the various stakeholders were in different files.
Merging those changes were tedious manual work with no clear traceability of who
proposed which changes and no automated way to ensure there were no conflicting
changes. [Here a workflow is proposed that ensures clear authorship, fails to
merge conflicting changes and creates PDF documents on top.](#collaborative-workflow).


On a different project some full moons ago there was a test report in a *Word*
document. This test report listed all requirements and how they were verified,
i.e. testing or analysis. For every entry there was a link to the report
documenting the relevant tests/analysis. This became tedious to keep updated and
correct with every changed test or requirement. [Here an automated solution is
presented](#traceability).



# Collaborative Workflow

It is assumed that the owner of the requirements specification has an initial
proposal. The generated *xls* and *pdf* documents will be distributed to all
stakeholders.

{% include image.html url="assets/images/Workflow-init.png" description="Initial Distribution of Requirements Specifications" %}

The stakeholders can edit the spreadsheets they've received to their liking
without any side-effects. Their feedback will then be imported and reviewed.
When all feedback has been imported, the various changes can be merged.

As all specification items are stored as plain text files, they can be merged
with your favourite version-control system, i.e. `git merge`. If there are
merge conflicts or review issues, they need to be solved separately.

{% include image.html url="assets/images/Workflow-feedback.png" description="Incorporating Stakeholder Feedback" %}

Generate a new set of documents (new baseline) for review. Repeat this
process until the project is finished.


## Requirements

Every requirement specification issue is stored in its own file. The following
example is called `SW-AS-501.req`. This allows us to track changes with a
*version control system*, i.e. `git`.

In the following image a reference specification item is shown.

{% include image.html url="assets/images/requirement-ex.png" description="Sample specification item" %}

The item's identifier is given next to the title. The hash calculated over the
title, description and identifier.

## Editing Requirements

The specification can be edited using any compatible spreadsheet program. It
will be along the lines of the following image.

New items can easily be created by copying the existing rows.

{% include image.html url="assets/images/excel-ex.png" description="Editing the specification items" %}


# Traceability

Ensure that verification and validation (V&V) activities are invalidated
when requirements change, i.e. requirements traceability[^1]:

    Requirements traceability is the ability to follow and audit the life of a
    requirement, in both a forward and backward direction; from its origins,
    through its realization in the design and functional specifications, to its
    eventual development and deployment and use, through subsequent rounds of
    modification and refinement.

## Traceability to Tests

The previous specification item `SW-AS-501` is referenced the
unit-tests[^3]. The following code snippet shows the test code and the
reference.

```python
def test_read_write_engines(record_property, dummy_vcd_file):
    """Write-back from read file, equal output"""
    record_property('req', 'SW-AS-501-f8d68d11')
    record_property('req', 'SW-AS-500-4c1a395a')
    ofile = 'test_writeback.vcd'
    reader = pymergevcd.vcd_reader.factory(dummy_vcd_file)
    writer = pymergevcd.vcd_writer.factory(ofile)

    writer.process_source(reader)
    assert filecmp.cmp(dummy_vcd_file, ofile)
```

The previously defined `record_property` creates the following lines in the
xunit XML results file `result.xml`.

```xml
<testcase classname="tests.test_io_manager" file="tests/test_io_manager.py" line="20" name="test_read_write_engines" time="2.830">
  <properties>
    <property name="req" value="SW-AS-501-f8d68d11"/>
    <property name="req" value="SW-AS-500-4c1a395a"/>
  </properties>
</testcase>
```

The `result.xml` file is then used to derive the traceability matrix.

{% include image.html url="assets/images/tracemat-ex.png" description="Sample traceability matrix" %}

Should this specific specification item change so will the traceability matrix
show a failed instead of passed. This due to the different hashes.


# Example Document

The previous examples were copied from the *architecture specification*[^2] for
[*pymergevcd*](https://kown7.github.io/pymergevcd/).


# Further goals

* Keep the specifications documents and code synchronised
  * Single source of truth
* Automate the generation of documents
  * Always up-to-date documents
  * Document baselining
* Edit requirements with Excel.
* Integrate with your CI/CD pipeline
* Still there in 10 years.

## Alternatives

This is an incomplete list of existing ALM tools that will solve your problems
with a different UI.

* [Octane ALM](https://www.microfocus.com/en-us/products/alm-octane/overview)
* [Codebeamer](https://codebeamer.com)
* [Aligned elements](https://www.aligned.ch/)
* ...

They're gone in 10 years though.

----

[^1]: [Chris Adams](https://www.modernanalyst.com/Careers/InterviewQuestions/tabid/128/ID/510/Why-is-requirements-traceability-important.aspx)  
[^2]: [Architecture Specification for *pymergevcd*](https://kown7.github.io/pymergevcd/assets/arch/artifacts/specification.pdf)  
[^3]: Please don't do this  

