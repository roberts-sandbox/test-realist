---
layout: post
title:  Now in &lt;= IE8
tags:   site

synopsis: Holy moly!
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

I started showing my blog around to some folks. They had IE8 installed. Or,
IE7. I mean, WTF, right?

Well, here you go, users of the Internet that don't have a "good" browser. My
site now looks correct in your silly browser.

What did I do? I added the "Hey, IE! This is HTML5! Deal with it!" script. It
looks like this.

{% highlight javascript %}
(function(){
  var html5elmeents = "address|article|aside|audio|canvas|" +
                      "command|datalist|details|dialog|" +
                      "figure|figcaption|footer|header|" +
                      "hgroup|keygen|mark|meter|menu|nav|" +
                      "progress|ruby|section|time|video".split('|');
  for(var i = 0; i < html5elmeents.length; i += 1) {
    document.createElement(html5elmeents[i]);
  }
})();
{% endhighlight %}

IE will apply styles to the elements if you define them in the DOM as a
"valid" element.

I named the script "ie-sucks.js" and put it on the site.

Hope you enjoy, IE-users.

For those of you in Chrome and Firefox, you get the gold star, today.
