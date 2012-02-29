---
layout: post
title:  Toolkits and Frameworks
tags:   architecture

synopsis: Another rambling foray into my pedantic world of nomenclature.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

The entertaining and amusing **winky99** recently tweeted at me.

<blockquote style="border: 1px solid #CCC; padding: 4px;" class="twitter-tweet"><p>@<a href="https://twitter.com/realistschuckle">realistschuckle</a> Should we quit saying MVC when most implementations are MVP? Or agile when actually it is scrum? Communication &gt; purity</p>&mdash; Scott Stevenson (@winky99) <a href="https://twitter.com/winky99/status/174497998523478017" data-datetime="2012-02-28T14:15:39+00:00">February 28, 2012</a></blockquote>

This came from a comment that he made regarding a post by Rob Conery. So, I
went to look at Rob's article. I have to disagree with his assertion that
"communication > purity" primarily because precise communication is pure
communication. We develop specialized languages with unambiguous terms just so
we can communicate with one another clearly.

Since Rob sparked our short-lived debate, I went to look at Rob's site.

-----

[Rob Conery](http://wekeroad.com/) strikes an impressive figure. Take a look
at this guy. He's the dude in the lower-right corner.

![Rob Conery](http://wekeroad.com/images/robconery.jpeg)

He likes "Kitchen Nightmares." He has at least 18 GitHub projects. He has a
podcast named "This Developer's Life." Rob Conery is a rock star. So, why did
he have to write the following?

> A RESTful API is in the eye of the beholder

You know how I feel about REST, since I've
[written](http://localhost:4000/2012/01/19/fieldings-rest.html)
[at](/2012/01/23/hateoas-a-follow-up-to-rest-for-r33lz.html)
[length](/2012/01/24/borax.html)
[about](/2012/01/25/borax-2.html)
[it](/2012/01/27/borax-3.html). I think that such inaccuracy highlights the
difference between *computer scientists* and *computer programmers*.

I tend to live in the computer scientist camp, a practitioner and
theoretician, a measurer and mentor.

I think Rob lives in the computer programmer camp, a practitioner and
pragmatist, an implementor and mentor.

He thinks REST does not have a precise definition. I disagree. I'm sure that
he'd accuse me of adhering to a purist viewpoint. I'd accuse him of diluting a
term that has a specific meaning as outlined by its creator.

-----

I bring up this context of well-defined terms because I had a conversation
regarding the definitions of "framework" and "toolkit," recently. I think that
when most people say "framework" they really mean "toolkit."

For a while, I've used the terms very specifically. A "toolkit" helps me build
an application by providing reusable components to reduce the complexity of my
code. This includes socket libraries, UI widget libraries, and AJAX/DOM
scripts. A "framework" does most of the heavy lifting of the application and,
when I want specific behavior, I implement some well-defined contract and plug
it into the framework, somehow.

For something to act as a framework, I've borrowed Marc Clifton's three
dimensions of a framework:

__Wrappers__
: Wrappers exist to simplify access to complex technologies, reduces or
eliminates boiler-plate code, and increase flexibility of the management of
its entities through the open-close principle.

__Architectures__
: Architectures manage collections of discrete objects that implement a
specific and recognizable set of design elements.

__Methodologies__
: Methodologies enforce a consistent design and implementation approach by
preventing closely-coupled classes that ignore the single-responsibility
principle.

If you don't trust Marc because you think he's a little kooky, then how about
the apostolic Gang of Four. From _Design Patterns_:

> When you use a toolkit, you write the main body of the application and call
> the code you want to reuse. When you use a framework, you reuse the main
> body and write the code it calls.

> Not only can you build applications faster as a result, but the applications
> have similar structures.They are easier to maintain, and they seem more
> consistent o their users. On the other hand, you lose some creative freedom,
> since many design decisions have been made for you.

> If applications are hard to design, and toolkits are harder, then frameworks
> are hardest of all. ...Any substantive change to the framework's design
> would reduce its benefits considerably, since the framework's main
> contribution to an application is the architecture it defines. Therefore
> it's imperative to design the framework to be as flexible and extensible as
> possible.

How much more could you ask for an explanation for the difference between a
framework and a toolkit. So, I try to speak purely and without ambiguity when
I use those terms. I encourage you to separate the difference in your mind so
you know what you're writing, what you're using, and what you're talking
about.

There's nothing wrong about refining your craft and, part of that maturity,
should include sharpening your thoughts and words about the concepts that we
programmers use in our daily lives.