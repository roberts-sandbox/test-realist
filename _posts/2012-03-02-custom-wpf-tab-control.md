---
layout: post
title:  Google Chrome-Like WPF Tab Control
tags:   GUI, widget

synopsis: An introduction to a new GitHub project and a call for participation.
---

# {{ page.title }}

{{ page.synopsis }}
{: .subtitle }

-----

Yesterday, I pushed my initial import of a Google Chrome-like tab control for
WPF to a new GitHub
[repo](https://github.com/realistschuckle/wpfchrometabs "WPF Chrome Tabs").
I have it rendering the look of the tabs and some *very* rudimentary dragging
of the tabs. I don't like the implementation of the dragging, yet, so I'll
have to fix that.

I've released it under my favorite FOSS license, the MIT license. Feel free to
make a million dollars off of it, use it in your commercial software, or
whatever. However, if you do make a million dollars off of it, please send a
little my way. Help support FOSS.

(This project's for you, eb&#178; and DrH. :)

# The implementation

Right now, the functionality for this custom tab control lives in three 
coöperating classes.

__ChromiumTabControl__
: This is the tab control class that users would put in their XAML. Like the
.NET `TabControl`, it inherits from `Selector` found in the
`System.Windows.Controls.Primitives` namespace. It maintains the
``SelectedContent`` shown by the tab control, provides the default
look-and-feel as found in **Themes\Generic.xaml**, and manages the z-index of
the children so that the selected tab appears on top and the overlap of tabs
appear in reverse order of their position in the tab control's child list.

__ChromiumTabPanel__
: This custom layout panel provides the layout logic for the tabs at the top
of the control. Right now, it merely makes each tab 100 pixels wide and draws
the line along the bottom of the tabs. I believe that, as this project
matures, it will become responsible for handling tab movement and
coördinate with the **ChromiumTabControl** to reorder children on drag
complete.

__ChromiumTabItem__
: This provides the wrapper for children foudn in the **ChromiumTabControl**.
Like the ``TabItem`` found in ``System.Windows.Controls``, it inherits from
``HeaderedContentControl``. Its default representation, as found in the
**Themes\Generic.xaml** file, represents itself as just the tab contained by
the **ChromiumTabPanel**. Right now, it initiates and tracks the mouse
movement, but as I alluded to in the description of **ChromiumTabPanel**, that
specific responsibility will move out of this class. It resuses the
`Selector.IsSelected` dependency property to mark its selection in the tab
control.

To get this far, I used the excellent
[WPF: TabControl Series](http://blogs.intuidev.com/post/2010/01/25/TabControlStyling_PartOne.aspx)
as a starting point and, then, the decompiled IL from the
*PresentationFramework* assembly that comes with WPF. I didn't imagine the
amount of internal plumbing found in the ``TabControl`` and its associated
classes that Microsoft decided to keep internal to the WPF assembly. It
disappointed me, somewhat, because that functionality would have made my life
a lot easier and I could not understand why they decided to not expose it.

# Want to help?

If so, then follow these easy steps.

1. Download and install Google Chrome (if you haven't already).
1. Run Google Chrome. Play a lot with the tabs to get their behavior firmly
   in your mind.
1. Fork the **wpfchrometabs** repository and make changes that implement some
   of the behavior that you see in Google Chrome that does not yet exist in
   **wpfchrometabs**.
1. Gerneate a pull request.

Make small changes that address a specific part of the Google Chrome interface
behavior. I'll ignore "big" pull requests. :)
