---
layout: post
title:  Making a To-Do List With flatiron.js (Story 3)
tags:   javascript, flatiron
date:   2012-01-13 08:00:00

synopsis: "Story 3: When a user POSTs a form to /, it creates a new ToDo item, adds it to the session, and redirects to /."
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

## Previous Stories in this Series
* [Story 0](../10/get-to-know-flatiron.js-by-building-a-todo-app-story-0.html) - [story0.zip](/assets/story0.zip)
* [Story 1](../11/get-to-know-flatiron.js-by-building-a-todo-app-story-1.html) - [story1.zip](/assets/story1.zip)
* [Story 2](../12/get-to-know-flatiron.js-by-building-a-todo-app-story-2.html) - [story2.zip](/assets/story2.zip)

-----

Oooh, a model. Finally! Let's use **resourceful** to define this ``ToDo``
model.

Turns out that the most recently released version of **resourceful** suffers
from some bugs, too. So, modify your ``package.json`` file to read

{% highlight javascript linenos %}
{
  "name": "todo-list",
  "version": "0.1.0",
  "dependencies": {
    "flatiron": "*",
    "union": "*",
    "plates": "*",
    "resourceful": "git://github.com/flatiron/resourceful.git",
    "connect": "git://github.com/senchalabs/connect.git"
  }
}
{% endhighlight %}

and run the commands 

{% highlight bash %}
npm uninstall resourceful
npm install
{% endhighlight %}

## resourceful - A storage agnostic resource-oriented ODM for building prototypical models with validation and sanitization.

That's quite a mouthful. In short, **resourceful** allows us to define
prototypes that will ensure that the properties have values of the correct
type assigned to them and other simple validations.

For us, though, we just want a pretty simple Task class that has an
identifier, some text to describe the task, and a created date. I think would
fit the bill, pretty well. At the top of our ``server.js`` file, we should
``require`` **resourceful** and define our Task prototype.

{% highlight javascript %}
// server.js

var session = require('connect').session
  , cookieParser = require('connect').cookieParser
  , flatiron = require('flatiron')
  , app = flatiron.app
  , fs = require('fs')
  , resourceful = require('resourceful')
  ;

var Task = resourceful.define('task', function() {
  this.timestamps();
  this.string('desc').required(true)
                     .minLength(1);
});
{% endhighlight %}

Now, down after the definition for GET, I will define my POST logic. I will 
need to parse the body of the post, so I will include a
``qs = require('querystring')`` at the top of the file.

{% highlight javascript %}
app.router.post('/', function() {
  var self = this;
  var task = new (Task)({desc: self.req.body.desc});
  if(task.validate().valid) {
    task.save();
    if(!self.req.session.tasks) {
      self.req.session.tasks = [];
    }
    self.req.session.tasks.push(task);
  }
  self.res.writeHead(303, {'Location': '/'});
  self.res.end();
});
{% endhighlight %}

Not bad at all.
