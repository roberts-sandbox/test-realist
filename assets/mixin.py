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
