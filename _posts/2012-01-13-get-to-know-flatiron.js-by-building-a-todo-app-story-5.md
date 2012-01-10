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

## Previous Stories in this Series
* [Story 0](../10/get-to-know-flatiron.js-by-building-a-todo-app-story-0.html) - [story0.zip](/assets/story0.zip)
* [Story 1](../11/get-to-know-flatiron.js-by-building-a-todo-app-story-1.html) - [story1.zip](/assets/story1.zip)
* [Story 2](../12/get-to-know-flatiron.js-by-building-a-todo-app-story-2.html) - [story2.zip](/assets/story2.zip)
* [Story 3](../13/get-to-know-flatiron.js-by-building-a-todo-app-story-3.html) - [story3.zip](/assets/story3.zip)
* [Story 4](../13/get-to-know-flatiron.js-by-building-a-todo-app-story-4.html) - [story4.zip](/assets/story4.zip)

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

Now, we need to take into account the post for that Delete button. Because we
have made this a POST, we can handle it in the POST handler that we defined
in
[Story 3](../13/get-to-know-flatiron.js-by-building-a-todo-app-story-3.html).

{% highlight javascript %}
app.router.post('/', function() {
  var self = this;
  if(self.req.body.method && self.req.body.method === "DELETE") {
    var taskId = self.req.body.id;
    var task = Task.get(taskId);
    var tasks = self.req.session.tasks;
    tasks = tasks.splice(0, tasks.indexOf(task)).concat(tasks.splice(1));
    self.req.session.tasks = tasks;
    Task.destroy(taskId);
  } else {
    var task = new (Task)({desc: self.req.body.desc});
    if(task.validate().valid) {
      task.save();
      if(!self.req.session.tasks) {
        self.req.session.tasks = [];
      }
      self.req.connection = {encrypted: false};
      self.res.emit('header');
      self.req.session.tasks.push(task);
    }
  }
  self.res.writeHead(303, {'Location': '/'});
  self.res.end();
});
{% endhighlight %}

And, that's it. Everything works. It's not pretty: the UI, the code. It would
be nice to convert the POST that destroys a task into a DELETE message;
however, that's deeper than this article should go.

And, obviously, **plates** leaves a lot to be desired. I actually had a
different implementation in my GET handler for this story and found that
**plates** falls apart with its "simple" (read: buggy) HTML parser. I would
like a DOM to actually handle this; however, as they mention in the
documentation, those options do not perform quickly enough.

But, this is it: **flatiron**. Overall, I like its unobtrusive nature. I think
I will find it easy to build applications atop this framework.

And, here's the completed [code](/assets/story5.zip).