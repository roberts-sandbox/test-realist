---
layout: post
title:  My Perfect Software Lifecycle Management Tool
tags:   splm

synopsis: In which I dream a little dream.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

I recently met a friend of a friend that has founded a company to provide
Building Information Modeling (BIM) software-as-a-service. He described the
flow of information through the construction process, from architects to
building owner. He lamented the loss of information that occurred during the
process in its current incarnation. He evangelized his dream for unifying BIM
in a suite of tools across the construction data ecosystem.

And, it made me remember my own dream about a very nice tool that does the
same thing for software.

## Where Are You Going, Where Have You Been?

Context is everything.

### Developers care about "what" and "how" and sometimes "why"

When I write software, I like to know what I need to write. Somewhere someone
had to have said, "Gee, it sure would be nice if it did this..." And, my job
is to implement *this* in a maintainable way.

### Managing developers care about "what," "how", "why", "when" and "how much"

When I manage software teams, I like to know why my team is writing something
as well as what they're writing and how that ties back to the requirements.
Then, I can use that knowledge to figure out how much more stuff they can
implement over some period of time.

### Big-bosses care about "why" and "when" and "how much"

Quite often, big bosses get frustrated with the software development
lifecycle. If they are business guys, then they don't know the mechanics. If
they're former programmers, then they're usually pretty good and can't
understand why things take so long. In either case, they lose the transparency
into the construction of the software because they've removed themselves from
the day-to-day coding.

### Sales gals and guys and USERS care about "when"

Really. That's it. What else is there to say?

## Our history is still an oral tradition

Good agile practices rely heavily on communication. The form of communication
that we developers rely on the most is talking. We ask each other questions,
we depend on one another's critiques, we collaborate in design sessions, we
talk and talk and talk.

That's a fundamental part of programming.

However, that oral tradition hurts the team when someone leaves and can't
answer a specific question to which they know the answer. Another person
leaves and we've lost the reason why some programmers built our software in a
specific way. Another person leaves and we might as well subscribe all of the
existing code to some mysterious event some time in the distant past.

## The agile dream failed. In parts.

In the beginning, we had eXtreme Programming. We saw it and said, "This is
good." Unit tests, pair programming, snacks, 40-hour work weeks, on-site
customer, very nice facets for a development methodology because, after all,
we didn't have a development methodology before that.

Sure, we had lots of management methodologies like RUP and ISO/IEC 12207 that
defined the software lifecycle process and artifacts and hwo to gather
requirements, but we didn't have a process by which you and I would sit down
and write some code. That was still the Wild West.

Shooting from the hip didn't satisfy the "old guard" anymore. They wanted to
help developers create maintainable software reliably with a repeatable
process.

### Where'd pair programming go?

I really like pair programming and try to do it whenever I can. I especially
like the format where one programmer writes a unit test, both agree on what it
expresses, the other programmer writes the implementation, both agree on it,
lather, rinse, repeat.

Most of the shops that I know have slowly abandoned the practice not due to
tight deadlines and "the usual excuses" but because the *programmers decided
that they liked programming by themselves!* We're just a bunch of asocial
creatures, I guess.

### The survivor: unit tests

Of all of the practices, unit tests seem to have taken the deepest root in
the minds of point-haired bosses and developers alike. With 100% code
coverage, we can make sure that more development or "bug fixes" don't break
the existing expectations of the code base.

What I think we've forgotten, though, is that unit tests are also supposed to
act as living and executable documentation. I should be able to write a small
parser that scans unit tests in any language, reformat the name of each test,
and end up with a description of the behavior of the *entire system*.

Could you do that with your unit tests? Probably not. And that's ok, because
when test-driven development failed to provide that living documentation, we
did what all good software developers do and invented something "better". We
created behavior-driven development.

Admittedly, most BDD harnesses read much better than a list of reformatted
unit test names. When I first came across **coulda** and **cucumber** in the
Ruby community, I felt something close to overwhelming joy because I felt that
we had reached a place where we could have that living documentation that
XP hoped unit tests would provide. It definitely helped with writing tests
that non-programmers could read, understand, and (given the inclination)
write. It helped communicate the intent of the software, could tie back to the
original requirements through URLs or something akin to that, and read much
more like natural language.

After a while, though, I realized that people abandoned the BDD documentation.
The Features and Scenarios ended up as abandoned as their unit test cousins.
Project managers, product managers and business analysts continued to use
their Microsoft Word documents to power the development process. Or, worse,
Microsoft PowerPoint presentations as requirements.

Never accept a PowerPoint presentation as a requirements document.

## Scrum is not a development methodology

Yep. That's right. I wrote that.

Scrum is a management methodology.

We use scrum to manage the user stories, to handle status reporting, to decide
our next actions. But, it's not a development methodology. 

## Bug-tracking software is not for requirements. Requirements management software is not for bugs.

The XP books consider a bug as another user story that a customer can schedule
into an iteration.

However, bug-tracking software is not a user story managment system,
regardless of how many plugins you add to JIRA.

And, requirements management software is not a bug-tracking system regardless
how much crap Quality Center shoves into that huge system.

Furthermore, requiremets management and bug-tracking software rarely
intimately ties into code changes and unit tests, unit tests rarely refer to
the requirement or bug to which it relates, and reporting any kind of
meaningful metric from these systems often leads to context-free numbers.

Have you ever been in a meeting where someone presents a table of bugs or
issues listed by severity along with a project plan that ties back to features
broken down to tasks with color coding all over the place, usually green?

Meaningless.

## What can a poor developer/manager/executive do?

Build something better. I want software product lifecycle management software.
I want actions tied together so I can understand how the software grows and
how much it costs. I want something that can help with projections and
time lines, estimated costs and times, knowledge bases and bugs that can find
someplace to live in the overall product's maturity. I want my developers to
not mind using it because it adds value for their daily processes and stays
out of their way the rest of the time. I want my CEO to open a window and get
his super-cool dashboard with meaningful metrics, confidence intervals, and
costs-to-date and projected costs.

I want SPLM for real.

The Enterprise version of CollabNet's stuff, Microsoft's Team Foundation
Server, IBM's Rational suite all have interesting solutions that tie into
their own software. That's cool. But, it's not for me. None of them support
"agile" very well. None of them care about the product from
twinkle-of-an-idea to five-years deployed and supported by some guy named Pete
at the end of a 1-800 number.

Other solutions serve singular parts of the overall process pretty darn well.
Mingle, JIRA, TeamCity, FogBugz, blah de blah, seen 'em all, impressed by
some, faithful to none.

## My list of minimum requirements

My ideal solution would have the following features and some workflow to tie
all that crap together.

* Idea capture
* Requirements capture and maturity
* Technical breakdown of requirements
* Non-technical requirements capture
* Project and iteration planning
* Commit-requirement association
* Cost calculation and projection
* Knowledge base - technical and non-technical
* Hyperlinked documentation generation from tests and code
* Source control integration
* Continuous integration integration
* Continuous deployment integration
* Issue management and triage
* CRM integration
* Stupid-easy time entry

Wow. That's a lot. Never mind. No one'll get it right.

*wink*
