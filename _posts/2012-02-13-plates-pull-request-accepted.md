---
layout: post
title:  A Little Open Source Amidst the Training
tags:   foss

synopsis: In which I talk about my small contribution to flatiron/plates.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

Today, more training, more test-driven training. The group of attendees
really seems to enjoy it. Yay! Because of this, I didn't really work on
anything else non-work related, except...

...I ran into a couple of problems when using
[flatiron/plates](https://github.com/flatiron/plates). You may recall my
[series](/2012/01/11/get-to-know-flatiron.js-by-building-a-todo-app-story-1.html)
[of](/2012/01/12/get-to-know-flatiron.js-by-building-a-todo-app-story-2.html)
[articles](/2012/01/12/get-to-know-flatiron.js-by-building-a-todo-app-story-3.html)
[on](/2012/01/12/get-to-know-flatiron.js-by-building-a-todo-app-story-4.html)
[flatiron](/2012/01/12/get-to-know-flatiron.js-by-building-a-todo-app-story-5.html)
that I posted about a month ago and the follow-up
[update](/2012/01/14/plates-update-for-todo-list.html) that I posted because
of the **plates** reëngineering. I found what I considered a bug. It goes like
this.

Given the HTML template

{% highlight html %}
<input name="method" value=""><input name="id" value="">
{% endhighlight %}

and the data

{% highlight javascript %}
var data = {
  method: 'DELETE',
  id: 7
};
{% endhighlight %}

then I would expect the following **plates** binding

{% highlight javascript %}
var map = Plates.Map();
map.where('name').is('method').use('method').as('value');
map.where('name').is('id').use('id').as('value');
{% endhighlight %}

to result in

{% highlight html %}
<input name="method" value="DELETE"><input name="id" value="7">
{% endhighlight %}

However, **plates** ignored the matching where/is clause in the binding code
and would just bind will-nilly such that the code above actually resulted in

{% highlight html %}
<input name="method" value="7"><input name="id" value="7">
      <!--                  ^
            incorrect value | -->
{% endhighlight %}

I went poking around the **plates** code, found the problem, wrote a test,
fixed the problem, ran the tests, ran the performance tests, optimized the
code, ran the performance tests, and felt generally happy about it all.

Then, I saw a request in the
[issues list](https://github.com/flatiron/plates/issues) about creating 
attributes if they don't exist and realized what I just implemented would make
that solution trivial. So, I went ahead and included that fix in my code.

Openend a pull request.

Forgot all about it.

Last week, I got a message from the **plates** developers. They had made some
changes to their master branch which made my pull request un-mergeable. They
asked for a refresh. I pulled the updates from their master into mine on
Saturday and forgot about it.

On the bus ride into work, this morning, I didn't have any important code to
write. Just poking around my local repos, I remembered that merge. Update.
Move some content to new files. Run tests. Shazam! Everything worked.

Pushed the code while at Starbuck's.
[hij1nx](http://resume.github.com/?hij1nx)
merged my pull request around 3pm.

Yay!

Contributing never felt so good.
