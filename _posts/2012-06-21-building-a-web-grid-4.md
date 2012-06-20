---
layout: post
title:  Building a Web Grid - Part 4
tags:   html, jquery

synopsis: In which I disucss navigating grijq with the keyboard.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

I think this is the most interesting part of the grid. This feature required
two different things: the ability to focus on a grid cell and the ability to
capture navigation keys to move the selected cell.

## Focusing on a grid cell

It turns out that all you need to do in HTML to get focus on a non-form
element means that you apply a `tabindex` to it. Let's take a look at this in
practice. Look at this HTML.

{% highlight html %}
<style type="text/css">
.tabindex-example span {
  height: 100px;
  display: inline-block;
}
.tabindex-example .orange {
  background-color: orange;
  width: 100px;
}
.tabindex-example .purple {
  background-color: purple;
  width: 150px;
}
.tabindex-example .yellow {
  background-color: yellow;
  width: 200px;
}
</style>
<div class="tabindex-example">
  <span tabindex="0" class="orange">&nbsp;</span>
  <span tabindex="0" class="purple">&nbsp;</span>
  <span tabindex="0" class="yellow">&nbsp;</span>
</div>
{% endhighlight %}

And, here it is in the browser. Click on the orange rectange. Once you see the
highlight around the element, press the TAB key and watch that focus move to
the purple. Then, after another TAB key press, the highlight will move to the
yellow element.

<style type="text/css">
.tabindex-example span {
  height: 100px;
  display: inline-block;
}
.tabindex-example .orange {
  background-color: orange;
  width: 100px;
}
.tabindex-example .purple {
  background-color: purple;
  width: 150px;
}
.tabindex-example .yellow {
  background-color: yellow;
  width: 200px;
}
</style>
<div class="tabindex-example">
  <span tabindex="0" class="orange">&nbsp;</span>
  <span tabindex="0" class="purple">&nbsp;</span>
  <span tabindex="0" class="yellow">&nbsp;</span>
</div>

That addressses the problem with how to get the TAB key to stop on one of the
grid cells. The real problem comes with how to apply tabindexes on the cells
of the grid. On big tables, applying the `tabindex` property on each of the
cells or prerendering them leads to *really slow* grid render and response
times. So, **grijq** takes the "apply a `tabindex` on demand" approach. For
example, when a cell receives focus, then it applies a `tabindex="0"` to each
of the cells in that row.

{% highlight javascript %}
cell.parent().children().prop('tabindex', '0');
{% endhighlight %}

That happens throughout the code in different ways, when the user interacts
with the different portions of the grid. This is the least amount of
interaction that guarantees smooth movement horizontally with the TAB key
presses. When the focus gets to the end or beginning of the row, then it
also applies it to the next or previous row, respectively.

{% highlight javascript %}
if(cell.next().length === 0) {
  var nextRow = row.next();
  nextRow.children().prop('tabindex', '0');
} else if(cell.prev().length === 0) {
  var previousRow = row.prev();
  previousRow.children().prop('tabindex', '0');
}
{% endhighlight %}

## Key navigation

Key navigation is mundane, lower level programming that, while makes the user
very happy, kind of sucks to implement. The jQuery UI library even defines
constants that we can use in capturing the key presses.

{% highlight javascript %}
grijq.element.keydown(function(e) {
  switch(e.keyCode) {
    case $.ui.keyCode.LEFT:
      target.prev().focus();
      e.preventDefault();
      break;
    case $.ui.keyCode.RIGHT:
      target.next().focus();
      e.preventDefault();
      break;
    case $.ui.keyCode.UP:
      var index = target.prevAll().length + 1;
      var tr = target.closest('tr').prev();
      tr.children().prop('tabindex', '0');
      $(':nth-child(' + index + ')', tr).focus();
      e.preventDefault();
      break;
    case $.ui.keyCode.DOWN:
      var index = target.prevAll().length + 1;
      var tr = target.closest('tr').next();
      tr.children().prop('tabindex', '0');
      $(':nth-child(' + index + ')', tr).focus();
      e.preventDefault();
      break;
  }
});
{% endhighlight %}

Very simple, really, once **grijq** gets the `tabindex`es into place. If we
stop here, we have a simple and relatively elegant solution. Unfortunately,
as we find out tomorrow, making cells editable completely screws with this
simple solution. When we allow users to type into an `input` element, we
introduce another `tabindex`-ed element into the mix which messes up this
code above. But, I'll leave that until tomorrow.

Head on over to [the project page](http://curtis.schlak.com/grijq) and check
out the examples.
