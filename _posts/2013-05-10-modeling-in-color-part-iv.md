---
layout: post
title:  Modeling in Color, Part IV - DNCs for «moment-interval»s
tags:   OOD

synopsis: In which I discuss identifying the «description»s, «thing»s, and «role»s in our example
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

This post concerns itself with identifying the participants in our domain model
that we have not classified as «moment-interval»s. That means we'll look at
«thing»s and their associated «description»s and «role»s. But first, I want to 
recap what we've completed so far over the past couple of days in case you've
jumped in mid-series. If you've followed along, however, you can jump to the
[new stuff](#)

## Work completed so far

### The user stories

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

### The identified concepts in our domain model by archetype

<table>
  <thead>
    <tr>
      <th>
        Moment-Interval (Pink)<br>
        Moment-Interval Detail (Pink)
      </th>
      <th>Role (Yellow)</th>
      <th>Thing (Green)</th>
      <th>Description (Blue)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        class<br>
        invoice<br>
        reward<br>
        member purchase<br>
        reservation<br>
        member arrival<br>
        membership<br>
        payment
      </td>
      <td>
        member<br>
        instructor
      </td>
      <td>
        person<br>
        room<br>
        equipment
      </td>
      <td></td>
    </tr>
  </tbody>
</table>

### The «moment-interval» "timeline"

In the [last post]({{page.previous.url}}), I worked on a draft design that took
the moment intervals and laid them out in the flows that identify our business
processes. The following figure shows that timeline.

Note that I have left off the archetype indicator «moment-interval» on the
classes in the diagram. The fact that I colored the classes pink tells us that
each of those classes have the «moment-interval» archetype.

![«moment-interval» timeline for the atheletic club requirements](/img/timeline.png)

## Domain-Neutral Components (DNCs) for the «moment-intervals»

To complete our domain model, we need to figure out the way in which the other
classes participate in the «moment-interval»s identified and associated for our
domain model.

I'll walk through a couple of examples for how I would go about assigning the
relationships. Then, I'll just present a completed domain model for you to grok
at your leisure.

I follow a simple methodology when completing the classes in a DNC:

1. Identify the transactions in the system along their timelines
1. Identify the participants of each of those transactions
1. Determine roles needed to participate in the transactions
1. Refactor common data to descriptions

### The DNC for `Membership`

As with every exercise that involves using the Domain-Neutral Component, we
start by identifying the «moment-interval» that acts as the nexus for the DNC.

![membership dnc step 1](/img/membership-dnc-1.png)

The first step we color modelers should take questions the need for
«moment-interval detail»s in this DNC. As far as the requirements go, the
`Membership` transaction has no collection of time-related details, so we can
get rid of the placeholding pink box.

![membership dnc step 2](/img/membership-dnc-2.png)

Now, as color modelers, we should determine the «thing»s that participate in the
transaction. Our thing list consists of `Person`, `Room`, and `Equipment`. Our
requirement reads

> People join the club to become members

Conspicuously missing from our list is the `Club` class. In software that would
manage more than one club at a time, it would make sense to have a `Club`
«thing». Because we have no such requirement, `Club` acts as an implied
participant in every transaction.

Through a process of elimination of the available «thing»s, we conclude that the
`Membership` «moment-interval» has `Person` as its only participant.

![membership dnc step 3](/img/membership-dnc-3.png)

Only «description» and «role» boxes remain. Starting with the «role», we ask,
"Does the `Person` play a «role» in this transaction?" Reviewing the «role»s
we've defined in this domain, «member» and «instructor», there's really only one
choice, eh?

![membership dnc step 4](/img/membership-dnc-4.png)

Finally, we have this concept of the «description». We must ask ourselves if we
have different groups of `Person`s that participate in this system. For us, we
have just people, not "rich people" and "poor people", "smart people" or
"Tea Party members" (I just lost some of my readership...), you know,
categories of people. No. We don't have those categories. Our system only deals
with people as
[meat bags](http://theinfosphere.org/Bender_Bending_Rodr%C3%ADguez). So, we get
rid of the «description» archetype placeholder and we arrive at the
`Membership` DNC.

![membership dnc step 5](/img/membership-dnc-5.png)

### The DNC for `ProposedClass`

Again, general DNC time for the `ProposedClass` «moment-interval». Note that
the `ProposedClass` «moment-interval» has two types of
«moment-interval-detail»s: `EquipmentUsage` and `Reservation`.

![proposed class dnc step 1](/img/proposedclass-dnc-1.png)

Now, let's look at the transaction `ProposedClass` and ask ourselves, "Who or
what makes that transaction?" That's a transaction between a `Person` acting as
an `Instructor` and the club. As stated before, we don't have a specific club
class, so the «moment-interval» for `ProposedClass` should look like this.

![proposed class dnc step 2](/img/proposedclass-dnc-2.png)

Next up, let's look at the «moment-interval-detail» `EquipmentUsage`. We have a
«thing» called `Equipment` in our list of identified nouns. Now, a «thing»
should represent something specific in the world. No where in our requirements
do we have to do inventory tracking for balls, racquets, mats, ropes, bean bags,
and the like. So, we don't have to track individual «thing»s. Rather, we just
need to track collections of types of equipment. That means that I have a
mistake in my initial categorization of nouns. :( So, let's fix that.

<table>
  <thead>
    <tr>
      <th>
        Moment-Interval (Pink)<br>
        Moment-Interval Detail (Pink)
      </th>
      <th>Role (Yellow)</th>
      <th>Thing (Green)</th>
      <th>Description (Blue)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        class<br>
        invoice<br>
        reward<br>
        member purchase<br>
        reservation<br>
        member arrival<br>
        membership<br>
        payment
      </td>
      <td>
        member<br>
        instructor
      </td>
      <td>
        person<br>
        room<br>
        <strike>equipment</strike>
      </td>
      <td>
        equipment
      </td>
    </tr>
  </tbody>
</table>

Due to that reclassification, `Equipment` participates in the transaction and
doesn't need a «role» because the `Equipment` doesn't change the way that it
participates in transactions. So, now we have this refined DNC.

![proposed class dnc step 3](/img/proposedclass-dnc-3.png)

Finally, our requirement about `Reservation`s reads

> Members RSVP for classes

So, we fill in the «role» and «thing» appropriately, get rid of the
«description», and we get this.

![proposed class dnc step 3](/img/proposedclass-dnc-4.png)

## Try the rest

Left as an exercise for you for the weekend, try filling out the DNCs for each
of the remaining «moment-interval»s. I'll post my design on Monday.

Have fun!