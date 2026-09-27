-- How can you retrieve all the information from the cd.facilities table?

select facid,
       name,
       membercost,
       guestcost,
       initialoutlay,
       monthlymaintenance
from facilities;

-- You want to print out a list of all of the facilities and their cost to
-- members. How would you retrieve a list of only facility names and costs?

select name, membercost
from facilities;

-- How can you produce a list of facilities that charge a fee to members?

select facid, name, membercost, guestcost, initialoutlay, monthlymaintenance
from facilities
where membercost > 0;

-- How can you produce a list of facilities that charge a fee to members,
-- and that fee is less than 1/50th of the monthly maintenance cost?
-- Return the facid, facility name, member cost, and monthly maintenance
-- of the facilities in question?.

-- NOTES FROM ME: WHILE RUNNING THIS FIRST TIME I DIDN'T CHECKED FOR 0
-- WHEN WRONG RESULT CAME THEN I UNDERSTOOD I NEED TO CHECK FOR THAT AS WELL

select facid, name, membercost, monthlymaintenance
from facilities
where membercost > 0
  AND membercost < monthlymaintenance / 50;


-- How can you produce a list of all facilities with the word 'Tennis' in their name?

-- NOTES FROM ME: WHILE RUNNING FIRST I MADE A SYNTAX ERROR, I  WROTE %Tennis% THEN GOOGLE SAID
-- IT SHOULD BE '%Tennis%'

SELECT facid, name, membercost, guestcost, initialoutlay, monthlymaintenance
from facilities
where name LIKE '%Tennis%';

-- How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.

-- NOTES FROM ME: IWROTE "where name LIKE '%2%';" IT WORKED BECAUSE OF DATA SET. I KNOW WRONG WAY OF DOING
-- HENCE CORRECT IT LATER TO USE IN()

select facid,
       name,
       membercost,
       guestcost,
       initialoutlay,
       monthlymaintenance
from facilities
where facid IN(1,5);

-- How can you produce a list of facilities, with each labelled as 'cheap' or 'expensive' depending on if their monthly
-- maintenance cost is more than $100? Return the name and monthly maintenance of the facilities in question.

-- NOTES FROM ME: I KNEW TO THAT I NEED TO USE CASE BUT DON'T KNOW SYNTAX HAD TO TAKE FULL HINTS AND SOLUTION

SELECT name,
       case
           when (monthlymaintenance > 100) then
               'expensive'
           else
               'cheap'
           end as COST
from facilities;

