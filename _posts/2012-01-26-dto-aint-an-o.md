---
layout: post
title:  Interlude - DTOs Ain't No O
tags:   architecture

synopsis: In which I express my dismay with nomenclature.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

Yesterday, **ayende** posted some blog about some code with which he didn't
agree. I read it with apathetic eyes. I really go there to read the comments
that people leave on his blog. Opinionated people draw opinionated readers.
The post, about
<abbr title="Command Query Responsibility Segregation">CQRS</abbr> in some
example app written once-upon-a-time, had people chattering like squirrels
since CQRS has become a buzz-worthy thing. (I call it the Fowler Effect.)

About 20 comments in, someone wrote something about
<abbr title="Data Transfer Object">DTO</abbr>s. It goes like this.

> This kind of separation \[CQRS\] sounds good for me, because you can design
> queries based on UI, with specific DTOs, while I can design commands to
> affect my domain model, via write side of it, based on user tasks.

I don't think this guy wrote anything offensive; it has a certain value of
insight. I realized while reading it, though, that I can no longer abide the
term "DTO".

For those of you not in the know, a Data Transfer Object provides a typed
representation for passing information between two layers of your application.
Those layers can physically run in the same process or across the world. A
DTO supplies a message contract. Also, we can't bother most developers to
figure out efficient serialization and deserialization algorithms for their
objects. They'd rather use the ones provided by whatever their specific
runtime or platform has in their communication packages.

I really dislike the "O" in "DTO." I refer you to my
[first](/2011/12/06/ramble.html) and [second](/2011/12/07/ramble.html) posts
where I wheedle on about object-oriented design and falafel. The sum total of
those posts: *Classes define behavior. Objects perform it.*

In object-oriented programming, we have a mantra, "Tell. Don't ask." We have
that mantra because our objects, defined by classes, have *behavior!*

A Domain Transfer Object has *no behavior*. Thus, they do have the defining
characteristic of an *object*.

From now on, I will call them "DT-NO"s: Data Transfer Non-Objects. Also, I
think "ditno" sounds kind of funny.
