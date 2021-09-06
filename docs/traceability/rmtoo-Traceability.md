---
title: "sltoo -- Integrating Requirements into CI/CD"
author: Kristoffer Nordström
date: \today
institute: \texttt{\url{info@sltoo.dev}}
header-includes: |
  \usepackage{hyperref}
  \usepackage{appendixnumberbeamer}
  \usetheme[block=fill,progressbar=frametitle]{metropolis}
  \usepackage{pgfpages}
  \setbeameroption{show notes on second screen=right}
  \usepackage[
    type={CC},
    modifier={by-nc-sa},
    version={3.0},
  ]{doclicense}
---


# Motivation

\note{

\begin{itemize}

\item Welcome everyone; it's an honour to open this topic's session: Applied SE.

\item Couple of words about myself

\item When talking about requirements, we should also define the requirements of the problem we're trying to solve.

\item Storytime

\end{itemize}
}


## Motivation

* Fully automated traceability matrix
* Consistent and up-to-date documents from the source
* Store (requirements') meta-information with code

\note{
\begin{itemize}
\item It's fine manually. Requirements change find minimal delta-test? Change
more than once. Hence we want this fully automated.

\item Review multiple documents for a different
contractor. No consistent set of documents were provided

\item Jon Holt's term in introduction to MBSE: Documents are a live *view* of
the system (not pretty pictures). CI/CD for software, why not for documents?

\item Every ALM tool will do this for you so far

\item It came with one document that contained all requirements and use-cases. It
appeared to have been exported from some web-based tool. All the information therein
is lost

\item Also: Too technical, interface with management/business side
\item 4'

\end{itemize}
}


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

* *Requirement A*
    * Red button to shut down system
* *Implementation a* says implemented A
	* Traceability can be automated
	* Machine-readable
* What if *A* changes?
	* *A* knows nothing of *a*

\begin{tikzpicture}[remember picture,overlay]
    \filldraw[fill=red!30!white, draw=red,thick] ([xshift=4.2cm,yshift=-2.5cm]current page.center) circle (1.5cm);
    \filldraw[fill=red!80!white, draw=red,thick] ([xshift=4cm,yshift=-2.3cm]current page.center)   circle (1.5cm) node[align=center, text=white] {\textbf{PANIC}} ;
\end{tikzpicture}


## Traceability

* *Requirement A*
    * Green button with large friendly letters: don't panic
* *Implementation a* says implemented `A`
	* Traceability can be automated
	* Machine-readable
* What if *A* changes?
	* *A* knows nothing of *a*
	* Traceability isn't given anymore


\begin{tikzpicture}[remember picture,overlay]
    \filldraw[fill=teal!20!green!30!white, draw=teal!20!green,thick] ([xshift=4.2cm,yshift=-2.5cm]current page.center) circle (1.5cm);
    \filldraw[fill=teal!20!green!80!white, draw=teal!20!green,thick] ([xshift=4cm,yshift=-2.3cm]current page.center)   circle (1.5cm) node[align=center, text=white, text width=2.5cm] {\textbf{DON'T PANIC}};
\end{tikzpicture}




## Proposed Solution

* *Requirement A-1.0*
    * Red button to shut down system
* *Implementation a* says implemented *A-1.0*
    * *A-1.0* (red button) changes to *A-2.0* (green button)
	* Use hashes instead of semantic versioning
	* Calculated automatically


\begin{tikzpicture}[remember picture,overlay]
    \filldraw[fill=teal!20!green!30!white, draw=teal!20!green,thick] ([xshift=4.2cm,yshift=-2.5cm]current page.center) circle (1.5cm);
    \filldraw[fill=teal!20!green!80!white, draw=teal!20!green,thick] ([xshift=4cm,yshift=-2.3cm]current page.center) circle (1.5cm) node[align=center, text=white, text width=2.5cm] {\textbf{DON'T PANIC}};
\end{tikzpicture}


\note{Why hashes: no tool or manual changes required, it's all derived

Let's see how it looks on an example}



## Example Requirement


\vfill

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
*Hash* is calculated over *Name*, *Description* and *Verification Method*


```bash
$ sha256sum ${Name} \
    ${Description} \
	${VerifMethod}
```

::::

:::

\vspace{1em}

![](../assets/images/requirement-ex.png)


\vfill\tiny
Example from [pymergevcd's architecture specification](https://kown7.github.io/pymergevcd/#architecture)

\note{

\begin{itemize}

\item Every requirement is in its own file

\item A from previous slides is now SW-AS-501

\item Version n.0 is now \texttt{F8D68D11}

\end{itemize}

}



## Testing the Example Requirement

* Requirement ID: `SW-AS-501`
* Hash: `F8D68D11`

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

![](tracemat-example.trans.png)

\note{Now it should be straightforward to integrate it into any CI pipeline}

## Integrating Requirements into CI/CD

* Integration for every output document
* Match *open* and/or *failed* issues
    * Left as an excercise for the reader
* Example for *failed* issues

```bash
$ bash -ec 'test "$(grep -c failed \
    arch/artifacts/tracematrix.tex)" -eq "0"'
```



\note{
9'
}


# sltoo in Practice

\note{

\begin{itemize}

\item sltoo based on rmtoo: text-file based req. tracking tool

\item Tracking requirements in text files with git --> might be ideal for engineering department

\item Defining system behaviour is a team effort

\item Solution not for everyone / clunky UI

\item Guess: most people aren't familiar with the tooling/console --> Which tool is "everyone" familiar with?

\end{itemize}
}


## Excel Workflow (I)

* Defining system collaborative effort
* Familiarity / Ease-of-use
* Consistency of Documents
    * The *Truth* is always in your repository
    * Templating for branding
* Works if all you've got is Office and E-Mail
* Getting Started: Edit [example Excel-Sheet](https://kown7.github.io/pymergevcd/assets/requirements/artifacts/specification.xlsx)

\centering
![](../assets/images/excel-ex.png){ width=75% }

\note{Simply use the excel sheet as long as no documents or verification tasks are necessary

Stepping stone for requirements tracking
}

## Excel Workflow (II) – Distribution


\centering
![](Workflow-init.png){ height=75% }


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

Example excerpt from page 7:

![](baseline-footer.png)

\note{Exercise to reject tainted documents in referenced documents}


## Excel Workflow (III) – Merging

\centering
![](../assets/images/Workflow-feedback.png){ height=75% }

\note{
\begin{itemize}

\item Commit for every author individually -> also put name in commit for easier lookup
\item Truth stays in repository
\item \texttt{git tag} makes new document releases as easy as possible

\end{itemize}
}

# Conclusion

## Storytime Revisited

* Requirements shipped with code \checkmark
    * Including relational meta-information
* Traceability matrix automated \checkmark
* Continuously updated documentation \checkmark
    * Document Versioning (baselining) \checkmark

A familiar UI for all stakeholders included

\note{Your Jira workspace will be gone}


# Questions




\appendix



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


## Alternatives

* [Sphinx-Needs](https://sphinxcontrib-needs.readthedocs.io/en/latest/)
* [Octane ALM](https://www.microfocus.com/en-us/products/alm-octane/overview)
* [Codebeamer](https://codebeamer.com)
* [Aligned elements](https://www.aligned.ch/)
* See [Wikipedia](https://de.wikipedia.org/wiki/Software-Configuration-Management#Diverse_Softwareentwicklungsprodukte)
* ...

## Future Developements

* Write Parser for *Test Reports* \checkmark
* Documents with the correct identifier automatically solve the specification
	* Document Formats:
            * docx (maybe with pandoc)
            * \LaTeX \checkmark
            * Text
            * CAD Files from HW/Mechanical
* GUI with multi-documents support (RS/TS/..)
    * Simplify design process

## Final Thoughts

* Never test against your requirements
* Always write some form of test specification

## Licensing

\doclicenseThis




