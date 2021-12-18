{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "505c0041-4de1-4b70-8980-5047953db259",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/pb/9nrds4y576x41j1jw01gnkc40000gn/T/ipykernel_4893/3808588032.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mnba_api\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstats\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mendpoints\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mleaguedashteamstats\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mstatistics\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mgetStats\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mgetStatsForTeam\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mtime\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mcustomHeaders\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mcustomHeaders\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/Desktop/BOOTCAMP/Project 2 folder/getStats.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     70\u001b[0m   {\n\u001b[1;32m     71\u001b[0m    \u001b[0;34m\"cell_type\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"code\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 72\u001b[0;31m    \u001b[0;34m\"execution_count\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     73\u001b[0m    \u001b[0;34m\"id\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"dcc19cd8-6207-4cfa-b475-d66b44504a04\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     74\u001b[0m    \u001b[0;34m\"metadata\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "# standardizeStats.py - Uses Z Scores ((Obs  - Mean) / St Dev.) to standardize any of the different statistics scraped\n",
    "\n",
    "from nba_api.stats.endpoints import leaguedashteamstats\n",
    "import statistics\n",
    "from getStats import getStatsForTeam\n",
    "import time\n",
    "from customHeaders import customHeaders\n",
    "\n",
    "# Finds league mean for the entered basic or advanced statistic (statType = 'Base' or 'Advanced')\n",
    "def basicOrAdvancedStatMean(startDate, endDate, stat,statType = 'Base', season='2018-19'):\n",
    "\n",
    "    time.sleep(.2)\n",
    "    # Gets list of dictionaries with stats for every team\n",
    "    allTeamsInfo = leaguedashteamstats.LeagueDashTeamStats(per_mode_detailed='Per100Possessions',\n",
    "                                                           measure_type_detailed_defense=statType,\n",
    "                                                           date_from_nullable=startDate,\n",
    "                                                           date_to_nullable=endDate,\n",
    "                                                           season=season,\n",
    "                                                           headers=customHeaders,\n",
    "                                                           timeout=120)\n",
    "    allTeamsDict = allTeamsInfo.get_normalized_dict()\n",
    "    allTeamsList = allTeamsDict['LeagueDashTeamStats']\n",
    "\n",
    "    specificStatAllTeams = []\n",
    "    for i in range(len(allTeamsList)):  # Loops through and appends specific stat to new list until every team's stat has been added\n",
    "        specificStatAllTeams.append(allTeamsList[i][stat])\n",
    "\n",
    "    mean = statistics.mean(specificStatAllTeams)  # Finds mean of stat\n",
    "    return mean\n",
    "\n",
    "\n",
    "# Finds league standard deviation for the entered basic or advanced statistic (statType = 'Base' or 'Advanced')\n",
    "def basicOrAdvancedStatStandardDeviation(startDate, endDate, stat,statType = 'Base', season='2018-19'):\n",
    "\n",
    "    time.sleep(.2)\n",
    "    # Gets list of dictionaries with stats for every team\n",
    "    allTeamsInfo = leaguedashteamstats.LeagueDashTeamStats(per_mode_detailed='Per100Possessions',\n",
    "                                                           measure_type_detailed_defense=statType,\n",
    "                                                           date_from_nullable=startDate,\n",
    "                                                           date_to_nullable=endDate,\n",
    "                                                           season=season,\n",
    "                                                           headers=customHeaders,\n",
    "                                                           timeout=120\n",
    "                                                           )\n",
    "    allTeamsDict = allTeamsInfo.get_normalized_dict()\n",
    "    allTeamsList = allTeamsDict['LeagueDashTeamStats']\n",
    "\n",
    "    specificStatAllTeams = []\n",
    "    for i in range(len(allTeamsList)):  # Loops and appends specific stat to new list until every team's stat has been added\n",
    "        specificStatAllTeams.append(allTeamsList[i][stat])\n",
    "\n",
    "    standardDeviation = statistics.stdev(specificStatAllTeams)  # Finds standard deviation of stat\n",
    "    return standardDeviation\n",
    "\n",
    "\n",
    "# Returns a standardized version of each data point via the z-score method\n",
    "def basicOrAdvancedStatZScore(observedStat, mean, standardDeviation):\n",
    "\n",
    "    zScore = (observedStat-mean)/standardDeviation  # Calculation for z-score\n",
    "\n",
    "    return(zScore)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bf279877-25e5-49b0-b4f9-d0dc724ddc4d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
