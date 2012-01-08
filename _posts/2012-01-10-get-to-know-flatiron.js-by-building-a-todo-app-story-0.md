---
layout: post
title:  Making a To-Do List With flatiron.js (Old School)
tags:   javascript, flatiron

synopsis: In which I walk through making a primitive to-do list Web app with flatiron.js.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

* Story 0
* [Story 1](../11/get-to-know-flatiron.js-by-building-a-todo-app-story-1.html)
* [Story 2](../12/get-to-know-flatiron.js-by-building-a-todo-app-story-2.html)
* [Story 3](../13/get-to-know-flatiron.js-by-building-a-todo-app-story-3.html)

-----

The makers of **[flatiron.js](http://flatironjs.org/)** bill it as "an
unobtrusive framework initiative for node.js." It consists of five major
components that the creators want to behave "isomorphically," that is,
similarly in the browser and on the server.

__director__
: A URL router for the framework.

__union__
: A hybrid buffered / streaming middleware kernel backwards compatible with
  [connect](http://senchalabs.github.com/connect/) middleware.

__plates__
: A simple, unobtrusive templating solution that keeps the trash/placeholders
  out of your html.

__resourceful__
: A storage agnostic resource-oriented ODM for building prototypical models
  with validation and sanitization.

__broadway__
: A simple plug-in API which allows you to extend the top-level application
  object easily.

## Installation

Because **flatiron** promises an unobtrusive framework, it only relies on
**broadway** and **director** from that list. You get to choose whether or not
you want to use the other three components. So, if you want middleware,
templating, or object-document mapping, you'll need to install the other
components separately.

{% highlight bash %}
mkdir todo
cd todo
npm install flatiron union plates resourceful
{% endhighlight %}

(*Warning*: If you want to use **flatiron** for responding to HTTP requests,
it *requires* **union**.)

## Using flatiron on the server

When you require the **flatiron** library in your server code, it exposes an
``app`` property that allows plugins through the use of **broadway**.
**flatiron** comes with a plugin to provide HTTP router function through
**director**. You configure it like this.

{% highlight javascript linenos %}
var flatiron = require('flatiron'),
    app = flatiron.app; // Singleton instance of an App.

app.use(flatiron.plugins.http);
{% endhighlight %}

After you execute that code, the plugin mixes four new attributes into the
``app`` instance.

__app.http__: object
: An object with **before** and **after** arrays to run callbacks before and
  after each successful HTTP request.  It also has a map named **headers**
  that allows you to specify a set of headers that **director** should add to
  each HTTP request.

__app.listen__: function(port, host, callback)
: A method that creates an middleware server using **union** and calls its
  ``listen`` method with the specified *port*, *host*, and *callback*.

__app.router__: object
: An instance of the **director** HTTP router.

__app.start__: function(port, host, callback)
: A method that initializes the underlying **broadway** subsystem and, then,
  calls **listen**.

We use the **app.router** attribute to configure the URLs to which our
application will respond. Then, we can use **app.start** to get it running.

## The to-do list design

Let's figure out the user stories.

1. When a user first issues a GET to /, then it creates a new session.
1. When a user first issues a GET to /, it serves an HTML page that shows an
   entry text box for a to-do list item and a button to POST the item to /.
1. When a user POSTs a form to /, it creates a new ToDo item, adds it to the
   session, and redirects to /.
1. When a user issues a GET to / after session creation, the HTML page
   continues to show the input and button while showing the task list beneath
   it.
1. Each item in the task list will have a "Delete" link next to it so the user
   can remove the to-do item from the list.

That seems pretty reasonable for a primitive, functional to-do list. Let's
make it happen.

## Building the to-do list application, story-by-story, without unit tests

Yes, without unit tests. Sorry. I want to do a blog post on
[vows](http://vowsjs.org/), an asynchronous BDD framework for node.js.
However, I haven't had enough time to play with it, so I will just cowboy my
way through the stories.

### Story 0: Getting started

Create some directory in which you want to write the code that I write. I ran
the following commands from the command line. Then, I opened the directory in
my currently favored text editor,
[Sublime Text 2](http://www.sublimetext.com/2).

{% highlight bash %}
mkdir -p ~/dev/todo
cd ~/dev/todo
touch package.json server.js
subl .
{% endhighlight %}

I like to let ``npm`` handle my dependencies. So, in ``package.json``, put the
following contents. If you don't know what this means, run ``npm help json``
at the command line.

{% highlight javascript linenos %}
{
  "name": "todo-list",
  "version": "0.1.0",
  "dependencies": {
    "flatiron": "*",
    "union": "*",
    "plates": "*",
    "resourceful": "*",
    "connect": "*"
  }
}
{% endhighlight %}

The asterisks in the dependencies dictionary just means load the latest
version available from **npm**.

Now, run ``npm install`` in that directory to get those dependencies
installed.
