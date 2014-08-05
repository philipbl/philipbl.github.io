---
layout: post
title: Time Parser
date: 2013-09-24 14:13:00 MST
categories : [articles]
tags: [Projects]
root: ../../../../..
---
Since I started working at [Xandem][8888-001], I have to keep track of the hours I work and enter them into a time card. I have no problem writing the times I come and go, but it is annoying to then have to calculate how many hours I actually worked. Sometimes, the amount of hours can get complicated, say for example, you come into work in the morning, leave in the afternoon to run some errands, come back in the evening, and take a 10 minute break. The math is not difficult, it is just monotonous.

I decided to create a script that could take care of this repetitive task for me. As I thought more about how to accomplish this, I noticed that I have a specific way of writing the time that I worked. On a normal day, my time worked might look something like "8:05 AM to 4:12 PM". If I take a lunch, then it might look like "8:05 AM to 4:12 PM - 45 min". I wanted this script to be flexible enough that I could handle any combination of time ranges ("8:05 AM to 4:12 PM") and time adjustments (+/- 45 min). As I thought about how I would parse this time text, some of the things I learned from my [compilers class][might] started coming back to me. I decided that I would try to implement the ideas from that class (as well as I could remember).

<!-- more -->

### Grammar
First, I needed to come up with a grammar for my "time language". I wrote out a bunch of examples of how I would want to use this mini-language and decided on this[^1] :

{% highlight text %}
<COMPOUND_STATEMENT> : <STATEMENT> (and <COMPOUND_STATEMENT>)*
<STATEMENT> : <ABS_TIME> to <ABS_TIME> (<REL_OPERATOR> <REL_TIME>)*
<REL_OPERATOR> : -, +
<ABS_TIME> : XX:XX AM|PM
<REL_TIME> : X+ min|hour|mins|hours
{% endhighlight %}


### Tokenizing
Next, I needed some way of tokenizing the input into the tokens of the grammar. After doing some research, I found an [article][evanfosmark] that describes an undocumented class, `Scanner`, in the `re` module. The article does a good job of describing how the `Scanner` works and gives an example on how to use it, but essentially you can give the `Scanner` class a list of regular expression and function pairs. When it matches the given regular expression, it calls the associated function. The function can return anything, but in terms of tokenizing, it would return some kind of token to be used for parsing later on. Here is the scanner that I came up with for my time parsing problem:

{% highlight python %}
# tokenize functions
abs_time = lambda scanner, token: ("ABS_TIME", token)
rel_time = lambda scanner, token: ("REL_TIME", token)
rel_operator = lambda scanner, token: ("REL_OPERATOR", token)
abs_operator = lambda scanner, token: ("TO") if token == "to" else ("AND")

# tokenizer
scanner = re.Scanner([(r"(0?[1-9]|1[0-2]):[0-5][0-9]\s*?(AM|PM)", abs_time),
                      (r"\d+\s*?(mins|min|hours|hour)", rel_time),
                      (r"to", abs_operator),
                      (r"and", abs_operator),
                      (r"-", rel_operator),
                      (r"\+", rel_operator),
                      (r"\s+", None)])

tokens, remainder = scanner.scan(input_)
{% endhighlight %}

The results of "8:05 AM to 4:12 PM - 45 min" look like: 

{% highlight python %}
[('ABS_TIME', '8:05 AM'), 
  'TO',
 ('ABS_TIME', '4:12 PM'), 
 ('REL_OPERATOR', '-'), 
 ('REL_TIME', '45 min')]
{% endhighlight %}


### Parsing
Now that we have a list of tokens, we need to combine them together to form some kind of output, in my case, the total hours worked. There are many different ways of doing this, but the general process I followed was removing items from the stack (list of tokens), verifying that they are the tokens I am expecting (based on the grammar), and  combining them together. For example, to parse part of a `<STATEMENT>`, I had

{% highlight python %}
def process_statement(tokens, total_time):
    # removing items from the stack
    time1 = tokens.pop()
    op = tokens.pop()
    time2 = tokens.pop()

    # checking to make sure all the tokens are good
    if time1[0] != "ABS_TIME": raise Exception
    if op != "TO": raise Exception
    if time2[0] != "ABS_TIME": raise Exception

    # combine tokens together
    total_time += calc_time_diff(time1[1], time2[1])
    return process_next_stament(tokens, total_time)
{% endhighlight %}


### End Result
To stay true to my compilers class, I tried to write this script as functional as I could (i.e. no loops, no global state, etc.). I think the script turned out well. It was fun and challenging to apply the principles of lexing and parsing to a small problem that I face almost every day. 

The script can be [downloaded here][github] or viewed on [github][github 2]. The script is ready to be used in a [Editorial workflow][0213-001] or as an OS X Service.

### [Download OS X Service][service]




[^1]: I do not profess to being a programming language expert. As a result, the grammar and other ideas were my best effort to come up with something that worked. In no way is this the "best" or the "only" way to solve this problem.


[8888-001]: https://www.xandem.com/ "Xandem Technology: Xandem Synergistic Sensing"
[0213-001]: http://omz-software.com/editorial/ "Editorial for iPad"
[evanfosmark]: http://www.evanfosmark.com/2009/02/sexy-lexing-with-python/
[github]: https://gist.github.com/philipbl/6552329/raw/ec369685f7108f2752107511dab0b9fb9f3dc103/time_parser.py
[github 2]: https://gist.github.com/philipbl/6552329
[might]: http://matt.might.net/teaching/compilers/spring-2013/
[service]: {{ page.root }}/resources/Time%20Parser.workflow.zip 

