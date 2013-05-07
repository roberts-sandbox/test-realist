---
layout: post
title:  Modeling in Color, Part I
tags:   OOD

synopsis: The first in a series of entries talking about Modeling in Color
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

Over the past six years, I've tried to apply the lessons from Eric Evans' book
with regards to collecting requirements from customers and, then, building a
robust object-oriented design that embodies those requirements. I have had quite
a bit of success with *domain-driven design* and can attest to its strengths.
However, when I started using Evans' recommendations, I had already spent the
previous eight years honing my OO acumen, decomposing real-world problems into
software-based solutions.

As you may have noticed, I haven't written in a while. Between bringing home the
bacon, eating the bacon, and riding around on another
[porcine entity](http://www.harley-davidson.com/en_US/Content/Pages/2012-Motorcycles/softail/fat-boy/fat-boy.html),
I haven't spent time tending this little word garden. Yeah, shame on me. But,
I recently spent some time talking with my nascent development team about
object-oriented design and how they should perform it as we move into a
business-focused cycle of coding. I wanted some process that would provide a
standard by which they could enter into the practice of OOD and come out the
other side with philosophically similar designs.

What to do?

Sitting in my office, I looked over at my Bookshelf of Broken Technologies™ and
spied a book that I hadn't read since the early 2000s:
[Java Modeling In Color With UML: Enterprise Components and Process](http://dl.acm.org/citation.cfm?id=554136).
I vaguely remembered something about Post-it® Notes. I read the book through and
sat back amazed.

This was it! An easy-to-understand, attainable OOD philosophy. With examples.

Let me write that, again. WITH EXAMPLES!

I think that most beginners have trouble with OOD books because they show ```Dog
inherits from Animal```. And, that's it. They want something more. Something
concrete. Coad, et. al. gives 61 concrete examples of how to use modeling in
color.

Head First ain't got nothing on that.

## The basics

I will get the basics out of the way and then explore examples of modeling in
color in the following days.

Any domain model consists of four basic class types, or four *archetypes*. They
are:

<dl>
  <dt>Description</dt>
  <dd>Common information for a kind of thing.</dd>
  <dt>Thing</dt>
  <dd>A party, place, or thing.</dd>
  <dt>Role</dt>
  <dd>A type of behavior that a _Thing_ takes on to participate in transactions.</dd>
  <dt>Moment-Interval</dt>
  <dd>A moment in time or interval of time that has particular importance to the business process or legal purposes.</dd>
</dl>

The «description» provides common attributes and behavior for a «thing». The
«thing» takes on a «role» to create or participate in a «moment-interval»
transaction.

And, why color? That's because each of those archetypes have a color associated
with them in UML diagrams.

* Description → Blue
* Thing → Green
* Role → Yellow
* Moment-Interval → Pink

And, here's a dumb example of the relationships.

![Relationships for archetypes](/img/archetypes.png)
{: .center }

With the example in the above figure, we see that a `LanguageType` provides
common descriptive attributes or behavior for `Language`.  (`LanguageType`
provides prototypal inheritance for `Language`.) An instance of `Language` can
have the `Spoken` role. With that role, the `Language` can participate in
`Speech`es.

An academic example, to be sure. Tomorrow, we'll get into a better example and
build an application around it.
