---
layout: post
title:  "HATEOAS: A Follow-Up to Rest for R33lZ for BORAX"
tags:   architecture

synopsis: In which I take my friend's advice to engage in more pedagogy about REST, and the New Web programming style BORAX.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

A friend, @[optimizedchaos](https://twitter.com/#!/optimizedchaos/), over on
Twitter, recommended that I
[write an entry here to address HATEOAS](https://twitter.com/#!/optimizedchaos/status/160737498622984193).

Agreed. Though, I think the acronym, itself, consists of an unfortunate
combination of letters in the English language, I present

## Hypermedia as the Engine of Application State (HATEOAS)

The term HATEOAS comes from a post that Dr. Roy T. Fielding (inventor of
REpresentation State Transfer) posted on 20 Oct 2008 under the title
[REST APIs must be hyptertext-driven](http://roy.gbiv.com/untangled/2008/rest-apis-must-be-hypertext-driven).
I encourage you to click that link and read the post and the comments. Really,
you should. Because, that link, that hypertext link and its associated
functionality in the browser, represents a change in the state of the
application in your browser, right now.

Clicked it? Good. Did you really? Are you lying? No? Ok. I trust you.

Dr. Fielding makes a series of very good points about REST and the way it
works. For those of you that had trouble with understanding his
[dissertation](http://www.ics.uci.edu/~fielding/pubs/dissertation/top.htm) or
had trouble with understanding the precision of his points, let me try to help
you come to a deeper understanding of REST. And, so the pedagogy begins.

### A REST API should not be dependent on any single communication protocol,

> though its successful mapping to a given protocol may be dependent on the
> availability of metadata, choice of methods, etc. In general, any protocol
> element that uses a URI for identification must allow any URI scheme to be
> used for the sake of that identification. \[Failure here implies that
> identification is not separated from interaction.\]

If you read my [most recent post about REST](/2012/01/19/fieldings-rest.html),
then you know that a <abbr title="Uniform Resource Locator">URL</abbr> can
have the form with some other junk that doesn't matter for this discussion:

> *protocol* ``':' '/' '/'`` *authority* *path*

For example, when you came to this page, your Web browser parsed the URL in
the address bar to the values

**protocol**: ``http``  
**authority**: ``curtis.schlak.com``  
**path**: ``/2012/01/23/hateoas-a-follow-up-to-rest-for-r33lz.html``

which ended up as an <abbr title="HyperText Transfer Protocol">HTTP</abbr>
request with, at the minimum, the content

{% highlight bash %}
GET /2012/01/23/hateoas-a-follow-up-to-rest-for-r33lz.html HTTP/1.1
Host: curtis.schlak.com
{% endhighlight %}

Now, if Dr. Fielding ever finished his
[WAKA](http://en.wikipedia.org/wiki/Waka_%28protocol%29) protocol, then he
should have the ability to replace the "http" with "waka" and still have the
ability to access your REST-based application. The identification of the
resource, *authority* plus *path* (and some other junk for other examples),
must not depend on the protocol.

Of course, I give you no guarantees that it works. REST just doesn't rely on
HTTP alone. If you change the protocol in your browser right now from "http"
to "ftp," you should get some indication that your browsing agent cannot
connect to that resource. Duh. Ain't got no FTP server running! However, if I
did, and you passed an equivalent GET request for that resource, you should
get this same page.

For an example of REST for another protocol, Paul Prescod wrote the
illustrative
[Reinventing Email using REST](http://www.prescod.net/rest/restmail/). Thank
you, **philipmat**, for that link.

### A REST API should not contain any changes to the communication protocols...

> ...aside from filling-out or fixing the details of underspecified bits of
> standard protocols, such as HTTP’s PATCH method or Link header field.
> Workarounds for broken implementations (such as those browsers stupid enough
> to believe that HTML defines HTTP’s method set) should be defined
> separately, or at least in appendices, with an expectation that the
> workaround will eventually be obsolete. \[Failure here implies that the
> resource interfaces are object-specific, not generic.\]

Ok, Ruby on Rails provides a nice example of this when editing resources
through the representation found at ``/:controller/:id/edit``. Somewhere in
that form, you'll find a hidden form field named "_method" with the value of
"put" in a form with a POST method. When the Rails stack parses the POST with
that "_method" field, it changes the HTTP method from POST to PUT. They do
this to compensate for the browser's inability to properly construct a PUT
request.

If, though, I went and hacked the Rails stack to allow me to put an invalid
value in the "_method" field that did not match with HTTP's methods. For
example, if I created a form in an HTML page that had the hidden "_method"
field with the value "reset" and, on the server-side, that translated to the
invocation of the ``reset`` method on my object handling that value, I've
done what Fielding warns against.

To do this correctly, you should follow the protocols strictly. If you need
resource locking, for example, adopt the WebDAV protocol instead of strict
HTTP. Don't subvert the protocol to your needs; instead, re-engineer your
needs to fit the protocol.

### A REST API should spend almost all of its descriptive effort in defining the media type(s) used for representing resources and driving application state, ...

> ...or in defining extended relation names and/or hypertext-enabled mark-up
> for existing standard media types. Any effort spent describing what methods
> to use on what URIs of interest should be entirely defined within the scope
> of the processing rules for a media type (and, in most cases, already
> defined by existing media types). \[Failure here implies that out-of-band
> information is driving interaction instead of hypertext.\]

Let's say that you've decided to build a blog framework for Web 2.0 and HTML5.
Since you already adopted two buzzwords, you decide to throw in a couple more:
AJAX and REST. On top of it all, your awesome server framework can generate
PDF versions of all the blog posts that it can serve! That's *awesome*! All
the user has to do is add "/pdf" to the URL. You know from that UX semiar that
you attended last year that users don't know how to type unless they can type
into a Google search box. You'll do it for them by providing a link but only
for Firefox users because IE users have no brain and Chrome users offend you
with their elitist attitude.

You get started building your blog application. When they arrive on your page,
the JavaScript makes an AJAX call and gets back some HTML that contains an
unordered list of links for different. You plop that into the DOM.

{% highlight html %}
<ul class="blog-lig">
  <li><a href="/posts/hello-world.html">First post!</a></li>
  <li><a href="/posts/my-favorite-lunch.html">LUNCH!</a></li>
  <li><a href="/posts/i-love-justin-timberlake.html">JT and me!</a></li>
</ul>
{% endhighlight %}

Now, you write a GreaseMonkey script and allow people to download it from your
blogging site. That script adapts the HTML into PDF-serving goodness.

{% highlight html %}
<ul class="blog-lig">
  <li>
    <a href="/posts/hello-world.html">First post!</a>
    <a href="/posts/hello-world.html/pdf">(pdf)</a>
  </li>
  <li>
    <a href="/posts/my-favorite-lunch.html">LUNCH!</a>
    <a href="/posts/my-favorite-lunch.html/pdf">(pdf)</a>
  </li>
  <li>
    <a href="/posts/i-love-justin-timberlake.html">JT and me!</a>
    <a href="/posts/i-love-justin-timberlake.html/pdf">(pdf)</a>
  </li>
</ul>
{% endhighlight %}

You just invoked Dr. Fielding's wrath!

As idiotic as this example seems, remember that REST APIs don't just exist for
browsers. REST describes building services for *applications* across a
network. In your .NET Winforms application or Java SWT app you may decide to
make such assumptions based on an interaction with a REST API that provides
the services for your application. Unless the resource representation includes
those links, you *cannot* assume those state transitions exist. Those
assumptions represents "out-of-band information driving interaction."

Messages in REST need to encapsulate all of the information needed to describe
the message, as well as the transitions away from the application. In this
case, you could use a
[URI Template](http://datatracker.ietf.org/doc/draft-gregorio-uritemplate/?include_text=1)
as a link generator to provide the alternate paths to the PDFs. Then, you
could use in-browser detection to determine if your user has Firefox, and only
then create the associated links.

### A REST API must not define fixed resource names or hierarchies (an obvious coupling of client and server)....

> ...Servers must have the freedom to control their own namespace. Instead, allow
> servers to instruct clients on how to construct appropriate URIs, such as is
> done in HTML forms and URI templates, by defining those instructions within
> media types and link relations. \[Failure here implies that clients are
> assuming a resource structure due to out-of band information, such as a
> domain-specific standard, which is the data-oriented equivalent to RPC's
> functional coupling\].

Let's use Ruby on Rails as an example and its RESTful API support. Assume that
we have created an active model named ``Person``, a controller named
``PeopleController`` with ``show``, ``edit`` and ``update`` methods,
and some views for the *show*, *edit*, and *update* browser requests.
Normally, with these entities and files in place, a programmer would make an
entry in the routes file along the lines of

{% highlight ruby %}
resources :people, :only => {:show, :edit, :update}
{% endhighlight %}

which would, in turn, map the following paths in HTTP requests to these paths.

HTTP method | path              | action
------------|-------------------|--------
GET         | /people/:id       | show
GET         | /people/:id/edit  | edit
PUT         | /people/:id/      | update

And, pretty much *every* Rails application works this way. That imposes a
hierarchy on how to interact with resource on the server. You could type with
real success directly into the browser to move from state to state in the
application without worrying about coming across a piece of functionality that
you would not expect.

The path in a URL should be opaque to the user. The benefit that you and I can
understand it is incidental. If your request to a server for a representation
of the resource at ``http://server/path/to/resource.html`` returns a nice HTML
page, we should also allow the server to define its namespace such that
``http://server/23948729384792834928347.jpg`` returns that HTML page, if the
server so desired.

Now, the Rails way does not *strictly* disobey REST since the easy way to use
it follows a convention-over-configuration design. You could go in and list
custom routes for any of those method+path combinations. Just make sure that
your REST API does not *require* clients to konw some predefined route
structure to use your service.

### A REST API should never have “typed” resources that are significant to the client....

> ...Specification authors may use resource types for describing server
> implementation behind the interface, but those types must be irrelevant and
> invisible to the client. The only types that are significant to a client are
> the current representation’s media type and standardized relation names.
> \[ditto\]

Almost every so-called REST service that serves JSON has this problem. For
example, you write a REST API for a resource that describes Mark Twain and it
returns this HTTP response.

{% highlight javascript %}
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 461

{
  "name": "Mark Twain",
  "notable feature": "crazy hair",
  "novels": [
    "Adventures of Tom Sawyer, The (1876)",
    "Prince and the Pauper, The (1881)",
    "Adventures of Huckleberry Finn, The (1884)",
    "Connecticut Yankee in King Arthur's Court, A (1889)",
    "Tom Sawyer Abroad (1894)",
    "Pudd'nhead Wilson (1894)",
    "Tom Sawyer, Detective (1896)",
    "Personal Recollections of Joan of Arc, the (1896)",
    "Diaries of Adam and Eve (1906)"
  ]
}
{% endhighlight %}

Here's the problem. You have a "typed resource" here. What you really know
from this response and the metadata is only that it contains JSON and the
value of the data in the body of the response. The entries *name* and *novels*
have no semantic meaning in this case. The only way that the browser knows
about how to do something with this is to represent it with out-of-band
information, especially if you decide to allow the user to add another book to
an incomplete list. Because this resource's representation contains no links
to other resources, your user has come to the end of the application.

We can fix this example a couple of ways. First of, ``application/json`` does
not really give us much information. We'd really like for the message to
describe the contents within the package so we can understand the semantic
meaning of the data packet.

#### Option 1: Include header links

We can include header links in the server's response to describe a relation
for this data that understands how it works.

{% highlight javascript %}
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 461
Link: <author-format-interpreter.js>; REL=JSON-interpreter

{
  "name": "Mark Twain",
{% endhighlight %}

The browser does not know how to interpret the relation "JSON-interpreter."
Instead, you should have code in the browser already that can read that header
from an AJAX call and load the script file.

#### Option 2: Invent a new media type or microfomat

\[Wikipedia has a nice article on
[microformats](http://en.wikipedia.org/wiki/Microformat).\]

For the most part, ``application/json`` fails almost every requirement of a
media type for REST. It merely states that the body of the message contains
JSON. When your browser loads something with a ``text/html`` type, it knows
what to do with it: render it using its HTML parser. If the browser receives
a message with a ``image/png`` media type, it knows to render bitmap
information. ``application/json`` does not tell the browser *anything* about
how to use the packet. And, if your JavaScript expects a certain data format
without the advantage of a self-describing message, then you have failed REST.

To ensure that we have an author returning, we can invent a media type for the
AJAX call to sense and handle it based on that media type rather than an
expected format.

{% highlight javascript %}
HTTP/1.1 200 OK
Content-Type: text/vnd.myapp-author
Content-Length: 461

{
  "name": "Mark Twain",
{% endhighlight %}

### A REST API should be entered with no prior knowledge beyond the initial URI (bookmark) and set of standardized media types that are appropriate for the intended audience...

> ...(i.e., expected to be understood by any client that might use the API). From
> that point on, all application state transitions must be driven by client
> selection of server-provided choices that are present in the received
> representations or implied by the user’s manipulation of those
> representations. The transitions may be determined (or limited by) the
> client’s knowledge of media types and resource communication mechanisms,
> both of which may be improved on-the-fly (e.g., code-on-demand). \[Failure
> here implies that out-of-band information is driving interaction instead of
> hypertext.\]

If you took the representation from the previous section and generated links
to Amazon Books that searched for each of the titles, that breaks this
expectation of REST. If you invent a URI that leads from the current resource
to another resource or POST back to this or another resource, you've boned
your REST client.

Again, to fix this, use code-on-demand and URI Templates.

## How does this relate to [New (Old) Web Architecture](http://philipm.at/2012/0121/)?

I like what **philipmat** wrote about when he defended his response to "why a
new way?" We can respond to every complaint with "if it complied with REST,
that complaint would not exist."

His proposal has a very REST-compliant feeling to it but breaks when we get to
the example. I see an opportunity to make it REST-compliant through a few
small augmentations, a couple of justifications, and a little celebration.

He proposes these steps for what I will now call "Bidirectional Operative
RESTful Asynchronous Xeri-programming." (When you hear in a couple of years
that everyone wants to do that BORAX-programming, remember you heard it here
first.)

1. Navigate to ``/one_entity#clients/1``, receive static HTML for the shell of
   the page and a link to a script to load entity data and another to load
   entity representation.
1. Run a script to request entity data.
1. Run a script to request entity template.
1. When both return, merge data into template and display it (In this
   example's case, merge with [knockout.js](http://knockoutjs.com).)

### Dissection - Step 1

**Understanding URL Fragments**  
I haven't touched on URL fragments, yet, in my discussions about URIs. Since
browsers don't send them to the server, I really haven't had need to talk
about them; however, with BORAX-programming, it makes sense. A fragment
points to a subentity of the entity represented by the resource at the end of
the URL. In a browser that usually means an element with a specific ``name``
or ``id`` attribute to which the browser will automatically scroll. However,
if the subentity does not readily exist in the entity and we have some way to
discover its location, then nothing in REST says that we can't traverse the
application state to include that subentity in the current state.
{: class=aside }

The first step states "Give me the resource for one_entity and navigate to the
sub-entity named by clients/1." The JavaScript included with "one_entity"
would then start the requests. Most likely, it knows how to do this because
the JavaScript interprets the information after the fragment identifier as a
relative URI. That does not comply with REST. However, we can make it comply
with REST by using the ``link`` tag, a custom relation, changing the fragment
to a Uniform Resource Name, and a
[URI template](http://datatracker.ietf.org/doc/draft-gregorio-uritemplate/?include_text=1).
{: class=after-aside }

Now, our application will change its state to the resource found at
``/one_entity#urn:myapp:client:1``.

{% highlight html %}
<!DOCTYPE html>
<html>
  <head>
    <link id="page-entity" rel="unloaded-subentity" href="{/entity,id}">
    <script src="entity-load.js"></script>
...
{% endhighlight %}

The browser won't know squat what to do with that link. Dr. Fielding knew that
this would happen and included the code-on-demand portion of REST to augment
the rendering of a resource. That's what that ``script`` tag following the
``link`` tag does: run the URI template from the link that the browser can't
handle because it does not understand the "entity-representation" relation.

Furthermore, because the fragment now consists of a URN, because the URI
standard allows us to translate URNs to URLs, because REST has allowed us to
load the "entity-load.js" script-represented resource, because we have a link
builder in the form a of URI template with a custom relation that our
application can interpret, we have met all requirements of self-describing
messages! That, friends, is REST.

### Dissection - Steps 2 and 3

If a browser supported HTTP responses with a *Content-Type* of
"multipart/related", then we would have no need to require two steps where one
would accomplish our task. This "plugs a hole" in the browser's limited
capabilities.

The "entity-load.js" script will make two related calls. The first should
return the HTML representation of the template. The second should return the
data representation of the resource. The key to successful REST compliance for
this step: ensure that we return meaningful media types.

In the case of the HTML template and JSON which will constitute the body of
the responses, we want to provide meaningful representations of those media
types. Since, in this case, we have decided to use **knockout.js**, we'll
invent knockout-specific MIME types to describe the responses.

For the HTML template, the AJAX request should include

{% highlight bash %}
Accept: text/vnd.knockout-template
{% endhighlight %}

and for the JSON data, the AJAX request should include 

{% highlight bash %}
Accept: text/vnd.knockout-data
{% endhighlight %}

If those two items came back in a "multipart/related" response from a server,
it would make total sense to use **knockout.js** to combine them.

We've leveraged the power of media types to help render our specific content.
Remember, if we have returned those two messages with the media types
``text/html`` and ``application/json``, the message would imply that we should
just render the HTML in the browser without connection to any templating
needs and do nothing with the JSON because we cannot infer to plug that into
the templating engine.

REST requires self-describing messages. We use custom media types to allow our
application to understand the rendering intent of the content of each of those
responses.

### Dissection - Step 4

Now that the content has returned, we should ensure the correct media types
exist for the responses, then let **knockout** do its magic. Shazam!

## Real REST? I think so!

From the dissection of those steps, I'd say they stay well within the
boundaries of REST over HTTP to make sure that we can have all of those
execllent benefits that Dr. Fielding displays in all of the REST literature.

Remember, REST does not say anything about CRUD. REST does not actually mean
GET, PUT, POST, and DELETE. HTTP grew up to embody the ideas of REST, not the
other way around.

It demands that we have *all* of the transitions for the current state of our
application contained within the resource returned in our request. It demands
that we pay attention to the metadata of the resource representation.

REST also allows us to extend the capabilities of the client through
code-on-demand to handle unknown media types and enrich the representation of
the current UI.

As Dr. Fielding writes, REST is simple. You just have to think a long time,
make many mistakes, and fail miserably a couple of times before it beomces
simple in your mind.

## Is this what philipmat wants? What he desires, covets, craves, lusts after?

I don't think so. From what I understand of his motives, the custom media
type issue just won't work without some work on the part of the Web developer
with custom mime-type mappings and custom file extensions. He wants to keep
that interaction as *simple as possible*.

However, that issue seems the only thing standing between his divorced efforts
of UI and server development. Perhaps he can think through the problem and
engineer a better solution.

You can find my forked nodejs-served version of
[philipmat/webmvc@github](https://github.com/philipmat/webmvc) over at
[realistschuckle/webmvc@github](https://github.com/realistschuckle/webmvc/tree/borax).
Make sure that you checkout the **borax** branch!

