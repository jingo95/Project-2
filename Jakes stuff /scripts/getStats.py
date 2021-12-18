{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b53e2a7b-53e6-4d61-8309-c0f1cf28aa2c",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/pb/9nrds4y576x41j1jw01gnkc40000gn/T/ipykernel_5269/1502725856.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# getStats.py - Obtains a grouping of stats for any team in the NBA\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mteamIds\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mteams\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mnba_api\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstats\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mendpoints\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mteamdashboardbygeneralsplits\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mleaguedashteamstats\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mtime\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/Desktop/BOOTCAMP/Project 2 folder/teamIds.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     50\u001b[0m   {\n\u001b[1;32m     51\u001b[0m    \u001b[0;34m\"cell_type\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"code\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 52\u001b[0;31m    \u001b[0;34m\"execution_count\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     53\u001b[0m    \u001b[0;34m\"id\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"2cfd8255-0d98-4359-9a74-4005a5449735\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m    \u001b[0;34m\"metadata\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "# getStats.py - Obtains a grouping of stats for any team in the NBA\n",
    "\n",
    "from teamIds import teams\n",
    "from nba_api.stats.endpoints import teamdashboardbygeneralsplits, leaguedashteamstats\n",
    "import time\n",
    "from customHeaders import customHeaders\n",
    "\n",
    "# Returns various stats for inputted team in a dictionary\n",
    "# team should match team name in teamIds.py\n",
    "# startDate and endDate should be in format 'mm/dd/yyyy'\n",
    "def getStatsForTeam(team, startDate, endDate, season='2019-20'):\n",
    "\n",
    "    time.sleep(1)\n",
    "    # Uses NBA_API to access the dictionary holding basic stats for every team per 100 possessions\n",
    "    generalTeamInfo = teamdashboardbygeneralsplits.TeamDashboardByGeneralSplits(team_id=teams[team], per_mode_detailed='Per100Possessions', date_from_nullable=startDate, date_to_nullable=endDate, season=season, headers=customHeaders, timeout=120)\n",
    "    generalTeamDict = generalTeamInfo.get_normalized_dict()\n",
    "    generalTeamDashboard = generalTeamDict['OverallTeamDashboard'][0]\n",
    "\n",
    "    # Returns Win PCT, Rebounds, Turnovers, and Plus Minus\n",
    "    winPercentage = generalTeamDashboard['W_PCT']\n",
    "    rebounds = generalTeamDashboard['REB']\n",
    "    turnovers = generalTeamDashboard['TOV']\n",
    "    plusMinus = generalTeamDashboard['PLUS_MINUS']\n",
    "\n",
    "    # Uses NBA_API to access the dictionary holding advanced stats for every team\n",
    "    advancedTeamInfo = teamdashboardbygeneralsplits.TeamDashboardByGeneralSplits(team_id=teams[team], measure_type_detailed_defense='Advanced', date_from_nullable=startDate, date_to_nullable=endDate, season=season, headers=customHeaders, timeout=120)\n",
    "    advancedTeamDict  = advancedTeamInfo.get_normalized_dict()\n",
    "    advancedTeamDashboard = advancedTeamDict['OverallTeamDashboard'][0]\n",
    "\n",
    "    # Variables holding OFF Rating, DEF Rating, and TS%\n",
    "    offensiveRating = advancedTeamDashboard['OFF_RATING']\n",
    "    defensiveRating = advancedTeamDashboard['DEF_RATING']\n",
    "    trueShootingPercentage = advancedTeamDashboard['TS_PCT']\n",
    "\n",
    "    # Puts all the stats for specified team into a dictionary\n",
    "    allStats = {\n",
    "        'W_PCT':winPercentage,\n",
    "        'REB':rebounds,\n",
    "        'TOV':turnovers,\n",
    "        'PLUS_MINUS':plusMinus,\n",
    "        'OFF_RATING':offensiveRating,\n",
    "        'DEF_RATING': defensiveRating,\n",
    "        'TS_PCT':trueShootingPercentage,\n",
    "    }\n",
    "\n",
    "    return allStats"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dcc19cd8-6207-4cfa-b475-d66b44504a04",
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
