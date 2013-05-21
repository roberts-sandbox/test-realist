---
layout: post
title:  mysql and the Leap Second
tags:   mysql, linux

synopsis: Lazy administration led to "server meltdown."
---
I admit: I don't pay attention to my Linux servers like I should. They have
lulled me into a false sense of security due to their stability. This morning,
though, my monitoring app sent an email to me. A snippet:

> The VM XXXXXX has exceeded the notification threshold (90) for CPU Usage by
> averaging 90.8% for the last 2 hours.

Yikes!

Log on.

{% highlight html %}
: top
{% endhighlight %}

What the? `mysqld` sitting at 87%. Um, ok...

{% highlight html %}
: sudo mysqladmin shutdown

Can't shutdown process mysqld
Can't shutdown process mysqld
Can't shutdown process mysqld
Can't shutdown process mysqld
Can't shutdown process mysqld
Can't shutdown process mysqld
Can't shutdown process mysqld
Can't shutdown process mysqld
...
{% endhighlight %}

Wow. Reboot. All is well.

Yep, mysqld choked on the leap second.

Stupid leap second. Stupid mysql.

Time to switch to SQL Server Azure.
