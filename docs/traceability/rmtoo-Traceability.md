---
title: "sltoo -- Integrating Requirements into CI/CD"
author: Kristoffer Nordström
date: \today
institute: \texttt{\url{info@sltoo.dev}}
header-includes: |
  \usepackage{hyperref}
  \usepackage{appendixnumberbeamer}
  \usetheme[block=fill,progressbar=frametitle]{metropolis}
  %\setbeameroption{show notes}
  \usepackage[
    type={CC},
    modifier={by-nc-sa},
    version={3.0},
  ]{doclicense}
---

# Motivation

\note{It's an honour to open this topic's session.

When talking about requirements, we should also define the requirements
of the problem we're trying to solve. For all requirements there's a anecdote.}


## Storytime

* Word is also a Hammer
    * Fully automated traceability matrix
* The Hopeless Review
    * Consistent documents straight from the source
* The Foundling
    * Store requirements' meta-information with code

\note{
4'

It's perfectly fine to create one manually. If the requirements change
it'll be hard to figure out the minimal delta-test. Obviously the requirements
change more than once. Hence we want this fully automated.


I've once had the pleasure to review multiple specifications for a different
contractor. Unfortunately, they didn't provide a consistent set of documents.

To use the term Jon Holt uses in his introduction to MBSE:
Documents need to be a live *view* of the system to be built (not pretty
pictures). We have CI/CD for software, why don't we include our documents?

It came with one document that contained all requirements and use-cases. It
appeared to have been exported from some web-based tool.

Propose and implement a solution to these problems.
Also: Too technical, need an interface with management/business side}


# Theory


## Requirements and Traceability

* Requirements across system hierarchies
    * Implies the need for traceability
* *Traceability* from and to specification items
* Directions
    * Forward (*Impact*) from requirements specification to dependant documents
    * Backwards from verification artefacts to specification

\vspace{15px}

![](vmodell-fwdrwd.png)


\note{Here Traceability only from items/issues}


## Traceability

* *Requirement A* says do `A`
* *Implementation a* says implemented `A`
	* Can be automated
* What if `A` changes?
	* *A* knows nothing of *a*

\begin{tikzpicture}[remember picture,overlay]
    \filldraw[fill=red!30!white, draw=red,thick] (9.2,-0.9) circle (1.5cm);
    \filldraw[fill=red!80!white, draw=red,thick] (9,-0.7) circle (1.5cm) node[align=center, text=white] {\textbf{PANIC}} ;
\end{tikzpicture}


## Traceability

* *Requirement A* says do `A`
* *Implementation a* says implemented `A`
	* Can be automated
* What if `A` changes?
	* *A* knows nothing of *a*


\begin{tikzpicture}[remember picture,overlay]
    \filldraw[fill=teal!20!green!30!white, draw=teal!20!green,thick] ([xshift=4.2cm,yshift=-2.5cm]current page.center) circle (1.5cm);
    \filldraw[fill=teal!20!green!80!white, draw=teal!20!green,thick] ([xshift=4cm,yshift=-2.3cm]current page.center) circle (1.5cm) node[align=center, text=white, text width=2.5cm] {\textbf{DON'T PANIC}};
\end{tikzpicture}




## Proposed Solution

* *Requirement A-1.0* says do `A`
* *Implementation a* says implemented `A-1.0`
    * *A-1.0* changes to *A-2.0* do `Â`
	* Use hashes instead of semantic versioning
	* Calculated automatically


\begin{tikzpicture}[remember picture,overlay]
    \filldraw[fill=teal!20!green!30!white, draw=teal!20!green,thick] (9.2,-0.9) circle (1.5cm);
    \filldraw[fill=teal!20!green!80!white, draw=teal!20!green,thick] (9,-0.7) circle (1.5cm) node[align=center, text=white, text width=2.5cm] {\textbf{DON'T PANIC}} ;
\end{tikzpicture}




## Example Requirement


![](../assets/images/requirement-ex.png)

\vspace{1em}

*Hash* is calculated over *Name*, *Description* and *Verification Method*.
Rationale is only informative


```bash
$ sha256sum "${Name}${Description}${VerifMethod}"
```


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
<testcase   line="20" name="test_read_write_engines" time="2.830">
  <properties>
    <property name="req" value="SW-AS-501-f8d68d11"/>
    <property name="req" value="SW-AS-500-4c1a395a"/>
  </properties>
</testcase>
```
:::


## Traceability Matrix

![](../assets/images/tracemat-ex.png)



## Integrating Requirements into CI/CD

* Integration for every output document
* Match *open* and/or *failed* issues
* Example for *failed* issues

```bash
$ bash -ec 'test "$(grep -c failed \
    arch/artifacts/tracematrix.tex)" -eq "0"'
```


## Document Baseline

Every document has a its own version tag

```bash
$ git tag -a RS/1A
$ git describe $(git log -n 1 --format=%H -- docs/reqs)
```

The output from `git describe` will be used as document baseline

```bash
  RS/1A — 0aec3ad0              # good
  RS/1A-8-g76b3ffe — 76b3ffe4   # tainted
```

Example excerpt from page 7

![](baseline-footer.png)




\note{This is all nice and dandy; but how do we communicate with people for whom git clone is too much to ask?}

# Business Interface


## Excel Workflow

* Non-tech people define the requirements
* Familiarity / Ease-of-use
* Consistency of Documents
    * Works if all you've got is Office and E-Mail

* INSERT IMAGE HERE



# Conclusion

## Storytime Revisited

* Requirements shipped with code \checkmark
    * Including relational meta-information
* Traceability matrix automated \checkmark
* Continuously updated documentation \checkmark
    * Document Versioning (baselining) \checkmark

\note{Your Jira workspace will be gone}


# Questions




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



## *rmtoo* -- Introductions

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


## Installation

Traceability features are in the beta releases.

```bash
$ pip3 install sltoo>=25.1.0b3
$ wget https://kown7.github.io/pymergevcd/assets/template_project.zip
```

## Future Developements

* Write Parser for *Test Reports* \checkmark
* Documents with the correct identifier automatically solve the specification
	* Document Formats:
	    * docx (maybe with pandoc)
		* \LaTeX \checkmark
		* Text


## Final Thoughts

* Never test against your requirements
* Always write some form of test specification

## Licensing

\doclicenseThis














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



