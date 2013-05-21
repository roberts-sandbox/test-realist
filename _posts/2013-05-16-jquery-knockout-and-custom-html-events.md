---
layout: post
title:  jQuery UI, knockout.js, and Custom HTML Events
tags:   javascript, jquery, jquery ui, knockout.js

synopsis: In which I reveal a solution to the fundamental problem of unifying the libraries.
---
Ok, so, I'm a purist. I like things to do their job, do it well, and not reach
beyond their boundaries of functionality. In this case, I refer to
[jQuery UI](http://jqueryui.com) and [knockout.js](http://knockoutjs.com) as the
things under conideration.

I think that each library has a strength that I want to use in my Web
application:

<dl>
  <dt>jQuery UI</dt>
  <dd>Used to create widgets and handle events like mouse clicks.</dd>
  <dt>knockout.js</dt>
  <dd>
    Used to bind values from JavaScript objects to HTML nodes (and back again).
  </dd>
</dl>

## The problem

With that in mind, I encountered a "problem" with getting the two to work
seamlessly with one another specifically around using the
[jQuery UI Datepicker](http://jqueryui.com/datepicker/). When a user selects a
date from the calendar control, the `Datepicker` sets the value of the
associated `INPUT` node with the selected date.

How does it do that?

Well, it does it with JavaScript. Duh.

When jQuery sets the value of the `INPUT` node with JavaScript, the browser does
not fire the `onchange` event. Because of that, knockout.js has no idea that the
value changed. The view model does not get updated. Something becomes rotten in
the state of Denmark.

I don't want jQuery UI to know about my knockout.js bindings and the other way
around. I want the browser to act the way as if a user had typed into the field.

## The solution

My solution comes in the form of creating an event in the browser similar to the
one that the browser would raise if the user *had* typed in the value. I want to
fire an `onchange` event for that `INPUT` node. Turns out that the browsers can
do that. Of course, it depends on the browser for the specific implementation.
(Yes, I'm looking at you, Internet Explorer!)

First, I want the `Datepicker` to fire the event when the user selects a date.

{% highlight javascript linenos %}
$('input.date')
  .datepicker({
    onSelect: function() {
      evt.fire(this, 'change');
    }
  });
{% endhighlight %}

Now, where did that `evt.fire` method come from? I imported a module using
[RequireJS](http://requirejs.org) and bound it to the `evt` variable. Here's
what that module looks like.

{% highlight javascript linenos %}
define(function() {
  var o = {
    fire: null
  };
  
  // This is for old IE
  if(document.createEventObject && !document.createEvent) {
    o.fire = function(element, event) {
      var e = document.createEventObject();
      return element.fireEvent('on' + event, e);
    };
  } else {
    o.fire = function(element, event) {
      var e;
      try {
        // This is for new IE
        e = document.createEvent('HTMLEvents');
      } catch(e) {
        // This is for everyone else
        e = document.createEvent('UIEvents');
      }
      e.initEvent(event, true, true);
      return !element.dispatchEvent(e);
    };
  }

  return o;
});
{% endhighlight %}

Now, the `onchange` event fires when jQuery UI `Datepicker` sets the value of
the field and knockout.js now knows to get the newly-entered value.

## References

[document.createEventObject](http://msdn.microsoft.com/en-us/library/ie/ms536390%28v=vs.85%29.aspx)

[document.createEvent('HTMLEvents')](http://msdn.microsoft.com/en-us/library/ie/ff975304%28v=vs.85%29.aspx)

[document.createEvent('UIEvents')](https://developer.mozilla.org/en-US/docs/DOM/document.createEvent)