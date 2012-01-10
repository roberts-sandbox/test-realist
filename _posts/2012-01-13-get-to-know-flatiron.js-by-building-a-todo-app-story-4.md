---
layout: post
title:  Making a To-Do List With flatiron.js (Story 4)
tags:   javascript, flatiron
date:   2012-01-13 09:00:00

synopsis: "Story 4: When a user issues a GET to / after session creation, the HTML page continues to show the input and button while showing the task list beneath it."
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

* [Story 0](../10/get-to-know-flatiron.js-by-building-a-todo-app-story-0.html) - [story0.zip](/assets/story0.zip)
* [Story 1](../11/get-to-know-flatiron.js-by-building-a-todo-app-story-1.html) - [story1.zip](/assets/story1.zip)
* [Story 2](../12/get-to-know-flatiron.js-by-building-a-todo-app-story-2.html) - [story2.zip](/assets/story2.zip)
* [Story 3](../13/get-to-know-flatiron.js-by-building-a-todo-app-story-3.html) - [story3.zip](/assets/story3.zip)
* Story 4

-----

Now, we need to go back and change the handler for GET to list the tasks
found in the session that we added back in the
[story 3]({{ page.previous.url }}).

Now, we'll use **plates** to build the list of items and, then, put it back
into the overall page. **plates** binds values based on HTML attributes such
as the ``id`` or ``class`` of the elements in the template. This removes the
gunk that you normally find in templates. I like that idea, a lot. However, it
does not handle collections of values, so we need to do that ourselves.

First, we need to include the **plates** library into the script.

{% highlight javascript %}
// server.js

var session = require('connect').session
  , cookieParser = require('connect').cookieParser
  , flatiron = require('flatiron')
  , app = flatiron.app
  , fs = require('fs')
  , resourceful = require('resourceful')
  , qs = require('querystring')
  , plates = require('plates')  // INCLUDE PLATES
  ;
{% endhighlight %}

I added a UL tag to my ``index.html`` with an id of "task-list". Now, in the
``server.js`` file, in the GET handler for /, we need to render the tasks
into LI tags. Here's what mine looks like.

{% highlight javascript %}
app.router.get('/', function() {
  var self = this;
  fs.readFile('index.html', function(err, data) {
    if(err) {
      self.res.writeHead(404);
      self.res.end();
      return;
    }

    /* NEW STUFF HERE */
    var listContent = "";
    var listItemTemplate = '<li>' +
      '<span id="ctime" class="ctime"></span>' +
      'I need to <span id="desc" class="desc"></span>' +
    '</li>';
    if(typeof self.req.session.tasks === 'undefined') {
      self.req.session.tasks = [];
    }
    self.req.session.tasks.forEach(function(task) {
      var data = {
        'desc': task.desc,
        'ctime': new Date(task.ctime).toDateString()
      };
      listContent += plates.bind(listItemTemplate, data);
    });
    data = plates.bind(data, {'task-list': listContent});
    /* NEW STUFF HERE */

    self.res.writeHead(200, {'Content-Type': 'text/html'});
    self.res.end(data);
  })
});
{% endhighlight %}

I run it and everything seems fine except when I click the "Add" button, no
new task appears in my list. No empty LI tag. No nothing. What's going on?
It's like the session doesn't remember my tasks between requests. So, I'm
going to put a log statement in the check for my task list being undefined.

{% highlight javascript %}
    if(typeof self.req.session.tasks === 'undefined') {
      console.log('No tasks in the session.');
      self.req.session.tasks = [];
    }
{% endhighlight %}

When I run it, sure enough, after a post, I see that message printed. Darn it.
The **connect** **session** plugin must not be working. Once again, going to
the source of
[session.js](https://github.com/senchalabs/connect/blob/master/lib/middleware/session.js),
I notice that the plugin writes the session cookie when the Response object
emits a 'header' event. That could be it. So, I'll put that into my POST
handler because I want the cookie written at that point.

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
  self.res.emit('header'); // <------------------- NEW LINE HERE
  self.res.end();
});
{% endhighlight %}

I type `npm start` and after I POST a new to-do item ... BOOM!

{% highlight bash %}
TypeError: Cannot read property 'encrypted' of undefined
  at [object Object].<anonymous> (./todo/node_modules/connect/lib/middleware/session.js:217:31)
{% endhighlight %}

Back to the source and I see that the **session** plugin requires a value
for ``req.connection.encrypted``. Well, let's stub that value and see what
happens.

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
  self.req.connection = {encrypted: false}; // <-- NEW LINE HERE
  self.res.emit('header'); // <------------------- NEW LINE HERE
  self.res.end();
});
{% endhighlight %}

Again, with the ``npm start`` and ... SUCCESS! Now, when I post my task, it
appears in my list! Hooray!

![story 4](/img/flatiron-todo-4.png)
