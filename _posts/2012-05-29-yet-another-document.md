---
layout: post
title:  Yet Another Document and a knockout.js Bug
tags:   job

synopsis: A small post excusing my small post and a little bug in knockout.js.
---
I have one more document to write for my current client. Because of that, I
really just don't have time to write, today, in this blog. Not only that, but
I don't really have anything interesting to write. Except this thing I found
with knockout.js.

It seems that knockout.js on IE8 strips any trailing white space between a
data-bound tag and further text. For example, given the markup:

{% highlight html %}
<div>
  My humorous substitution <span data-bind="text: verb27"></span> away with
  a <span data-bind="text: noun11"></span>.
</div>
{% endhighlight %}

renders as the following in IE8.

{% highlight html %}
<div>
  My humorous substitution <span data-bind="text: verb27">ran</span>away with
  a <span data-bind="text: noun11">spoon</span>.
</div>
{% endhighlight %}

And you can see the trailing whitespace of the first ``span``, the space
between the end tag and the word "away," disappears. I haven't had time to
hunt down the bug or even report it.

Maybe this weekend.
