---
layout: post
title:  Running nunit-console Under mono on OSX
tags:   mono, nunit

synopsis: In which I share how to run nunit-console under mono.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

I continue to program in C# even though I don't consider it my favorite
language. The experience of starting a VM on my Macbook Pro to use Visual
Studio 2010 on Microsoft Windows 7 quickly paled. I downloaded and installed
Monodevelop 2.8.5 so that I could compile C# without a VM.

For example, I use Monodevelop to work on
[sqlcop](https://github.com/realistschuckle/sqlcop).

Unfortunately, on OSX, the `System.Windows.Forms` namespace draws the GUI
through functionality of `System.Drawing`. When I execute the GUI runner for
NUnit, I find it unacceptably slow. I want my unit tests to execute *fast*.

The `nunit-console.exe` runner does execute the tests fast. However, getting
the darn thing to run can be quite a hassle. Follow these easy steps to run
`nunit-console.exe` under Mono on OSX.

* Add the path to your installation of ./net-2.0/framework to `MONO_PATH`.
* Change the working directory of your command line to the output directory
  for your tests.
* Run `mono --debug <relative path to nunit-console> --nologo --noshadow <test dll>`

And that should do it. Test with clarity!
