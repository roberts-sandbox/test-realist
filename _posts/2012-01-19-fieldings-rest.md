---
layout: post
title:  Fielding&apos;s REST for R33LZ
tags:   architecture

synopsis: In which I consider Roy Fielding's definition of REpresentational State Transfer.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

*Note:* this discussion primarily centers on the HTTP; REST over other
protocols exceeds the scope of this article.

\[Updated with link to **philipmat**'s blog.\]

My friend [philipmat](http://philipm.at) over at his blog 
has [published a novel approach](http://philipm.at/2012/0121/)
to building Web applications that use the server as a REST service and use the
browser as the controler and view in the MVC triumverate.

That idea, in and of itself, does not represent a "new idea." The fine
developers at [Sencha](http://extjs.org) and [Yahoo!](http://yuilibrary.com)
have already developed in-browser MVC frameworks that usually use some proxy
as the Model to fetch/write data stored on a server.

**philipmat** takes this at least one step further. And, in that step, I find
a favorable pace toward Roy Fielding's notion of
[REST](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm). First,
I'll go on about REST for a little while to cure any confusion about what REST
means. Then, I'll examine the step-toward-REST that **philipmat**'s proposal
makes to us.

## What is a URL?

Guess what? We have a standard which we can reference:
[RFC3986](http://www.ietf.org/rfc/rfc3986.txt) from the IETF.

That's long and boring. Let's do the Cliff's Notes version.

The set of all Uniform Resource Locators makes a proper subset of all Uniform
Resource Identifiers. In this post, I will use the terms interchangeably
though I really shouldn't.

A Uniform Resource Identifier uniquely names or locates a resource. In this
blog post, I don't care about the naming aspect of URIs, only the locating
aspect.

A Uniform Resource Locator points to a location that you can access with a
specified protocol, host, a (normally) hierarchical path, and some query crap.
It is not the thing at the location.

Once again,

> A Uniform Resource Locator points to a location. It is not the thing at the
> location.

To put that in concrete terms, when you type ``http://curtis.schlak.com`` in
your browser's address input field, that URL only tells your browser to go
look at that place for a resource. In this case, the HTML that you view in
the browser coupled with the values in the HTTP Response headers, comprises a
way to represent the resource located at that URL in the specific media type
of "text/html" as specified in the "Content-Type" Response header.

If you don't understand that distinction, then you won't understand Fielding's
idea of REST.

Two distinctly different URLs can point to the same resource. For example,
assume that you have a host named ``dictionary`` on your network. Then, you
could make a request for the resource located at ``http://dictionary/ischium``
which would go across the network like

> ``GET /ischium HTTP/1.1``  
> ``Accept: text/plain``

and receive a response like

> ``HTTP/1.1 200 OK``  
> ``Content-Type: text/plain``
>
> ``The curved bone forming the base of each half of the pelvis.``

If the ``dictionary`` also had a resource at
``http://dictionary/word_of_the_day`` and today the dictionary gods decided to
make that "ischium," then the request would go across the network like

> ``GET /word_of_the_day HTTP/1.1``  
> ``Accept: text/plain``

and you'd get the same representation of the resource located at
``http://dictionary/ischium``.

## Representational State Transfer - what it ain't

Any item in the following list does not mean REST:

* Rails, Merb, ASP.NET MVC
* Pretty URLs (http://host/:controller/:id/:action)
* Format from file extensions (.xml, .html, .json)
* The word "restful" in the description

Those don't mean that a RESTful API can't have any of those attributes. But
don't mistake those concepts as representing REST faithfully.

REST really means that you can go to a URI and get the entire representation
of the resource represented by that URI. An "entire" representation can mean
the HTML of an HTML document, the bits that make a Microsoft PowerPoint, or
an error. When I write "entire representation," I really mean that. A complete
REST implementation would mean that, for a given URI, I could receive multiple
representations of the resource for the same media type: a VIEW representation
with optional executable code, an EDIT representation with optional executable
code, and a REMOVE resource with optional executable code. Or, for that
matter, I could make a request for the resource and receive only executable
code that would know how to go about showing the resource and allowing
interaction.

### The "compromises" of Rails

The Ruby on Rails community has done the most for popularizing the concepts of
REST throughout the Web development ecosystem. Unfortunately, naïve developers
then think that the Rails Way means REST. It doesn't. But it does a really
good job at making compromises due to browser limitations.

### HTTP verb simulation

Your browser can GET a representation of a URL or POST some data to a URL, but
it cannot PUT to or DELETE the representation at a URL. It just won't form
HTTP requests with those verbs. So, Rails makes use of a magic form field to
specify PUTs and DELETEs when you POST that form to a Rails application. I
think that bridges the gap nicely until browser vendors remove the restrictions
on the types of HTTP requests their browsers can craft.

### Pretty URLs

Rails prides itself for "convention over configuration." It applies this
notion to its use of REST. REST does not specify any convention whatsoever.
You can write a RESTful service that has absolutely no conventional URLs;
you'd just find it hard to do that in Rails.

When a developer uses the ``resources`` or ``resource`` method in the Rails
routing file, the method generates a bunch of route matching logic that maps
a URL path and HTTP verb to the form ``/:controller/:id/:action`` which, in
turn, maps to a method on an object. That allows the developer to do things
quickly.

Pretty URLs illustrate only a subset of RESTful interactions with a server.

### Format file extensions

We know that two URLs can refer to the same resource. Therefore, the URLs
``http://host/fortune.json`` and ``http://host/fortune.html`` can refer to
the same resource and return different representations of that fortune, JSON
and HTML, respectively. Rails uses that interpretation of file extensions.

However, we could switch those around and REST would not care. You could ask
for ``http://host/fortune.html`` and receive a JSON representation. You could
go to ``http://host/fortune.cgi`` and receive an HTML representation.
So-called file extensions don't really mean anything in a URL; RFC writers
call everything after the host name *opaque*, which means that you and I
should not infer any semantic meaning from the combination of letters after
``http://host``.

Instead, REST allows metadata about the request and even metadata about the
metadata. In a perfect world, I could use the 
[Accept HTTP Request header](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.1)
to specify the kind of representations that I can use. Once again, though, the
browsers
[fail us in this regard] (http://www.gethifi.com/blog/browser-rest-http-accept-headers).

## philipmat's proposal

What does this dude have that others don't?

I think that **philipmat** has proposed a purer form of RESTful Web
applications than we've seen with other frameworks. For that matter, he hasn't
even proposed a framework, just the way that we should architect our Web
applications. It reads like a funnier version of Fielding's dissertation, but
with real-world technologies like "JavaScript" instead of abstract concept
phrases like "Code-On-Demand."

Combining code-on-demand and **philipmat**'s idea of how to architect Web
application really intrigues me. I think that it makes more sense than
other frameworks. Pure HTML. Pure JavaScript downloads to render resources.
Pure client/server interactions. Pure REST.

Kind of makes me itchy to write a new framework...
