---
layout: post
title:  Interesting Browser Detection
tags:   javascript

synopsis: Look at window.HTMLElement
---
Often, I need to change the way I apply some CSS due to the different box
models that browsers employ. Some include padding, some borders, some other
stuff in their calculations of widths during their layout phase. I stumbled
across this interesting way of detecting the browser that the visitor to your
site has decided to use.

{% highlight javascript %}
(function() {
  var htmlElementName = Object.prototype.toString.call(window.HTMLElement);

  isIE8      = htmlElementName === '[object Object]';
  isFF13     = htmlElementName === '[object DOMPrototype]';
  isChrome19 = htmlElementName === '[object Function]';
  isSafari5  = htmlElementName === '[object HTMLElementConstructor]';
})();
{% endhighlight %}

Neat, eh?

I put the version numbers on those `isXXX` variables because those're the
versions that I used to test those values. They might work for other versions,
too.

If you use this trick and find a different value or even the same value, then
please post your discovery on this page and we can compile a list of very
easy-to-use tests for browser detection!
