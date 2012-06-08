---
layout: post
title:  TFS Not for Developers
tags:   splm, tfs, tfs 2010, tfs 2012

synopsis: In which I temper my enthusiasm for TFS with developer hardships.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

Over the past month I have taken a deep dive into the use and customization of
Team Foundation as an application lifecycle management system. I've looked at
both the 2010 and 2012 beta versions and, for the most part, feel admiration
for the systems. It really allows different team members to access information
that they need to create, review, or modify within the lifecycle of the
application.

Some things that I *really* like:

* PowerPoint as a screenshot mocking tool
* SharePoint integration for deep understanding of project status
* Task association to commits
* Custom "work items" with semantic linking
* Possible integration of source, work items, and build
* User feedback gathering through screen/audio recording
* Exploratory testing

All of those things help non-developers to really understand the status of a
software project. That really represents the largest hurdle of any software
project because software development remains opaque to those that do not read
source code with even the most communication-based process. This part of TFS,
though requiring crazy licensing navigation and purchase, makes a lot of sense
to me and has some of the most advanced features I've seen in an ALM.

Unfortunately, I think the TFS team really latched onto the word
"management" in Application Lifecycle Management. Regardless of the project, I
think that code monkeys remain the primary users of ALM tools and when a
system like TFS pushes itself into their bailiwick, it needs to understand the
usage patterns of software developers. And, not Microsoft's internal
developers.

Associating a commit to a work item (task, bug, etc.) is an exercise in modal
dialogs and querying. That sucks. Bad. TeamForge does it correctly with `svn`
simple work item id in the commit message. JIRA also provides this capability
to track bugs to commits in multiple source controls. Dialog-driven management
kills developer productivity.

Intra-team code review embedded in Visual Studio has some of the worst
usability that I've ever seen. I consider
[Crucible](http://www.atlassian.com/software/crucible/overview) the standard
for code review. TFS falls extremely short of this simple UX benchmark.

I often program on my laptop. Most laptop screens now have "widescreen" ratios
that drastically reduce the vertical real estate available for a view. As we
all know, scrolling kills comprehension. TFS integration into Visual Studio and
Eclipse requires a lot of this scrolling because of the list-like interfaces
that the team has created.

Now, this is philosophical, but I consider shelving antithetical to good
branching strategies. The ease with which TFS allows shelving will lull good
developers into bad practices. Shelves don't share and good development must
share.

