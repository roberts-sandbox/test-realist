---
layout: post
title:  The Visitor Pattern in Python
tags:   OOD, python

synopsis: In which I implement the visitor pattern in Python with decorators.
---
I'm a fan of the visitor pattern for its emulation of dynamic dispatch and its
ability to extend functionality of a tree of objects.

In lanugages that do not support method overloading, the visitor pattern tends
to fall apart. Python is one of those languages. So, in an effort to have the
same effect in Python, here's some code that does that. I'm just amazed at how
few lines it takes to create this effect.

{% highlight python linenos %}
# visit.py

import inspect

__all__ = ['on', 'when']

def on(param_name):
  def f(fn):
    dispatcher = Dispatcher(param_name, fn)
    return dispatcher
  return f


def when(param_type):
  def f(fn):
    frame = inspect.currentframe().f_back
    dispatcher = frame.f_locals[fn.func_name]
    if not isinstance(dispatcher, Dispatcher):
      dispatcher = dispatcher.dispatcher
    dispatcher.add_target(param_type, fn)
    def ff(*args, **kw):
      return dispatcher(*args, **kw)
    ff.dispatcher = dispatcher
    return ff
  return f


class Dispatcher(object):
  def __init__(self, param_name, fn):
    frame = inspect.currentframe().f_back.f_back
    top_level = frame.f_locals == frame.f_globals
    self.param_index = inspect.getargspec(fn).args.index(param_name)
    self.param_name = param_name
    self.targets = {}

  def __call__(self, *args, **kw):
    typ = type(args[self.param_index])
    d = self.targets.get(typ)
    if d is not None:
      return d(*args, **kw)
    else:
      issub = issubclass
      t = self.targets
      ks = t.iterkeys()
      return [t[k](*args, **kw) for k in ks if issub(typ, k)]

  def add_target(self, typ, target):
    self.targets[typ] = target
{% endhighlight %}

We can use it in the following way. Imaginge we have an abstract syntax tree
with nodes that accept a visitor. The following code would correctly print an
infix assignment expression.

{% highlight python linenos %}
import visit

class AbstractSyntaxTreeVisitor(object):
  @visit.on('node')
  def visit(self, node):
    """
    This is the generic method that initializes the
    dynamic dispatcher.
    """

  @visit.when(BaseNode)
  def visit(self, node):
    """
    Will run for nodes that do specifically match the
    provided type.
    """
    print "Unrecognized node:", node

  @visit.when(AssignmentExpression)
  def visit(self, node):
    """ Matches nodes of type AssignmentExpression. """
    node.children[0].accept(self)
    print '='
    node.children[1].accept(self)

  @visit.when(VariableNode)
  def visit(self, node):
    """ Matches nodes that contain variables. """
    print node.name

  @visit.when(Literal)
  def visit(self, node):
    """ Matches nodes that contain literal values. """
    print node.value
{% endhighlight %}

Raw code available at [visit.py](/assets/visit.py).
