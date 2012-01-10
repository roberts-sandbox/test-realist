---
layout: post
title:  Making a To-Do List With flatiron.js (Story 1)
tags:   javascript, flatiron

synopsis: "Story 1: When a user first issues a GET to /, then it creates a new session."
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

## Previous Stories in this Series
* [Story 0](../10/get-to-know-flatiron.js-by-building-a-todo-app-story-0.html) - [story0.zip](/assets/story0.zip)

-----

We'll use **connect**'s 
[session](http://senchalabs.github.com/connect/middleware-session.html)
middleware to get this going. In the documentation, it shows that we must
include the ``cookieParser`` middleware first and then pass a token into the
``session`` middleware to compute the hash stored in the session cookie. In
our server file, let's implement that. 

{% highlight javascript linenos %}
// server.js

var session = require('connect').session
  , cookieParser = require('connect').cookieParser
  , flatiron = require('flatiron')
  , app = flatiron.app
  ;

app.use(flatiron.plugins.http);

app.http.before.push(cookieParser());
app.http.before.push(session({secret: 'todo list secret'}));

app.router.get('/', function() {
  this.res.end();
});

app.start(8090);
{% endhighlight %}

That should be all there is to it. Run ``npm start`` from the command line
and navigate to [http://localhost:8090](http://localhost:8090).

### Problem: Object \[object Object\] has no method '_implicitHeader'

Well, that didn't work. The server threw an exception and our process exited.
The top two entries in the stack trace show us some relevant information.

{% highlight bash %}
"TypeError: Object [object Object] has no method '_implicitHeader'",
" at [object Object].<anonymous> (./node_modules/connect/lib/middleware/session.js:279:31)",
" at Object.<anonymous> (./server.js:15:12)",
{% endhighlight %}

There's a problem in the **session** middleware. If we head over to its github
repo and look at the
[history of session.js](https://github.com/senchalabs/connect/commits/master/lib/middleware/session.js),
then we find out that the version of ``session.js`` that we installed with
version 1.8.5 of **connect** is at least six months old. Well, let' update
connect to the 2.0.0alpha version by specifying the URL to the tarball. Change
``package.json`` to read

{% highlight javascript linenos %}
{
  "name": "todo-list",
  "version": "0.1.0",
  "dependencies": {
    "flatiron": "*",
    "union": "*",
    "plates": "*",
    "resourceful": "*",
    "connect": "https://github.com/senchalabs/connect/tarball/2.0.0alpha1"
  }
}
{% endhighlight %}

Run the following commands at the command line.

{% highlight bash %}
npm uninstall connect
npm install
npm start
{% endhighlight %}

Once again, navigate to [http://localhost:8090](http://localhost:8090) and
let's see what we get.

### Another problem: connect.cookieParser(\"secret\") required for security when using sessions

Well, looks like the API changed between **connect@1.8.5** and
**connect@2.0.0**. Let's change the ``server.js`` file to honor the error
message. Since the **cookieParser** now takes the secret, I bet that we don't
need to provide it to the **session**. Change ``server.js`` to read

{% highlight javascript linenos %}
// server.js

var session = require('connect').session
  , cookieParser = require('connect').cookieParser
  , flatiron = require('flatiron')
  , app = flatiron.app
  ;

app.use(flatiron.plugins.http);

app.http.before.push(cookieParser('todo list secret')); // secret here
app.http.before.push(session()); // no secret here

app.router.get('/', function() {
  this.res.end();
});

app.start(8090);
{% endhighlight %}

Run the following commands at the command line.

{% highlight bash %}
npm start
{% endhighlight %}

Once again, navigate to [http://localhost:8090](http://localhost:8090) and
let's see what we get.

### Problem revisited: Object \[object Object\] has no method '_implicitHeader'

Seriously? Don't they release new versions of **connect**? Ever?

Fine, we'll install HEAD instead of 2.0.0.alpha. Change ``package.json`` to
read 

{% highlight javascript linenos %}
{
  "name": "todo-list",
  "version": "0.1.0",
  "dependencies": {
    "flatiron": "*",
    "union": "*",
    "plates": "*",
    "resourceful": "*",
    "connect": "git://github.com/senchalabs/connect.git"
  }
}
{% endhighlight %}

Run the following commands at the command line.

{% highlight bash %}
npm uninstall connect
npm install
npm start
{% endhighlight %}

Once again, navigate to [http://localhost:8090](http://localhost:8090) and
let's see what we get.

### Problems resolved

Finally, an empty page in the browser and no uncaught exceptions in our
server. Let's head on over to the second story. So, **flatiron** may be
backwards compatible with **connect**, but **connect** doesn't have a new
release to make it compatible with node@0.6.
