---
layout: post
title: PNG Converter (Updated 02-22-2014)
date: 2014-01-11 10:00:00 MST
categories : [articles]
root: ../../../../..
---
I was recently downloading my iPhone pictures and adding them to Lightroom. Lightroom can't handle `PNG` files, which occur occasionally in my camera roll when I take a screenshot. It is easy to convert them into `JPG`s but I noticed that the creation and modified date are set to the current date and time, not the date and time that the `PNG` was created. This is typically not a problem except that it changes the ordering and flow of my iPhone pictures. I don't want a bunch of screenshots from my iPhone all clumped together showing that they were just created. I decided to write a small bash script to fix this.

<!-- more -->

Like I said before, converting from `PNG` to `JPG` is trivial with [ImageMagick](http://www.imagemagick.org/script/index.php):

{% highlight bash %}
convert file.png file.jpg
{% endhighlight %}

The challenging part is to change the creation and modified date. Basically, we need the original date (using `stat`) of the `PNG` and change the date of the new `JPG` image (using `touch`). Some parsing needs to be done to get the time from `stat` and then the date needs to be converted into something that `touch` can understand. I am sure there are many other ways to do this, but this is what I came up with in an afternoon.

{% highlight bash %}
for i in *.png; do
    # Get the filename without the extension
    file=${i%.*}

    png="$file.png"
    jpg="$file.jpg"

    # Convert from PNG to JPG
    convert "$png" "$jpg"

    # Get original time of PNG
    orig_time=$(stat "$png" | cut -d '"' -f 4)

    # Some time formatting needs to be done
    change_time=$(date -jf "%b %d %H:%M:%S %Y" "$orig_time" +"%Y%m%d%H%M.%S")

    # Change the time of the JPG
    touch -mt $change_time "$jpg"
done
{% endhighlight %}

This script converts all `PNG` files in a folder, but it could easily be modified to only convert a specified file.

I think this script will come in handy beyond converting screenshots from my camera roll. It feels more complete to be able to convert images and keep all of the metadata about that image the same.

**Update (02-22-2014)**: I fixed a few problems with the script. It would fail if file names had spaces in them.

