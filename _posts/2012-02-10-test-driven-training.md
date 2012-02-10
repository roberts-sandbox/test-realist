---
layout: post
title:  Test-Driven Training
tags:   mentoring

synopsis: In which I talk about the training I led, today.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----
Remember back on Monday when I said that I had to fill my week
[with typing other stuff](/2012/02/06/busy-at-work.html)? Well, I did. I
mostly finished my leave-behind training manual (67 pages, so far) and started
on the presentations for the three-day course to help the employees joining
the new development stream. And, then, yesterday afternoon, a Muse inspired me
to throw away the presentations.

You see, I need to train some people to code in a new language. I need to
train them to understand an alien, home-grown platform. I need to train them
to abandon certain "best practices" for "best practices" that exercise the
new platform efficiently and maintainably. I need to train them on the
customized versions of source control, code review workflow, deployment,
new design patterns, home-grown IDE, all in a scripting language. In three
days.

These are developers that have, for the past five years or more, lived in the
Subversion + C# + Visual Studio + NUnit world. The safe and warm arms of
statically-typed systems have enveloped them for so long, they seemed like
newborns looking at a new world.

Not looking good. No, sir.

But, that Muse, she inspired me. She caused me to remember a conversation that
I had with **bray** and **philipmat** about six months ago. I said to them,
"Wouldn't it be cool if we could have a tutorial that showed a unit test that
I could make pass? That would teach me a lot about a language or framework
without having to endure badly-written prose."

So, away with the presentations! Away with the slides and code samples that I
would type and others would mimic. I would keep them engaged with writing
code to make unit tests pass!

I sat down at my MBP, started a Windows 7 VM, clicked the Visual Studio icon,
and built a little interface to guide the attendees through a series of unit
tests that I would augment with instruction.

TEST-DRIVEN TRAINING!

And, I have to say, I think I had a hit. No one nodded off. They didn't check
their smart phones. They didn't doodle.

Instead, they typed. They learned through thinking and applying rather than
listening and remembering. They can take the unit test presenter and work
through them like katas.

For every code presentation that I now have to do where I need to teach people
about something, I will now lead test-driven training. It's really awesome.

![start](/img/tdt-start.png)

![test](/img/tdt-test.png)

![message](/img/tdt-message.png)