---
layout: post
title:  Making a To-Do List With flatiron.js (Story 2)
tags:   javascript, flatiron

synopsis: "Story 2: When a user first issues a GET to /, it serves an HTML page that shows an entry text box for a to-do list item and a button to POST the item to /."
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

* [Story 0](../10/get-to-know-flatiron.js-by-building-a-todo-app-story-0.html) - [story0.zip](/assets/story0.zip)
* [Story 1](../11/get-to-know-flatiron.js-by-building-a-todo-app-story-1.html) - [story1.zip](/assets/story1.zip)
* Story 2
* [Story 3](../13/get-to-know-flatiron.js-by-building-a-todo-app-story-3.html)

-----

Ok. Easy and ugly. Create a file named ``index.html`` and create some HTML
that shows a text input and a submit button. Change your ``server.js`` to
return it for the GET / request. I did it like this.

{% highlight javascript %}
// server.js

var session = require('connect').session
  , cookieParser = require('connect').cookieParser
  , flatiron = require('flatiron')
  , app = flatiron.app
  , fs = require('fs')
  ;

app.use(flatiron.plugins.http);

app.http.before.push(cookieParser('todo list secret'));
app.http.before.push(session());

app.router.get('/', function() {
  var self = this;
  fs.readFile('index.html', function(err, data) {
    if(err) {
      self.res.writeHead(404);
      self.res.end();
      return;
    }
    self.res.writeHead(200, {'Content-Type': 'text/html'});
    self.res.end(data);
  })
});

app.start(8090);
{% endhighlight %}

With my awesome HTML, my page looks like this.

![story 2](/img/flatiron-todo-2.png)
