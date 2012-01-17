---
layout: post
title:  How To Run Python.NET on Mac OS X with Mono
tags:   programming

synopsis: In which I set up Python.NET with Python 2.7 and Monodevelop on Lion
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

__Install subversion__
: I used [homebrew](http://mxcl.github.com/homebrew/).

__Install Python for .NET Source__
: Pick a nice directory for installation. I put it in ~/dev/pythonnet. I ran
  these commands.
{% highlight bash %}
mkdir -p ~/dev/
cd ~/dev
svn co https://pythonnet.svn.sourceforge.net/svnroot/pythonnet/trunk pythonnet
{% endhighlight %}

__Install Monodevelop__
: I installed
  [version 2.8.5](http://download.xamarin.com/monodevelop/Mac/MonoDevelop-2.8.5.dmg)
  because they don't have a release for 2.8.5.1, yet.

__Open Python.NET Solution__
: Start Monodevelop, answer its stupid questions, and open the solution. I
  found mine at ~/dev/pythonnet/pythonnet/pythonnet.sln.

__Configure Build for Python 2.7__
: Double-click the "Python.Runtime" project to open its optiosn. In the 
  dialog that appears, select "Build > Compiler" from the navigation pane on
  the left. For each configuration in the Configuration dropdown, change the
  ``PYTHON26`` in the "Define Symbols" input to ``PYTHON27``.

![options](/img/pythonnet-mono-project-options.png "options")

__Link the Python Shared Library to the Test Output Directory__
: Create a softlink from ``libpython.2.7.dylib`` to ``libpython27.dylib`` in
  the output directory of the "EmbeddingTest" project.
{% highlight bash %}
mkdir -p ~/dev/pythonnet/pythonnet/src/embed_tests/bin/Release/
cd ~/dev/pythonnet/pythonnet/src/embed_tests/bin/Release/ libpython27.dylib
ln -s /System/Library/Frameworks/Python.framework/Versions/2.7/lib/libpython2.7.dylib 
{% endhighlight %}

__Patch the Import Unit Test__
: In the "EmbeddingTest" project, open the ``PyImportTest`` fixture. In the
  ``SetUp`` method, you will see on line 28 a line that looks like a path to
  a "tests" directory. You need to change that because Python on Mac OS X does
  not know about those backslashes. So, change it to the following. (I've
  already submitted a patch to the project, so you may not have to complete
  this step if they choose to apply it to the source.)
{% highlight csharp %}
char c = System.IO.Path.DirectorySeparatorChar;
string s = string.Format(@"..{0}..{0}..{0}tests", c);
{% endhighlight %}

__Build Solution__
: You know, CTRL+COMMAND+B.

__Run the Unit Tests One Fixture At A Time__
: This kind of blows. However, the Unix pipe used to communicate with the
  tests doesn't do well with the embedded cPython runtime. They should all
  pass.

Now, you can use Python.NET in your Mono development. Just remember to link
in that shared library or put it in your ``MONO_PATH`` environment variable.

