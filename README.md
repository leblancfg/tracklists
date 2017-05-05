# tracklists
 :arrow_forward: Little CLI program that makes skippable YouTube tracklists out of duration-based ones

You've probably stumbled onto your share of YouTube albums that either didn't have a skippable tracklist, or worse yet, one that is based on track duration rather than total running time. This little CLI tool aims to remedy that problem by reading in what's in your clipboard -- regardless of platform! -- and spitting out a proper tracklist.

    * copy a duration-based tracklist to clipboard *
    $ tracklist
    * print out abeautiful, skippable tracklist *

## Installation
Well that's just a little nosy, you should know. I'm still working on this! Gimme a minute, I'm trying to get it on PYPI, to be easily installable directly from `pip`.

## Use
There's thankfully very little to say, all you need is a shell. On macOS or most shades of Linux, will read directly from your clipboard, as long as your terminal allows it. Fear not, most modern terminals do. On Windows, hit `CMD` from the Start Menu search and that's it. **tracklists** is meant to be used as a single call in your shell, regardless of your operating system. A simple:

    $ tracklist
    
Should suffice to take what's in your clipboard, and print out a copyable version, as long as it's a valid duration-based tracklist.



