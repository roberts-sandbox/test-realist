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

# Follow Up

After reading this post, @philipmatix and I exchanged a brief set of emails that
help better illuminate this subject. Here they are.

---

## @philipmatix writes:

So here's what I didn't quite get:

> A ReST application has one or more entry points (start URIs) and hyperlinks to
> allow the user to navigate (change states) in the application."

Let me try to butcher that beautiful wording in an example. Let's go with HTML
as media format.

Say you just did `GET /foo/5`:

    <h1>Foo Five</h1>
    <a href="bars">Go here</a> to see my Bars.

Alright, so you go to `GET /foo/5/bars`. But there are no Bars, so the server
replies with:

    Here are all Bars for <a href="/foo/5">Foo Five</a>:
    <ol>
    </ol>

> Therefore, a consumer of the application should never have arrived at a point
> in an application where a POST would not provide the correct format for the
> resource.

So what should the server have replied with to provide the client with the
knowledge required to create a new Bar?

And I guess related to that, if the server elects to send the client an
incomplete representation (of a comprehensive entity), how would the client know
how to create an entity with the missing part.

I'm thinking if the server replies with this:
    GET /foo/5
    Accept: text/javascript

    { "Name": "Foo Five",
     Bars: [],
     Baz: null
    }

Leaving aside that JSON is not truly ReSTful because it doesn't provide links
(at least not explicitly), how would the client know what

1. a new Bar would look like?
2. a new Baz would look like?
3. if the server doesn't send in a Baz because it's null (JSON.Net has an
   option, default I think, to not send null properties at all) how would the
   client ever know that Foo has a Baz?

---

## to which I reply:

I understand your confusion and apologize that I did not make my post more
clear.

Let's say that you did `GET /foo/5/bars`. If the user should have an opportunity
to create a bar, then a reply might look like this:

    Here are all Bars for <a href="/foo/5">Foo Five</a>:
    <ol>
    </ol>
    You can <a href="/foo/5/bars/new">create a new bar, too!</a>

Regarding the JSONy thing, yeah, that's why JSON doesn't do ReST justice. You
just need more info for self-description like
[JSON Schema](http://json-schema.org). Or, you define a new MIME type that uses
JSON as a medium of encoding but the MIME type has semantics regarding how it
gets processed in the application (i.e., your JavaScript.)

In the absence of those alternatives, the answers to the questions that you pose
at the end of your email:

1. It wouldn't know what a new Bar looks like.
1. It wouldn't know what a new Baz looks like.
1. It wouldn't know that a Baz exists.

---

## to which @philipmatix replies:

So what would `GET /foo/5/bars/new` look like?

---

## to which I reply:

Regarding `/foo/5/bars/new`

In a browser browsing mode (`Accept: text/html`), it may look like a form.

In a JSON call (`Accept: application/json`), it may follow the JSON schema spec.

In a computer-to-computer XML call (`Accept: text/xml`), it may return an XML
schema.

In a text-only mode (`Accept: text/plain`), it may look like an instruction form
on how to call customer service to get the thing added.

In an image mode (`Accept: image/png`), it may return 406 with the list of
`text/html`, `application/json`, `text/xml`, and `text/plain`.

The first three entries would have a `POST` instruction to `/foo/5/bars` for the
*create new resource* action. Of course, the server that receives the `POST`
will have to handle the available formats `text/html`, `application/json`, and 
`text/xml` as viable inputs for the *create new resource* action.

<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
