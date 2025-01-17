# Predicting NBA All-Stars


## Goal / Hypothesis
An issue in the world of sports fandom is always predicting what may happen. For betters, analysts, etc. People tend to use the same statistics to predict future outcomes. However, when predicting the future, there are always outside factors that play into what may occur. 

Our goal is to build a machine learning model that predicts the likelihood of an NBA player becoming an All-Star in the NBA. In order to become an All-Star starter  for the East or West teams, a player is selected by a weighted combination of fan, player and media voting (50%, 25% and 25% respectively). The reserves are chosen by a vote between the coaches. We will look to predict the probability that a draft eligible College Basketball player becomes an All-Star by analyzing which features of a player lead to future NBA success.



## Data Dictionary
The majority of the data descriptions can be found [here](https://www.basketball-reference.com/about/glossary.html#mp) with the remainder on Bart Torvik's [site](https://www.bigtengeeks.com/new-stat-porpagatu/).


## Executive Summary
We tried to predict the probability that a draft eligible college basketball player will become an NBA All-Star at some point in his career. This was accomplished by utilizing data scraping, data cleaning, Bayesian statistics, preprocessing and classification modeling. The data used for the analysis was pulled from two websites, [Basketball Reference](https://www.sports-reference.com/cbb/play-index/psl_finder.cgi?request=1&match=combined&year_min=2006&year_max=2019&conf_id=&school_id=&class_is_fr=Y&class_is_so=Y&class_is_jr=Y&class_is_sr=Y&pos_is_g=Y&pos_is_gf=Y&pos_is_fg=Y&pos_is_f=Y&pos_is_fc=Y&pos_is_cf=Y&pos_is_c=Y&games_type=A&qual=&c1stat=&c1comp=&c1val=&c2stat=&c2comp=&c2val=&c3stat=&c3comp=&c3val=&c4stat=&c4comp=&c4val=&order_by=pts&order_by_asc=&offset=0) and [Bart Torvik](http://barttorvik.com). The process of pulling/scraping the data from the Basketball Reference website for the NBA draft data, All-Star data and single season data can be seen in the **Data_Collection** folder of the repository. Bart Torvik's data was collected through a JSON file provided by Bart himself. The process of organizing that data can also be seen in the **Data_Collection** folder. 

We were able to collect data on 55,939 college basketball seasons. This value includes every player that has played college basketball since 2008. If an individual played in multiple seasons, then they will have multiple observations listed for each season. Something that we do not have the data for are International and high school athletes. College basketball players also make up more than 83% of the players in the NBA ([RPI Ratings](http://rpiratings.com/NBA.php)). In the data cleaning process, we identified which players were drafted and which made an All-Star game. We also reduced the dataset to only include the final season a player played in college. Including all seasons for a player could affect my target variable since the player will be listed multiple times as having made an All-Star game. The last season someone played in college tends to be their best performing season and is what's looked at most heavily by a team's front office. Ultimately, the dataset included 581 college basketball seasons with 30 of the seasons having been All-Star players. The data collected for each player includes many individual statistics for that season as well as information on where the player went to school, conference and physical measurements. 

Before building our model, we needed to understand the dataset in greater detail. In order to do this, we performed exploratory data analysis and used Bayesian MAP estimates to adjust certain features. We wanted to see what percentage of players made an All-Star game given a certain feature as well as what percentage of All-Stars had that feature. We also looked at the continuous features (players stats) by separating the data for players that have made an All-Star game and those who have not to see if there were any significant differences between the two. Before eliminating certain features that had overlap in their calculations, we calculated Bayesian MAP estimates to adjust several values. For example, **Free Throws Made (FTM)** and **Free Throws Attempted (FTA)** are used to calculate **Free Throw % (FT %)**. We adjusted the **FT %** using prior knowledge and a likelihood function before we dropped the **FTM** and **FTA** features. This provided us with a more accurate representation and helped account for players with far fewer attempts than other players. 

After completing EDA, we began the classification modeling process. We separated the data into a training and test set. The training data included players from 2008-2020 and the test set included college players from the 2020 NBA draft. We began by train/test splitting the training data after selecting features to include in the analysis. Then we began to build several classification models utilizing GridsearchCV to optimize for the best hyperparameters. Below is a list of the classification models used. 

- Logistic Regression  
- KNearest Neighbors 
- DecisionTree 
- RandomForest
- Adaboost

The best model had the highest accuracy and the lowest variance, but also had the most realistic and interpretable probabilities based off of prior knowledge. This model was then used to predict the All-Star probability on the 2019 test dataset.

## Limitations
- Size of dataset: Unfortunately we were only able to collect data going back to 2008. Ideally, I could collect data for more years.
- Unbalanced class: There have only been 30 college players drafted into the NBA that have made an All-Star game since 2008. Therefore, our target class is approximately 5% of our data. Given the already small size of our dataset, this could make it difficult for our model to learn enough information from our features to create an accurate prediciton. 


## Conclusions
Utilizing a random forest model after a train/test split, we were able to predict correctly if a player had become an All-Star at some point in their career 99% of the time and 94% on the test set. The model was slightly overfit and did not perform better than the baseline on the test set. This was not a surprise due to how unbalanced the target class was. However, when looking at the top 20 All-Star probabilities, it predicted the correct value 100% of this time. This even includes players such as Draymond Green who was drafted in the second round and Kyrie Irving who only played 11 games in his college career. Had the front office of a sports team utilized our model, it would have been unlikely that Draymond Green would've been taken at pick 35 in the draft.

When testing our model on unseen data, the 2019 drafted players, it predicted Zion Williamson to have the highest probability of becoming an All-Star. Zion Williamson was a transcendent player in college this past year and also happened to be the first player taken overall. The player with the second highest probability was Brandon Clarke from Gonzaga. He happened to be selected 21st overall which is not a range where All-Stars are typically taken. We will see soon enough if Brandon Clarke will have a similar career to Draymond Green and surprise the skeptics by becoming an All-Star. He is off to a good start as he was named the MVP of the NBA summer league this year.
 

## Next Steps
- Collect more data: This includes data going back further than 2008. It also includes data for new features. Some new features we'd like to include in our analysis are a players high school recruiting rank, number of wins in college and athletic measurements from the NBA combine. We'd also like to collect data on international players as well as players who were drafted straight from high school.
- We'd like to figure out a way to quantify the mental aspects of the game. It is good to know the on-court statistics of a player, but there are other off the court aspects which can lead to success. For example, knowing a players basketball aptitude to understand their personality and behavior can be critical to finding a successful player and one that is a fit for a specific team.
- In the future, we'd like to build out our analysis to predict which amateur basketball players will get drafted, their draft position and from that result find the probability that the drafted players will become All-Stars.

## Resources
- [Bart Torvik](http://barttorvik.com/playerstat.php?link=y&year=2019&top=353&start=20181101&end=20190501)
- [Basketball-Reference](https://www.sports-reference.com/cbb/play-index/psl_finder.cgi?request=1&match=combined&year_min=2006&year_max=2019&conf_id=&school_id=&class_is_fr=Y&class_is_so=Y&class_is_jr=Y&class_is_sr=Y&pos_is_g=Y&pos_is_gf=Y&pos_is_fg=Y&pos_is_f=Y&pos_is_fc=Y&pos_is_cf=Y&pos_is_c=Y&games_type=A&qual=&c1stat=&c1comp=&c1val=&c2stat=&c2comp=&c2val=&c3stat=&c3comp=&c3val=&c4stat=&c4comp=&c4val=&order_by=pts&order_by_asc=&offset=0)
- [MIT Sloan Sports Analytics Conference](http://www.sloansportsconference.com/wp-content/uploads/2018/02/2004.pdf)


