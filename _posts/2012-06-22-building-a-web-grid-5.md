---
layout: post
title:  Building a Web Grid - Part 5
tags:   html, jquery

synopsis: In which I disucss the editors in grijq.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

I wanted to have a "pluggable" editor system for the grid so programmers
could customize the widgets that appear in the cell when editing begins. This
post discusses how to create a custom editor and use it in
[grijq](http://curtis.schlak.com/grijq).

## The structure of an editor

An editor for **grijq** has the following form:

{% highlight javascript %}
var myEditor = {
  'edit': function(value, options) {
    // return a jQuery-wrapped DOM element
    //   -or-
    // return an object like
    // {
    //   element: jQuery-wrapped DOM element,
    //   afterAppend: function() {
    //     // run after the DOM element appended
    //     // to grid cell
    //   }
    // }
  },
  'unedit': function(input) {
    // return value here
  }
}
{% endhighlight %}

You then pass it as an option to the `grijq` widget when you create it:

{% highlight javascript %}
$('#some-table').grijq({editors: {'mytype': myEditor}});
{% endhighlight %}

And make sure that you've marked the column header with the key of your custom
editor:

{% highlight html %}
<table id="some-table" width="100">
  <colgroup>
    <col width="100">
  </colgroup>
  <thead>
    <tr>
      <th data-type="mytype">Some value</th>
    </tr>
  </thead>
  <tbody>
{% endhighlight %}

Or pass in the type to the cols parameter of the `grijq` widget:

{% highlight javascript %}
$('#some-table').grijq({
  cols: [{'type': 'mytype'}],
  editors: {'mytype': myEditor}
});
{% endhighlight %}

## A custom editor that displays a &lt;select&gt;

I don't have much use for &lt;select&gt;s. However, you may like them. Let's make a
custom editor that creates a &lt;select&gt; that contains shirt sizes. 

{% highlight javascript %}
var shirtSizeEditor = {
  'edit': function(value, options) {
    var template = '<select>' +
                      '<option>Large</option>' +
                      '<option>Medium</option>' +
                      '<option>Small</option>' +
                    '</select>';
    var select = $(template)
      .val(value)
      .width('100%')
      .keydown(function(e) {
        switch(e.keyCode) {
          case $.ui.keyCode.UP:
          case $.ui.keyCode.DOWN:
            e.stopPropagation();
        }
      });
    var wrapper = $('<div></div>').append(select);
    return {
      element: wrapper,
      afterAppend: function() {
        select.focus();
      }
    };
  },
  'unedit': function(input) {
    return input.val();
  }
};
{% endhighlight %}

Now, we'll create a table that uses that.

{% highlight html %}
<table id="some-table" width="300">
  <colgroup><col width="300"></colgroup>
  <thead>
    <tr>
      <th data-type="shirt-size">Shirt Size</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Large</td></tr>
    <tr><td>Medium</td></tr>
    <tr><td>Small</td></tr>
    <tr><td>WTF?!?!?</td></tr>
  </tbody>
</table>
{% endhighlight %}

Then, we create the grid with **grijq**.

{% highlight javascript %}
$('#some-table').grijq({
  width: 316,
  editors: {
    'shirt-size': shirtSizeEditor
  }
});
{% endhighlight %}

And you get this handsome devil.

<table id="some-table" width="300">
  <colgroup><col width="300" /></colgroup>
  <thead>
    <tr>
      <th data-type="shirt-size">Shirt Size</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Large</td></tr>
    <tr><td>Medium</td></tr>
    <tr><td>Small</td></tr>
    <tr><td>WTF?!?!?</td></tr>
  </tbody>
</table>

<link rel="stylesheet" href="/css/jquery-ui-1.8.21.css" />
<link rel="stylesheet" href="/css/jquery.ui.grijq-0.2.4.css" />
<script src="/scripts/jquery-1.7.2.min.js"> </script>
<script src="/scripts/jquery-ui-1.8.21.min.js"> </script>
<script src="/scripts/jquery.ui.grijq-0.2.4.js"> </script>

<script>
  var shirtSizeEditor = {
    'edit': function(value, options) {
      var template = '<select>' +
                        '<option>Large</option>' +
                        '<option>Medium</option>' +
                        '<option>Small</option>' +
                      '</select>';
      var select = $(template)
        .val(value)
        .width('100%')
        .keydown(function(e) {
          switch(e.keyCode) {
            case $.ui.keyCode.UP:
            case $.ui.keyCode.DOWN:
              e.stopPropagation();
          }
        });
      var wrapper = $('<div></div>').append(select);
      return {
        element: wrapper,
        afterAppend: function() {
          select.focus();
        }
      };
    },
    'unedit': function(wrapper) {
      return wrapper.children().val();
    }
  };
  $(function() {
    $('#some-table').grijq({
      width: 316,
      editors: {
        'shirt-size': shirtSizeEditor
      }
    });
  });
</script>
