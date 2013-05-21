---
layout: post
title:  Building a Web Grid - Part 1
tags:   html, jquery, widget

synopsis: In which I disucss the goals of grijq.
---
Last week I needed to convince some folks that the World Wide Web can act as a
deployment platform for enterprise applications. They had some bad experiences
with Web applications a couple of years ago and, since that time, felt
convinced that desktop applications could only serve that niche of
data-intense applications. I believe in the power of the browser and worked on
a small demonstration Web application that would corroborate my beliefs.

Data-rich applications traditionally have grids. Users have grown comfortable
scanning hundreds of rows of text and numbers to perform some kind of
analysis. Trying to convince them that alternatives exist that could present
the data in more comprehensible ways can pose challenges because these good
people have adopted the Religion of the Grid.

> They can have my Excel when they pry it from my cold, dead fingers.

To quell their unease, I went in search of a data grid that would meet my
needs for this demo. The data grid had to

<ul>
  <li>gracefully handle thousands of cells</li>
  <li>
    allow keyboard-only input to:
    <ul>
      <li>activate cells with arrow keys</li>
      <li>activate cells with TAB and ENTER keys</li>
      <li>
        start editing cell content by
        <ul>
          <li>pressing F2 to edit at the end of the cell</li>
          <li>start typing to replace the entire cell's content</li>
        </ul>
      </li>
    </ul>
  </li>
  <li>comply with the jQuery UI CSS framework</li>
  <li>have read-only functionality for cells, rows, and tables</li>
  <li>have column resizing</li>
  <li>handle fixed widths and heights</li>
  <li>have fixed headers</li>
  <li>have a pluggable editor architecture</li>
  <li>and work with HTML tables and not from a JavaScript data store</li>
</ul>

That last requirement emerges from a vested interest in using
[knockout.js](http://knockoutjs.com) for binding data in the browser. I really
want an interactivity widget that rests atop *knockout*'s HTML rendering. I
don't want the grid to render, just handle interaction.

For one reason or another, the grids that I've used in the past failed to meet
one or another of these needs: jqGrid, ExtJs Grid v3 and v4, SlickGrid,
dojox.grid, and the DataTables from YUI 2 and YUI 3.

## If I can't find it, I'll build it: grijq

That's pronounced "gridge." The "q" is silent.

That's the mantra of software developers everywhere. And, I believe it. Last
year I built a fixed header grid for my former employer which garnered a lot
of praise. It didn't have most of the requirements listed above; however, I
figured I could do it without too much pain. With jQuery and jQuery UI on my
side, how could I not get it done quickly?

I "finished" it in three fifteen work hour days. As it goes with a lot of
projects, I wrote the majority of the code during the first third and spent
the next two-thirds of the project time tweaking the script and style for it
to meet my expectations.

This week I will dive into the details of creating [grijq](/grijq). I'll write
about the main challenges of creating it. The menu reads (and I hope it makes
your mouth water)

Tuesday
: Designing the scrolling of a fixed-header grid

Wednesday
: Get column resizing working on big tables

Thursday
: Navigating the grid with the keybaord

Friday
: Creating a pluggable editor system

Remember, **grijq** does not promise feature parity with the grids listed
above. I designed **grijq** as an eventing and interaction layer. It should
tie into a rendering system. I like the cleanliness of separating those two
concerns: one thing renders HTML and another handles the interactivity with
the user. In the
[Taligent MVP](http://www.wildcrest.com/Potel/Portfolio/mvp.pdf) pattern,
**grijq** acts as an interactor between the view (the browser) and the
presenter (in my case, **knockout.js**).
