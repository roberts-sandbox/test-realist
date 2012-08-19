---
layout: post
title:  POSTing a Bad Resource to a "ReST API"
tags:   rest

synopsis: A brief discussion on failing to create new things in ReST
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

Over on Twitter, @philipmatix just sent these tweets to me.

<blockquote class="twitter-tweet"><p>. <a href="https://twitter.com/realistschuckle"><s>@</s><b>realistschuckle</b></a> in a ReSTful API how do you know what you know what you need to POST to create a new entity? Documentation?</p>&mdash; Philip Mateescu (@philipmatix) <a href="https://twitter.com/philipmatix/status/237190399343611904" data-datetime="2012-08-19T14:12:52+00:00">August 19, 2012</a></blockquote>
<blockquote class="twitter-tweet"><p>. <a href="https://twitter.com/realistschuckle"><s>@</s><b>realistschuckle</b></a> POST with an invalid payload and expect the server to reply with 400 (or 422) and a sample of a valid payload?</p>&mdash; Philip Mateescu (@philipmatix) <a href="https://twitter.com/philipmatix/status/237191286128513024" data-datetime="2012-08-19T14:16:24+00:00">August 19, 2012</a></blockquote>

My response would take to long to break up over a multitude of Twitter-sized
messages, so I'll put it here.

## The Purist's Perspective

First, the concept of a "ReST API" has some conflicting semantics to the name,
kind of like the phrase "climb down". A ReST application has one or more entry
points (start URIs) and hyperlinks to allow the user to navigate (change
states) in the application. Therefore, a consumer of the application should
never have arrived at a point in an application where a POST would not provide
the correct format for the resource.

In the context of a Rails app, a purist's perspective would demand that the
user agent have GETted the `controller#new` action to get the representation
of the resource before POSTing to `controller#create`.

ReST really offers no guidance for the problem about which @philipmatix has
posed.

## The Less Literal-Minded

Of course, we don't live in that world.
[Everyone](https://dev.twitter.com/docs/api)
[has](http://developer.netflix.com/docs/REST_API_Conventions)
[ReST](https://www.dropbox.com/developers/reference/api)
[APIs](http://developer.force.com/REST).
These APIs have documentation that describe the expected format of a resource
and to which URI a consumer should POST that representation. Therefore, we're
not really talking about ReST, anymore. That's why @philipmatix's question makes
a lot of sense, in this muddied landscape.

With that in mind, let's try to figure out something similar and use it as a
basis. Further confusing the world with more errors can only make this problem
worse.

He asks about HTTP status code 422, defined in
[RFC 4918](http://tools.ietf.org/html/rfc4918#section-11.2). It defines 422
as

> The 422 (Unprocessable Entity) status code means the server understands the
> content type of the request entity (hence a 415(Unsupported Media Type) status
> code is inappropriate), and the syntax of the request entity is correct (thus a
> 400 (Bad Request) status code is inappropriate) but was unable to process the
> contained instructions. For example, this error condition may occur if an XML
> request body contains well-formed (i.e., syntactically correct), but
> semantically erroneous XML instructions.

That sounds a lot like what we need. Admittedly, the authors defined the status
code for the WebDAV protocol. But, why not use it? It seems reasonable to me.

The 422 response does not describe a payload, so providing the correct
"definition" of the resource pushes the meaning of the code. But, what the hell,
right?

## Further Thoughts

ReST does not make APIs. ReST defines an architecture by which to construct an
application.

The so-called ReST APIs hawked by vendors do not actually represent ReST.
Instead, they really represent *resource-based* APIs. We need a protocol to fill
that need, it seems.

Why not WebDAV? Oh, because it's for files. Duh.

Well, why not adapt it? I mean, we *know* that the end of a URI points to a
*resource*. That could be a file. It could be a database entry. It could be any
old thing. Do we really need to adapt it?

If we look at the [WebDAV RFC](http://tools.ietf.org/html/rfc4918), we see in
the introduction that it supports Web authoring. Isn't that what we're doing in
this example? In its loosest sense, these so-called ReST APIs allow users to
"author" new content.

So, why aren't we really using WebDAV for that?

Oh, probably because WebDAV has an XML syntax. And, XML smells bad.


<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
