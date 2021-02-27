
## Shooting Statistics
___
To measure if the bubble environment had an affect on player's shooting percentages, I looked at FT, FG, 3P and TS makes, attempts, and percentages.

I charted the distributions from the 2020 Regular Season, with it's mean, compared to the distribution from the 2020 Post Season, also with it's mean. Though the 2020 Post Season contained almost 1/6 of the data of the 2020 Regular Season, their distributions lined up very neatly and similarly

I also charted the distributions of the average differences, from the 2019 Regular to Post Season, and the 2020 Regular to Post Season. By charting the deltas from Regular to Post Season, I was looking for anything interesting in terms of the rate of change, if the Bubble provided any impact on that change. 

## Offensive Rating (ORtg) and Defensive Rating (DRtg)
___
*"This game has always been, and will always be, about buckets" - 11x NBA Champion, Bill Russell*

https://www.youtube.com/watch?v=-xYejfYxT4s

I chose to focus on these two metrics, as they provide a succint look into how well a team is performing. Simply put, you need to score more points than the other team to win. Are players more focused and does a team "get better" (ORtg goes up or DRtg goes down) in the Post Season? Or do they crumble under the pressure and choke away their chance at the championship (ORtg goes down or DRtg goes up)?

Because the Bubble provided an isolated environment, teams no longer had to spend time travelling. I charted the change in Pace, of teams in the Post Season versus their Regular Season Pace. **Pace** is defined as an estimate for the number of possessions per 48 minutes by a team. Were teams more well rested, were they able to perform at a peak level (pace wise), are they hustling for longer periods of time? 


**H0: Average FT% inside the Bubble (Home/Away) is the same as the FT% from the 2020 Regular Season**

**HA: Average FT% inside the Bubble (Home/Away) is different as the FT% from the 2020 Regular Season**

Based on the distribution plots, displayed an increase in FT% for the 2020 Post Season, when performing a Student's T-test with Average FT% from 2020 Regular Season Away games, I observed a p-value of 0.472.

Using an alpha of 0.05, based on the p-values observed, I fail to reject the null hypothesis that the Average FT% inside the Bubble (Home/Away) is the same as the FT% from the 2020 Regular Season

## Offensive Rating (ORtg) 
___
**H0: ORtg is the same in the Bubble as the 2020 Regular Season**

**H0: ORtg is different in the Bubble as the 2020 Regular Season**

Since this data set was substantially smaller than the previous data sets, I plotted the Playoff Teams's difference of their ORtg from their Regular Season ratings. 

And since I was working on a small data set with the same indexed values, Teams, and was dealing with a difference between two samples (Post Season and Regular Season), I concluded a Mann-Whitney U test would be appropriate, using an alpha of 0.05. 

The Mann-Whitney U test produced a p-value of 0.076, so I fail to reject the null hypothesis that ORtg is the same in the Bubble as the 2020 Regular Season.

##  Defensive Rating (DRtg)
___
**H0: DRtg is the same in the Bubble as the 2020 Regular Season**

**H0: DRtg is different in the Bubble as the 2020 Regular Season**

Since DRtg is a positive number, I captured the positive difference (the Team is allowing more points to be scored on them on defense) as a negative value. Again, since this data set was substantially smaller than the previous data sets, I plotted the Playoff Teams's difference of their ORtg and DRtg from their Regular Season ratings. 

As stated previously, working with a smalle set of data with the same indexed values, Teams, and was dealing with a difference between two samples (Post Season and Regular Season), I concluded a Mann-Whitney U test would be appropriate, using an alpha of 0.05. 

The Mann-Whitney U test produced a p-value of 0.025, so I reject the null hypothesis that DRtg is the same in the Bubble as the 2020 Regular Season.