---
layout: post
title:  jekyll&apos;s New Draft Feature
tags:   blog, jekyll

synopsis: In which I note the new feature of jekyll that I really like.
---
I just updated this site to use [jekyll](http://jekyllrb.com) v.1. It builds my
site faster which is good during the local development of a new posting. It also
has better messages about the build, including a "done" indicator which the
last version I ran did not have. Here's some actual output from saving this
file:

> Regenerating: 1 files at 2013-05-17 11:35:36 ...done.

That's awesome.

The best feature, by far, is the support of the `_drafts` folder that contains
works in progress. Previously, you had to specify the date of the post for a
future date and use the `--future` option to get those included in the site
build. Too much work!

Now, just put a new markdown document in the `_drafts` folder and they show up
at the top of the list using the file's last modified time. Awesome!

If you have a blog and want to use something other than Wordpress, try out
[jekyll](http://jekyllrb.com) and use [GitHub Pages](http://pages.github.com) to
host the content.

[Easy peasy lemon squeezy](http://www.newser.com/off-the-grid/post/223/caution-do-not-read-the-words-easy-peasy-lemon-squeezy.html)!