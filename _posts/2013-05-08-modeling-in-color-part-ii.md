---
layout: post
title:  Modeling in Color, Part II - Categorizing Classes With Archetypes
tags:   OOD

synopsis: Considering the first step of modeling in color.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

[Yesterday's post]({{page.previous.url}}) kind of sucked. Sorry about that. It
seems that my perishable skill of writing nears six feet under. I'll
endeavor to make today's post more lucid, cohesive, and informative. Perhaps
that will revive my chosen word.

I told my nascent development team that we would use modeling with color as our
object-oriented design philosophy. Then, I reserved a conference room for four
mornings so we could learn this practice first hand. I started by showing them
the following list of user stories.

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

Then, I asked them to break out in groups and create some static class diagrams
that model the problem. From three groups, we had four designs emerge. They all
looked like candidates for creating software to address the user stories.
However, they all looked different. They all lacked some transactional
information. Nothing wonky, mind you. Nobody forgot to include a `Person` class.
But, this project that we've launched will grow in number tenfold over the next
year; I want the code to look and feel the same regardless of who wrote it and
when they wrote it. Modeling in color to the resuce!

## Colors and the Domain-Neutral Component

Recall that we have the following *archetypes* for classes in our domain model.

<table>
  <thead>
    <tr>
      <th>Archetype</th>
      <th>Color</th>
      <th>Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Moment-Interval</td>
      <td>Pink</td>
      <td>
        Describes a moment in or interval of time that the application should
        track for business or legal reasons.
      </td>
    </tr>
    <tr>
      <td>Moment-Interval Detail</td>
      <td>Pink</td>
      <td>
        Describes a detail of a «moment-interval».
      </td>
    </tr>
    <tr>
      <td>Thing</td>
      <td>Green</td>
      <td>
        A party (person or organization), place, or, well..., thing.
      </td>
    </tr>
    <tr>
      <td>Role</td>
      <td>Yellow</td>
      <td>
        A specific kind of behavior taken on by a «thing» to allow it to create
        or participate in the creation of «moment-interval»s.
      </td>
    </tr>
    <tr>
      <td>Description</td>
      <td>Blue</td>
      <td>
        A prototype for one or more «thing»s.
      </td>
    </tr>
  </tbody>
</table>

Using those four archetypes, Peter Coad, Jeff de Luca, and Eric Lefebvre
formalized a standard relationship for classes that fulfill these archetypes.
They dubbed that formalization the *Domain-Neutral Component* (DNC) because they
posited that, regardless of the problem domain, the DNC provides an adequate
structure to express the associations, behavior, and data needed. That structure
looks like this.

![Domain-Neutral Component](/img/dnc.png)
{: .center }

The «plug-in points» allow you to provide different strategies at different
levels in the component.

Modeling with the DNC means identifying the «moment-interval» of interest, then
the participating «thing» in that transaction, then any «role»s those «thing»s
expose, then any «description»s that contain prototype-level attributes or
behavior.

In some cases, you will have classes that will fill all of the reserved blocks
in the DNC. In other cases, you may find that you have only two. The relevant
point to glean from this: start with the DNC and take away superfluous boxes
until you have reached what you need. Take away the things you don't need. Don't
suffer from
[blank-page syndrome](http://www.codinghorror.com/blog/2005/10/avoiding-blank-page-syndrome.html).

You should never have a DNC that does not contain a «moment-interval».
{: .important }

Quoting Eric S. Raymond in <u>The New Hacker's Dictionary</u>, we find similar
advice from
[a pretty cool guy](http://en.wikipedia.org/wiki/Antoine_de_Saint-Exupéry):

> The French aviator, adventurer and author Antoine de Saint-Exupéry, probably
> best known for his classic children's book The Little Prince, was also an
> aircraft designer. He gave us perhaps the best definition of engineering
> elegance when he said "A designer knows he has achieved perfection not when
> there is nothing left to add, but when there is nothing left to take away."

# Starting to model with color

Those user stories at the top of this page describe some of the functionality
for software to administer an athletic club. We can do our usual "list of nouns"
that starts most object-oriented design sessions and come up with the following
nouns at first blush.

* member
* instructor
* class
* invoice
* equipment
* reward
* member purchase
* reservation
* member arrival
* person
* room
* payment

That may not consist of all of the nouns implied by the user stories, but I
think it represents a good start. Now, we should classify each of the nouns as
one of the four *archetypes*.

<table>
  <thead>
    <tr>
      <th>
        Moment-Interval<br>
        Moment-Interval Detail
      </th>
      <th>Role</th>
      <th>Thing</th>
      <th>Description</th>
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
    </tr>
  </tbody>
</table>

We'll start tomorrow with that first column containing the «moment-interval»s
and laying out their flow from one to another. In that way, we can model the
flow of information through the business processes and the features that they
represent. Then, we'll fill out DNCs for each of the «moment-interval»s to
complete the design portion of the classes for the athletic club software.
