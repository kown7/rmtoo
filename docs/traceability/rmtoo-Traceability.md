---
title: "sltoo -- Traceability"
author: Kristoffer Nordström
date: \today
header-includes: |
  \usepackage{hyperref}
  \usepackage{appendixnumberbeamer}
  \usetheme[block=fill,progressbar=frametitle]{metropolis}
  %\setbeameroption{show notes}
---

# Introduction

## Storytime

* The Foundling
* Word is also a Hammer
* The Spanish Review
* The Blame Game

## The Foundling

Once upon a time a we inherited from another contractor a project that has
been dormant for a couple of years.

It came with one document that contained all requirements and use-cases. It
appeared to have been exported from some web-based tool.

**Question:** How do we ensure that all requirements and documentation is
shipped with the code for future use?

## Word is also a Hammer

A different project had one test report with a traceability matrix. It's
perfectly fine to create one manually. If the requirements change it'll be
hard to figure out the minimal delta-test.

Obviously the requirements change more than once. Hence we want this fully
automated.

## The Spanish Review

I've once had the pleasure to review multiple specifications for an ESA
contractor. Unfortunately, they didn't provide a consistent set of documents.

We have CI/CD for software, why don't we include our documents?

## The Blame Game

We can branch software files and have tools to review merges/changes.

Software is just text, requirement specifications too. Can we use the same
tools, e.g., running `git blame` on the spec?


# Theory

## Non-locality of comments

Perhaps the biggest problem with code comments are their non-locality

::: {.block}
### Dragons
```python
# Here be dragons, don't forget to clean up later
some_func()
...
cleanup()
```
:::

Changes to `some_func()` will not propagate back to the above snippet, let alone the clean-up.


## Non-locality of comments (II)

```java
// Always returns true.
public boolean isAvailable() {
    return false;
}
```


## Traceability Directions

* Traceability from specification items
    * Forward from requirements specification to dependant documents
	* Backwards from verification to specifications

![Traceability Overview](vmodell-fwdrwd.png)


## Traceability

* *Requirement A* says do `A`
* *Implementation a* says implemented `A`
    * What if `A` changes?
	* *A* knows nothing of *a*
	* Can be tedious manually


## Proposed Solution

* *Requirement A-1.0* says do `A`
* *Implementation a* says implemented `A-1.0`
    * *A-1.0* changes to *A-2.0* do `Â`
	* Use hashes instead of semantic versioning
	* Calculated automatically


# Practice

## Baseline

* Based on [rmtoo](https://github.com/florath/rmtoo)
    * File-based requirements tracking tool
    * Requirements stored in text-files
    * group requirements by topics
    * document and requirements \LaTeX based
	   * Customizable with templates
* Manage with your favourite VCS
	* Merge changes from various sources
* Excel import/export
* Traceability


## Example Requirement


::: columns

:::: column
\tiny
```
Name: VCD Writer Inputs
Topic: ReqsDocument
Description: The output from ...
Rationale: Make the process as ...
Status: external
Owner: development
Effort estimation: 1
Invented on: 2020-05-30
Invented by: default
Type: requirement
```
::::

:::: column
![Example Requirement](../assets/images/requirement-ex.png)
::::

:::

\vspace{1em}
*Hash* is calculated over *Name*, *Description* and *Verification Method*

## Testing the Example Requirement

* Requirement ID: `SW-AS-501`
* Hash: `F8D68D11`
* Status: *external*

::: {.block}
### Test Code
\tiny
```python
def test_read_write_engines(record_property, dummy_vcd_file):
    """Write-back from read file, equal output"""
    record_property('req', 'SW-AS-501-f8d68d11')
    record_property('req', 'SW-AS-500-4c1a395a')
    ...
    assert filecmp.cmp(dummy_vcd_file, ofile)
```
:::


::: {.block}
### xUnit Output
\tiny
```xml
<testcase classname="tests.test_io_manager" file="tests/test_io_manager.py" line="20" name="test_read_write_engines" time="2.830">
  <properties>
    <property name="req" value="SW-AS-501-f8d68d11"/>
    <property name="req" value="SW-AS-500-4c1a395a"/>
  </properties>
</testcase>
```
:::


## Traceability Matrix

![](../assets/images/tracemat-ex.png)

## CI/CD

* Integration for every output document
* Match *open* and/or *failed* issues
* Example for *failed* issues
```bash
bash -ec 'test "$(grep -c failed \
   arch/artifacts/tracematrix.tex)" -eq "0"'
```

## Versioning

* Every document has a release process

```bash
git tag -a RS/1A
git describe $(git log -n 1 --format=%H -- docs/reqs)
```

Output good and tainted:

```bash
$ RS/1A — 0aec3ad0
$ RS/1A-8-g76b3ffe — 76b3ffe4
```

# Conclusion

## Storytime Revisited

* Requirements shipped with code \checkmark
* Traceability matrix automated \checkmark
* Continuously updated documentation \checkmark
    * Document Versioning \checkmark
* `git blame` and `gitk`? \checkmark

\note{Your Jira workspace will be gone}

# Questions?

\appendix
## Excel Support Rationale


::: columns

:::: column
* Good-enough GUI
* Understood by everyone
* The *Truth* is still in your repository
  * Import from Excel to repository
  * Export every build to a new Excel file
  * Templating for branding
::::

:::: column
![Workflow](../assets/images/Workflow-feedback.png){ height=75% }
::::

:::



## *rmtoo*

Introduction Presentations

An
\href{https://github.com/florath/rmtoo/releases/download/v23/rmtooIntroductionV9.pdf}{introduction
presentation} into *rmtoo*  and with more
\href{https://github.com/florath/rmtoo/releases/download/v23/rmtooDetailsV5.pdf}{details}.


## Traceability Rationale

* Traceability for the given requirements
* Bring code and documentation into same repository
* Integrate into build-system
  * Detect upstream changes to requirements
  * Quickly identify affected code-regions
* No silver bullet for verification


## Results

The status *external* will yield the following results:

* *open*
    * No matching requirement ID
* *passed*
    * Matching requirement ID
	* All hashes match
	* Unit-tests passed
* *failed*
    * Matching requirement ID
	* Some/all hashes didn't match, or
	* Unit-tests haven't passed



## Specification Hash

* SHA256 hash calculated over sum of
    * Description,
	* Titel, and
	* Verification Method (if available)
* Rationale is only informative

## Installation

Traceability features are in the beta releases.

```bash
pip3 install sltoo>=25.1.0b3
wget https://kown7.github.io/pymergevcd/assets/template_project.zip
```

## Future Developements

* Write Parser for *Test Reports*
    * Documents with the correct identifier automatically solve the specification
	* Document Formats:
	    * docx (maybe with pandoc)
		* \LaTeX
* Cross-Document References
    * *Solved by external*
	    * *Solved by* is used in *downwards* direction in the V.
	    * Only within document at the moment. Makes merging documents easier.
    * *Depends on external*
	    * References requirements in other documents, can be with or without hashes.
		* Think about extending the current *Depends on* handler (deprecated) for use as external (leftwards, upwards) reference.

## Final Thoughts

* Never test against your requirements
* Always write some form of test specification










