---
layout: post
title:  Runtime Class Mixins with Python
tags:   OOD

synopsis: In which I show you how to do runtime mixins for classes in Python.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

Say you want to mix in a method into an existing class but can't get to the
class' definition. In Python, you can use the following decorator to do that.

{% highlight python linenos %}
# mixin.py

import inspect

def mixin_to(cls):
  def f(fn):
  	if inspect.isfunction(fn):
	  setattr(cls, fn.func_name, fn)
	elif inspect.isclass(fn):
	  for name in dir(fn):
	    attr = getattr(fn, name)
	    if inspect.ismethod(attr):
	      setattr(cls, name, attr.im_func)
	return fn
  return f
{% endhighlight %}

This method handles mixing in a single method as well as another class'
methods. You can even mix methods into a class after instantiating it.

{% highlight python linenos %}
class Unadorned(object):
  pass

# Instantiate an Unadorned
u = Unadorned()

# Mixin in methods from a class
@mixin_to(Unadorned)
class MixinClass(object):
  def mixin_method(self):
    return "mixin_method calls " + self.mixin_function()

# Mixin a function
@mixin_to(Unadorned)
def mixin_function(o):
  return "mixin_function!"

# Use the method mixed into the class
print u.mixin_method() # PRINTS "mixin_method calls mixin_function!"
{% endhighlight %}

Wow! That's nice. You can download [mixin.py](/assets/mixin.py) for your use.
