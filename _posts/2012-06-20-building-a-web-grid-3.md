---
layout: post
title:  Building a Web Grid - Part 3
tags:   html, jquery

synopsis: In which I disucss the column resizing in grijq.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

**Update**: Last night I added a new example for
[grijq](http://curtis.schlak.com/grijq) that demonstrates its integration with
knockout.js. You can find it at
[Simple knockout.js integration](http://curtis.schlak.com/grijq/examples/simple-knockout-integration.html).

I found that implementing column resizing really took a little code and some
care with respecting the layout of the header contents. The following code
listing shows the extracts of the JavaScript that control column resizing.

{% highlight javascript linenos %}
var mover = ie? '<span class="mover ie">.</span>'
              : '<span class="mover">.</span>';
grijq.element
  .children('thead')
    .find('th')
      .append(mover)
      .wrapInner('<div></div>')
    .end();

$('.mover', grijq.headerTable).draggable({
  axis: 'x',
  helper: function() {
    grijq.widget.append(grijq.columnResizer);
    grijq.columnResizer
      .height(grijq.widget.height() - 16)
      .css('z-index', 1000);
    return grijq.columnResizer.show()[0];
  },
  stop: function(event, ui) {
    var th = $(this).closest('th');
    var pad = parseInt(th.css('padding-left')) + 
              parseInt(th.css('padding-right'));
    var offset = ui.position.left - ui.originalPosition.left;
    var index = th.prevAll().length;
    var col = $(grijq.cols.get(index));
    var newColWidth = offset + parseInt(col.prop('width'));
    newColWidth = Math.max(minWidth, newColWidth);
    newColWidth = Math.max(pad + 5, newColWidth);
    col.prop('width', newColWidth);
    var newHeaderWidth = Math.max(minWidth, newColWidth - 1 - pad);
    $(th).width(newHeaderWidth);
    var newTableWidth = offset + parseInt(grijq.element.prop('width'));
    newTableWidth = Math.max(minWidth, newTableWidth);
    grijq.element.prop('width', newTableWidth);
    grijq.element.css('width', newTableWidth);
  }
});
{% endhighlight %}

Lines 1 - 8 put the mover into each header cell. Nothing special there.

Line 10 attaches the jQuery UI `draggable` to each of the movers constraining
the movement of the mover to the x-axis. The `stop` helper function on line 12
reattaches and styles the mover helper to show the height of the grid.

The real meat exists in the `stop` function starting on line 19.

Line 20 gets the actual header cell whose width we'll modify.

Line 21 calculates the horizontal padding for the header so we can subtract it
from the overall width of the cell.

Line 23 determines the change in position that the mover went through.

Line 24 gets the index of the header cell.

Line 25 gets the `col` tag associated with the column.

Lines 26 - 28 calculate the new column width, ensuring that it does not get
thinner than a couple of minimum widths that ensure that IE continues to work
correctly.

Line 29 sets the `col` tag's `width` property to the newly calculated width.

Line 30 calculates the width of the header cell with respect to the padding
of the cell.

Line 31 sets that new width.

Lines 32 and 33 calculate the new table width ensuring that it, too, does not
get thinner than a specific minimum width.

Lines 34 and 35 set the width of the table both in the `width` property of the
table and the "width" entry in the table's `style` attribute. I have to do
this because the `width` property ensures that the table maintains its width
for values larger than its container. The "width" entry in the table's `style`
attribute ensures that the table maintains its width for values smaller than
its container.

Booyah!

Up next in tomorrow's blog, I'll discuss how I got focusing to work on the
grid and navigate the cells with the keyboard.
