---
layout: post
title:  Comments Check-In Policy with Visual Studio 2012 and git-tfs
tags:   visual studio 2012, git-tfs

synopsis: Getting the now-hidden check-in policy to work with git-tfs.
---
Once upon a time, the "Require a Changeset Comments" check-in policy for TFS
came in the TFS Power Tools. In Visual Studio 2012, they rolled that policy into
the Visual Studio distribution. Now, the check-in tool from git-tfs cannot find
it. To solve that problem, you need to make the check-in policy available to
git-tfs.

Copy `Microsoft.TeamFoundation.VersionControl.Controls.dll` from

    C:\Program Files (x86)
      Microsoft Visual Studio 11.0
        Common7
          IDE
            CommonExtensions
              Microsoft
                TeamFoundation
                  Team Explorer

to your `git-tfs` installation directory. That should allow the check-in tool to
find the policy.
