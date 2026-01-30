This is a small project. It looks simple but took me a while as I had to go through and breakdown the concepts of pagination, sorting, filtering, order, skip, limit and every other word you find in this code.

I started first with the understanding limit as to me, it is the easiest to grasp of all the terms I came accross. you can return your data, limit it and it will produce something, that's progress.

Next, I built into it the offset which in the argument is presented as "skip". It took a minute to corelate these words as I have learnt the theory without much mention of skip in the tutorials I watched. 

Then I added order and sorting. These two were easy to combine - didn't take too much racking of my brain. 

With on and off days, this topic took me about a day and two coding sessions to get. This is the second code.

You can return your values with query.offset(ski"p_value).limit(limit_value).all() 
