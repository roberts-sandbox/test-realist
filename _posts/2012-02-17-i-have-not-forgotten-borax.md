---
layout: post
title:  Back to BORAX
tags:   foss

synopsis: In which I outline my current development plans for BORAX.
---
Ok, things have started to slow down in my personal and professional life. It
seems that I have time, again, to work on BORAX.

And there was much rejoicing. "yay."

I started the changes, this morning, with creating some other files for
<abbr title="BORAX In Client">BORIC</abbr>. Then, I added
[jake](https://github.com/mde/node-jake.git) as a development dependency.
Finally, I added a script to the BORAX package to build the
**borax-in-client.js** file. I did this to make the size of the files on which
I work more manageable. I'll probably get some EcmaScript minifier as part of
the build process, too, for a "production" build.

With the next volley of work, I'll make the state of the current application
a first-order idea for BORIC. Then, I'll have BORIC wire transitions found in
the current rendering (if possible) and provide hooks for dynamic state
transitions engineered from any code-on-demand-driven logic.

That shoud make BORIC pretty darn usable.

Then, I'll switch back over to <abbr title="BORAX In Server">BORIS</abbr> and
get some convenience functions to serve the new convenience types expected by
BORIC for node.js and, maybe, ASP.NET MVC, if I remember how to write code for
that framework. &lt;wink /&gt;

Finally, I'll head back over to BORIC to implement some templating mechanisms
for Knockout.js and plates. With all of that in place, BORAX should provide a
good enough stack to release as an alpha version. At that point, as I wrote in
a previous article, I'll use BORAX to build my novelty excuse generation site.

If you notice any holes in this development plan, leave a note so I
don't miss out on anything.