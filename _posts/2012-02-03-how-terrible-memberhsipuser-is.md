---
layout: post
title:  MembershipUser SchmembershipUser
tags:   ood

synopsis: In which I rant very briefly about my dislike for System.Web.Security.MembershipUser.
---
Yeah, it's bad. Really bad.

[bray](http://bryanray.net) and I just spent a couple of hours looking at the
authentication model in ASP.NET MVC.

&lt;blegggh/&gt;

I threw up a little in my mouth. Sorry. I'm okay.

This class from which you *must inherit* for authentication to work just
makes my heart sink. If nothing else, Microsoft, please just provide hooks on
which to hang my authentication. Then, build your stuff atop that.

I'm a big boy and understand how to write my own authentication and
authorization services. Really, I do. And, thanks for providing means by which
to authenticate against Active Domain and relational databases. I'll make
sure to use them in "enterprise" systems.

But, for my home-grown system, for this software that I want to write here,
for the *awesome* product that **bray** gets to help create for his energetic
start-up, just give us tracks on which we can run our own locomotives.

Choo choo choo choo!
