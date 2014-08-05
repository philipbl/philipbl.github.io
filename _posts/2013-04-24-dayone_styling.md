---
layout: post
title: Day One Custom Styling
date: 2013-04-24 10:51:00 MST
categories : [articles]
tags: [Day One]
---
I love [Day One][dayone]. It is by far my favorite journaling app. I use it to take notes in my classes, record thoughts about my research, and anything else that I feel like I need to record.

One thing that I wish Day One would add is customizable styling. Sometimes it is nice to change how the different headers look and their sizes or what colors are being used for links. After digging around, I found that there are some ways you can change the styling of Day One, but it involves modifying the contents of the app.

<!--more-->

To change the styling, you need to know a little about CSS. Since entries in Day One use [Markdown][md] which eventually gets boiled down to HTML, CSS is used to style an entry. The file that you want to change is `/Applications/Day One.app/Contents/Resources/DayOne.css`. From what I can tell, this file controls most of the styling for an entry. The easiest way to get this directory is to use Terminal.app,

{% highlight bash %}
$ cd /Applications/Day One.app/Contents/Resources/
$ open .
{% endhighlight %}

but if you don't feel comfortable with that you can always navigate to your Applications folder and then right click on `Day One.app` and select "Show Package Contents".

Once you have `DayOne.css` open, you are able to control styling for an entry in Day One. The first thing that I changed was the headers (`h1`, `h2`, `h3`, etc.). For example, I like a line at the bottom of my `h1` header. To do this I just replaced the old `h1` and `h1.title` with

{% highlight css %}
h1 {
    font-size: 1.5em;
    font-weight: 200;
    line-height: 1.3;
    margin: 12px 0 7px;
    border-bottom: 1px solid #ddd;
}

h1.title {
    font-size: 1.5em;
    font-weight: 200;
    color: #26748F;
    line-height: 1.3;
    margin: 11px 0 16px;
    border-bottom: 1px solid #ddd;
}
{% endhighlight %}

I also changed some of the sizes of the headers and what font is used for code blocks to fit my preferences. For these changes to take effect, you must restart Day One. There are tons of other things you can change that I haven't even touched. The possibilities are endless!


**Update (5/15/13)**: Looks like Day One is headed in the direction of custom styling. The designer of Day One, [Paul Mayne][paul], has created a [github repository][git] that shows the correspondence from markdown to HTML, which is important to know when customizing the CSS of an entry.

[dayone]: http://dayoneapp.com
[md]: http://daringfireball.net/projects/markdown/
[paul]: http://paulmayne.org
[git]: https://github.com/bloom/DOMarkdown
