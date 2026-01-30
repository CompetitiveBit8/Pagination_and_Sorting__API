This is a small project. It looks simple but took me a while as I had to go through and breakdown the concepts of pagination, sorting, filtering, order, skip, limit and every other word you find in this code.

I my understanding started clicking with limit because it was the easiest to grasp of all the terms I came accross. You can return your data, limit it and it will produce something, that's progress. Limit is the total munber of items you want returned at once (in a page)

Next, I built into it the offset which in the argument is presented as "skip". It took a minute to corelate these words as I have learnt the theory without much mention of skip in the tutorials I watched. 
Offset or skip is the number of of values to skip over to make a page. This is never decided as a query by the user in order to avoid overlap of displayed values. It is the page number that is given to the user to decide which is then used to calculate the offset values using the formula:
                 skip = ( page - 1 ) * limit

Then I added order and sorting. These two were easy to combine - didn't take too much racking of my brain. For order, you use it to decide the ascending or descending order of the attribute you want to view your datathrough. You use the getattr built-in, python function to fix the ordering of all these values.

With on and off days, this topic took me about a week and three coding sessions to get. This is the second code.

You can return your values with query.offset(skipValue).limit(limitValue).all() 
