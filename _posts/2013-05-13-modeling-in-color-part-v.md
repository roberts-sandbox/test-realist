---
layout: post
title:  Modeling in Color, Part V - Full Domain-Neutral Component for the Athletic Club Exercise
tags:   OOD

synopsis: In which I present my full model for the athletic club exercise.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

## The requirements

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

## The nouns

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
        <strike>reward</strike><br>
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
        reward<br>
        <strike>equipment</strike>
      </td>
      <td>
        equipment
      </td>
    </tr>
  </tbody>
</table>

## The design

<a href="/img/full-athletic-club-dnc.png" target="_blank">
  <img src="/img/full-athletic-club-dnc-small.png" alt="full atheletic club dnc">
</a>
<div class="caption"><caption>Click image to enlarge</caption></div>

When you see multiple occurrences of `Person`, `Member`, and `Instructor` in
that diagram, those are not different classes. I just want to show each of the
transaction participants.