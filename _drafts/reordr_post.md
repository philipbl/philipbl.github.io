I have been slowly been uploading all of my pictures to Flickr. I am using Flickr as a last resort back up solution and as a way to view my pictures from pretty much anywhere (iOS, AppleTV, web). Flickr's organization (or lack of it) has always bugged me. I don't like that the photo stream sorts by the time the picture was uploaded, not the time the picture was taken. I'm not sure if that is a desirable behavior for anyone, but that's the way it is.

Show picture of horrible interface

Similar to the photo stream, sets[^1] are organized by when a picture was last uploaded. Given that I have over 100 albums and the old Organizr, I knew that I needed to find a better way. Looking through the Flickr API, I was happy to find that there is a way to change the order of the sets. I did a courtesy Google search to see if someone has made something that fixes the ordering and found nothing[^2], so I wrote up a quick Python script to fix the problem.

The script has two options, get and set. get returns a list of all of the sets. set takes a list of photo set IDs as input.

```
reordr --get > order.txt
```

... mess with ordering of order.txt[^3]

```
reordr --set < order.txt
```

And just like that, you have much better control over the ordering of your sets.

[^1]: Or albums. I can't keep track of the difference if there is any.

[^2]: I was in a programming mood, so my search was not exhaustive.

[^3]: I used a little bash scripting to make this process easier. My private albums start with the date of the set (YYYY-MM-[DD][-description]). I used sort to get all of these in chronological order.
