---
layout: post
title:  Making a To-Do List With flatiron.js (Story 5)
tags:   javascript, flatiron
date:   2012-01-13 10:00:00

synopsis: "Story 5: Each item in the task list will have a &quot;Delete&quot; link next to it so the user can remove the to-do item from the list."
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

* [Story 0](../10/get-to-know-flatiron.js-by-building-a-todo-app-story-0.html) - [story0.zip](/assets/story0.zip)
* [Story 1](../11/get-to-know-flatiron.js-by-building-a-todo-app-story-1.html) - [story1.zip](/assets/story1.zip)
* [Story 2](../12/get-to-know-flatiron.js-by-building-a-todo-app-story-2.html) - [story2.zip](/assets/story2.zip)
* [Story 3](../13/get-to-know-flatiron.js-by-building-a-todo-app-story-3.html) - [story3.zip](/assets/story3.zip)
* [Story 4](../13/get-to-know-flatiron.js-by-building-a-todo-app-story-4.html) - [story4.zip](/assets/story4.zip)
* Story 5

-----

Last but not least: we need to allow the user to delete a listed item. So, we
can change the template used to create the list items to include a delete
button. Here's what I have, simple and ugly.

{% highlight javascript %}
app.router.get('/', function() {
  var self = this;
  fs.readFile('index.html', function(err, data) {
    if(err) {
      self.res.writeHead(404);
      self.res.end();
      return;
    }
    var listContent = "";
    var listItemTemplate = '<button>Delete Item</button>' +
                           '<span id="ctime" class="ctime"></span>' +
                           'I need to <span id="desc" class="desc"></span>' +
                           '<input type="hidden" name="method" value="DELETE" />' +
                           '<input type="hidden" id="id" name="id" value="" />';
    if(typeof self.req.session.tasks === 'undefined') {
      self.req.session.tasks = [];
    }
    var options = {
      'id': ['id', 'value'],
      'ctime': 'id',
      'desc': 'id'
    };
    self.req.session.tasks.forEach(function(task) {
      var data = {
        'desc': task.desc,
        'ctime': new Date(task.ctime).toDateString().substr(4),
        'id': task._id
      };
      listContent += '<li>' +
        '<form method="post" action="/">' +
        plates.bind(listItemTemplate, data, options) +
        '</form>' +
      '</li>';
    });
    data = plates.bind(data, {'task-list': listContent});
    self.res.writeHead(200, {'Content-Type': 'text/html'});
    self.res.end(data);
  })
});
{% endhighlight %}

Now, we need to take into account the post for that Delete button.