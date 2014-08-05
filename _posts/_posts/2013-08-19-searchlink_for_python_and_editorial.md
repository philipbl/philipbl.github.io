---
layout: article
title: SearchLink for Python and Editorial
date: 2013-08-19 08:10:00 MST
categories : [articles]
tags: [Projects]
---
I have been using [SearchLink][8145-001] for a few months and love it. If you have never used it, you should read more about it on [Brett Terpstra's Project Page][8145-001]. To summarize, SearchLink allows you to write Markdown links using search terms instead of a URL. This script then goes through, uses its magic to search for those terms online and switches them out with the correct URL. It is a pretty powerful script and helps save a lot of time when you are writing in Markdown.

A new iPad text editor app recently came out called [Editorial][editorial-app]. In my opinion, this is the best text editor for the iPad to date. There have already been several great [reviews][8145-002] on it, so I will spare you the details. I just want to talk about one amazing feature and how it relates to SearchLink--it has the ability to run Python inside of Editorial. This makes me dance for joy! iPad apps always seem so limited and constrained; it feels good to think that there could be an iPad app that will let me run Python code for some advanced automation. My first thought was how awesome it would be to have SearchLink on the iPad. The problem is that SearchLink is written in Ruby and Editorial only works with Python. I know and love Python, so decided to take on the challenge of porting it over to Python and see if Editorial could handle it. 

Over the weekend, I was able to port SearchLink from Ruby to Python smoothly. There might be a few bugs in the Python version, but so far it is looking pretty good. I did all of my programming and testing on my computer and as a last step, copied it over to Editorial. Everything worked perfectly -- SearchLink acted exactly how it would have on a computer. 

I stored the code for SearchLink.py in a [gist][github]. The Editorial workflow can be downloaded **[here][appspot]**. Hopefully this will be as useful to you as it is to me. Let me know if you have any suggestions or if you find any bugs. 

And special thanks to Brett Terpstra for creating this crazy, awesome script in the first place. If you haven't checked out his [other projects][brettterpstra], you definitely should. 

[appspot]: http://editorial-app.appspot.com/workflow/5803016212971520/Id9R-MLqQ4g
[brettterpstra]: http://brettterpstra.com/projects/
[editorial-app]: http://editorial-app.com/
[github]: https://gist.github.com/philipbl/6257916
[8145-001]: http://brettterpstra.com/projects/searchlink/ "SearchLink - BrettTerpstra.com"
[8145-002]: http://www.theverge.com/2013/8/15/4623714/editorial-ipad-text-editor-hands-on "Editorial for iPad is the new text editor to beat | The Verge"


