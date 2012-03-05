---
layout: post
title:  ChromeTabControl and Visual Children in WPF
tags:   GUI, widget

synopsis: A rename, some functionality, and an interesting feature of WPF.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

I've renamed the classes, projects, and solution for the project because I
didn't want to infringe on Google's IP. Thank you, **philipmat**, for pointing
out their trademark and thank you, Google, for letting me search out the
particulars of your intellectual property.

Since Friday, I've committed

* Changed mode on most files. Make resizing work correctly.
* Make the unselectable tab selectable (a tab with no ChromeTabItem as the
child)
* Make the little round button for closing
* Remove objects from the mapping dictionary to prevent "memory leaks"
* Now tabs close nicely for the tab control
* AddTab/RemoveTab functionality demonstrated
* Moved the responsibility of dragging tabs from the tab item to the tab panel
* Added "Close selected tab" button on test window
* Draw the "add tab" button and have it react to mouse over for color change
* Wire up the add button to add a tab

Those last two commits demonstrated a feature that I knew about WPF but never
had use to exercise: the difference between the logical tree and the visual
tree.

Right now, the `ChromeTabPanel` acts as the item host for the
`ChromeTabControl` which means that the `ChromeTabPanel` acts as the panel
that displays the children on behalf of the `ChromeTabControl`. In this case,
that means a lot of `ChromeTabItem`s.

With that coöperation occuring, the content of `ChromeTabPanel`'s `Children`
property contains the enumeration of `ChromeTabItem`s that appear as the tabs
thanks to the `Style`s found in the **Generic.xaml** file. While that works
well, I wanted the `ChromeTabPanel` to also manage and display a button that
the user could click to add a new tab, just like you find in Google Chrome.
I didn't want to add that to the `Children` list because that would pollute
the content and intent of that collection. I needed something else. I needed
the visual tree instead of the logical tree.

First, I defined a new `Style` for the add button in the XAML theme file.

{% highlight xml %}
<Style x:Key="{ComponentResourceKey TypeInTargetAssembly={x:Type local:ChromeTabPanel}, ResourceId=addButtonStyle}" TargetType="{x:Type Button}">
  <Setter Property="Template">
    <Setter.Value>
      <ControlTemplate>
        <Grid SnapsToDevicePixels="True">
          <Path Fill="{TemplateBinding Background}"
                Stretch="Fill"
                Stroke="#FF999999"
                Data="M36.904667,19.333333 C42.238,19.25 36.238,0.5 34.863116,0.5 23.863116,0.5 19.613032,0.5 2.8630319,0.5 -3.2202511,0.5 4.0712139,19.416667 6.5711261,19.416667 15.593514,19.416667 28.609259,19.462949 36.904667,19.333333 z" />
        </Grid>
      </ControlTemplate>
    </Setter.Value>
  </Setter>
</Style>
{% endhighlight %}

Then, I created a field for it and its size in the `ChromeTabPanel` class and
initialized it in the constructor with the style from the theme file.

{% highlight csharp %}
ComponentResourceKey key;
key = new ComponentResourceKey(typeof(ChromeTabPanel), "addButtonStyle");
Style addButtonStyle = (Style)this.FindResource(key);
this.addButton = new Button { Style = addButtonStyle };
this.addButtonSize = new Size(20, 12);
{% endhighlight %}

Now, I want it to pariticpate in the measure/arrange phase of WPF rendering.
I added the calculations to the `ArrangeOverride` and `MeasureOverride`
methods in the `ChromeTabPanel`.

{% highlight csharp %}
protected override Size ArrangeOverride(Size finalSize)
{
  // Other stuff removed for brevity
  double left = offset + overlap;
  double top = finalSize.Height - this.addButtonSize.Height) / 2;
  Point location = new Point(left, top);
  this.addButtonRect = new Rect(location, this.addButtonSize);
  this.addButton.Arrange(this.addButtonRect);
  // Other stuff removed for brevity
}

protected override Size MeasureOverride(Size availableSize)
{
  Size resultSize = new Size(0, availableSize.Height);
  // Other stuff removed for brevity
  this.addButton.Measure(this.addButtonSize);
  resultSize.Width += this.addButtonSize.Width;
  return resultSize;
}
{% endhighlight %}

At this point, I really thought it would work. I've included the add button in
the measure/arrange cycle.

It did not work. Sadness descended upon me like a unkindness of ravens. :(

Then, hope struck me. I found the ``Visual.AddVisualChild`` method! Woot! I
added a call in the constructor to add the button as a visual child. And...

...nothing. What the? Off to Googleland, again, where I found
[this thread on MSDN](http://social.msdn.microsoft.com/Forums/en-AU/wpf/thread/f643b9d7-4434-4044-b23f-779e648da1f9).
Turns out that `AddVisualChild` really doesn't do anything except *send a
notification to the base class that you've acquired a new child in the
visual element's child collection!* Kind of a badly named method, if you ask
me.

The thread suggests, instead, overriding the `VisualChildrenCount` property
and the `GetVisualChild` method. I did that with the expectation that the
add button should always appear as the last visual child in the visual
children collection.

{% highlight csharp %}
// In ChromeTabPanel
protected override int VisualChildrenCount
{
  get { return base.VisualChildrenCount + 1; }
}

protected override Visual GetVisualChild(int index)
{
  if (index == this.VisualChildrenCount - 1)
  {
    return this.addButton;
  }
  else if (index < this.VisualChildrenCount - 1)
  {
    return base.GetVisualChild(index);
  }
  throw new IndexOutOfRangeException("Not enough visual children in the ChromeTabPanel.");
}
{% endhighlight %}

And, by Grabthar's hammer, by the suns of Warvan, it worked! Now, I have a
visual but not a logical child.

![add button](/img/chrometabs-addbutton.png)

The downside to this implementation: I have to do the mouse event handling
because routed event propagation occurs only in the logical tree. Not a big
deal. I have introduced a refactoring opportunity with the wedged-in
implementation that currently exists.

Again, if you feel like helping out or reviewing the code for suggestions,
head over to the
[GitHub repo](https://github.com/realistschuckle/wpfchrometabs)
and do the magic that we call "development!"
