---
layout: post
title:  Modeling in Color, Part III - The Mighty «moment-interval» Archetype
tags:   OOD

synopsis: In which I discuss the "timeline" core to modeling in color.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

In **Java Modeling in Color with UML**, the authors define the «moment-interval»
archetype as

> something that one needs to work with and track for business or legal reasons,
> something that occurs at a moment in time or over an interval of time.

Originally, Peter Coad called this archetype «transaction»; however, this caused
a lot of confusion in the programming community due to the implication that
"transaction" meant "business transaction", like a sale or a purchase. Coad
actually meant the purer definition of the word as *an exchange or interaction
between parties*. Because of the confusion, he renamed the archetype from
«transaction» to «moment-interval», a more cumbersome phrase with a neutral
meaning.

This post discusses finding «moment-interval»s in our problem domain and using
them in our object-oriented designs.

## Finding «moment-interval»s

Because I've done this software thing for quite a while, identifying
«moment-interval»s in a problem domain comes naturally. For newer modelers,
[Stephen R. Palmer](http://www.step-10.com/SoftwareDesign/ModellingInColour/Moment-Interval.html)
offers some valuable advice.

> When looking for Moment-Interval classes for a particular piece of software,
> we need to consider things like significant events and activities, business
> transactions, steps in a process, or interactions within a business
> relationship that are within the scope \[of\] our software system,
> application, or component.

In most (all?) books that discuss object-oriented design, the authors suggest
to find the nouns to find the classes in the problem domain. As invaluable as
that advice may sound, sometimes a «moment-interval» masquerades as a verb in
the problem domain. Here, again, I present the requirements for our athletic
club software.

* People join the club to become members and get invoiced monthly a flat fee and
  participation fees for classes
* Participation fees for classes consist of a prorated amount of the
  instructor's hourly rate and a percentage of the cost of the equipment used by
  participants in the class
* Record member purchases of food and beverages from the club for rewards 
* For every ten dollars spent on food and beverages from the club, the member
  receives a one dollar credit on their next invoice.
* Members RSVP for classes and their arrival is recorded
* Instructors schedule rooms and equipment for classes

Consider the first part of the first statement.

> People join the club to become members

We see the nouns *people* and *members*. However, the verb *join* implies a
transaction between a person and the club. That transaction, let's call it
"membership", embodies a moment in time that a person becomes a member. We have
found a «moment-interval» that did not have a direct name!

## Business processes described as a sequence of «moment-interval»s

Transactions in a business process rarely exist in isolation. For example, at my
university, I had to enter into an `Enrollment` transaction with the school
before I could enter into a `Graduation` transaction from the school. These
transactions occur in a flow: I enroll →  I pass classes → I graduate.

When we model in color, we use the «moment-interval» archetype to specify each
of the steps of a process to track as part of our software. A «moment-interval»
can have zero-to-many previous «moment-interval»s and zero-to-many
«moment-interval»s that occur after it. These chains allow us to construct the
behavior and data associations across the lifetime of a business process.

Let's take a look at the list of «moment-interval»s from the athletic club
requirements:

* class
* invoice
* member arrival
* member purchase
* membership
* payment
* reservation
* reward

For a lot of these transactions, everything must start with a membership. So,
that's where we start. Then, other «moment-interval»s follow as events that
occur after a person's initial transaction of *membership*. My take on it
appears in the figure below.

![Timeline for athletic club](/img/timeline.png)

And, there we have it. The next exercise will consist of filling out the «role»,
«thing», and «description» participants for each of those transactions.