---
layout: post
title:  Emergency plates Update (2012-01-13) for To-Do List Application
tags:   javascript, flatiron, plates

synopsis: In which we revisit the **plates** functionality.
---
Back in
[Story 4](../13/get-to-know-flatiron.js-by-building-a-todo-app-story-4.html),
we used **plates** to generate the HTML that we used. It seems that since I
wrote the entry, [hij1nx](https://github.com/hij1nx) had the audacity to make
**plates** *much better*. Kudos!

## Clearer option specification through fluency

Before, when I wanted to map values into tags, I had to specify the following
dictionary.

{% highlight javascript %}
var options = {
  'id': ['id', 'value'],
  'ctime': 'id',
  'desc': 'id'
};
{% endhighlight %}

If I want to change that, I have to refer to the documentation because those
values have no context to them. What does ``'id': ['id', 'value']`` really
mean, anyway?

Now, **plates** replaces that with a new ``Map`` object. Now, I can write the
following that has the same meaning as above.

{% highlight javascript %}
var options = plates.Map();
options.where('name') // HTML attribute of tag
       .is('id')      // Value for attribute
       .use('id')     // Entry in the binding data
       .as('value');  // Target attribute for replacement
{% endhighlight %}

I put the comments there for clarification. However, I don't really need them
because the replacement parameters now have context to them.

## Changing the to-do list app

The code that I wrote in 
[Story 4](../13/get-to-know-flatiron.js-by-building-a-todo-app-story-4.html)
no longer works. I'll fix that, now.

First, get the newly published version of **plates**. Mark the version as
0.4.3 in the ``package.json``.

{% highlight javascript %}
{
  "name": "todo-list",
  "version": "0.1.0",
  "dependencies": {
    "flatiron": "*",
    "union": "*",
    "plates": "0.4.3",
    "resourceful": "git://github.com/flatiron/resourceful.git",
    "connect": "git://github.com/senchalabs/connect.git"
  }
}
{% endhighlight %}

Now, re-install **plates** using ``npm``.

{% highlight javascript %}
todo/%  npm uninstall plates
todo/%  npm install
{% endhighlight %}

Finally, change the ``get`` route to the following. In-line comments explain
the changes.

{% highlight javascript %}
app.router.get('/', function() {
  var self = this;

  // Had to add 'utf-8' to my readFile. Don't know what changed, but
  // started getting a raw Buffer object rather than a string.
  fs.readFile('index.html', 'utf-8', function(err, data) {
    if(err) {
      self.res.writeHead(404);
      self.res.end();
      return;
    }
    var listContent = "";
    if(typeof self.req.session.tasks === 'undefined') {
      self.req.session.tasks = [];
    }

    // For the elements with a class of 'ctime', replace its inner value with
    // the value stored in 'ctime' in the data object.
    var optctime = plates.Map().class('ctime').to('ctime');

    // For the elements with a class of 'desc', replace its inner value with
    // the value stored in 'desc' in the data object.
    var optdesc = plates.Map().class('desc').to('desc');

    // For the element with a name attribute of 'id', put the value stored in
    // 'id' in the data object into the 'value' attribute of the element.
    var optid = plates.Map().where('name').is('id').use('id').as('value');

    self.req.session.tasks.forEach(function(task) {
      var data = {
        'desc': task.desc,
        'ctime': new Date(task.ctime).toDateString().substr(4),
        'id': task._id
      };

      // Bind the options on each element that requires the value replacement.
      listContent += '<li>' +
        '<form method="post" action="/">' +
          '<button>Delete Item</button>' +
          plates.bind('<span class="ctime"></span>', data, optctime) +
          '<span>I need to </span>' +
          plates.bind('<span class="desc"></span>', data, optdesc) +
          '<input type="hidden" name="method" value="DELETE" />' +
          plates.bind('<input type="hidden" name="id" value="" />', data, optid) +
        '</form>' +
      '</li>';
    });
    data = plates.bind(data, {'task-list': listContent});
    self.res.writeHead(200, {'Content-Type': 'text/html'});
    self.res.end(data);
  })
});
{% endhighlight %}

You can get this new code from
[story5-plates-0.4.3.zip](/assets/story5-plates-0.4.3.zip)

You can find the updated API documentation at
[https://github.com/flatiron/plates](https://github.com/flatiron/plates).