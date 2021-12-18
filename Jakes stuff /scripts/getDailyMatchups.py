{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "fde4fd5a-0597-4bfb-bbe3-7d629229331c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting nba_api\n",
      "  Downloading nba_api-1.1.11.tar.gz (125 kB)\n",
      "\u001b[K     |████████████████████████████████| 125 kB 2.8 MB/s eta 0:00:01\n",
      "\u001b[?25hRequirement already satisfied: requests in /opt/anaconda3/lib/python3.8/site-packages (from nba_api) (2.26.0)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in /opt/anaconda3/lib/python3.8/site-packages (from requests->nba_api) (2.0.4)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /opt/anaconda3/lib/python3.8/site-packages (from requests->nba_api) (2021.10.8)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /opt/anaconda3/lib/python3.8/site-packages (from requests->nba_api) (1.26.7)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /opt/anaconda3/lib/python3.8/site-packages (from requests->nba_api) (3.2)\n",
      "Building wheels for collected packages: nba-api\n",
      "  Building wheel for nba-api (setup.py) ... \u001b[?25ldone\n",
      "\u001b[?25h  Created wheel for nba-api: filename=nba_api-1.1.11-py3-none-any.whl size=251504 sha256=9821d06a4046aacb47aaff667db73d161821b860eeadb0d9ab1aeedd13f4bae1\n",
      "  Stored in directory: /Users/JakeDoherty_1/Library/Caches/pip/wheels/96/0a/d6/0e51f16e26a046ed08ce8266c86011c74bf57678cd62ad71b0\n",
      "Successfully built nba-api\n",
      "Installing collected packages: nba-api\n",
      "Successfully installed nba-api-1.1.11\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install nba_api "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "434e3db6-5a17-4b2e-b84c-b4745818d955",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'teamIds'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/pb/9nrds4y576x41j1jw01gnkc40000gn/T/ipykernel_5173/3738171405.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mnba_api\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mstats\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mendpoints\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mleaguegamelog\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mscoreboard\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mteamIds\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mteams\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mcustomHeaders\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mcustomHeaders\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'teamIds'"
     ]
    }
   ],
   "source": [
    "# getDailyMatchups.py - Finds the daily NBA games\n",
    "\n",
    "from nba_api.stats.endpoints import leaguegamelog, scoreboard\n",
    "from teamIds import teams\n",
    "from customHeaders import customHeaders\n",
    "\n",
    "# Function to get you the games on a specified date (Home vs. Away)\n",
    "# Used for dates in the past\n",
    "# Return value is a list where index 0 is a dict holding the games and index 1 is the result of the games\n",
    "# Enter a date in the format mm/dd/yyyy and season in the format yyyy-yy\n",
    "def dailyMatchupsPast(date, season):\n",
    "\n",
    "    # Obtains a list of teams who played on specified date\n",
    "    dailyMatchups = leaguegamelog.LeagueGameLog(season=season, league_id='00', season_type_all_star='Regular Season', date_from_nullable=date,date_to_nullable=date, headers=customHeaders,timeout=60)\n",
    "    dailyMatchupsDict = dailyMatchups.get_normalized_dict()\n",
    "    listOfTeams = dailyMatchupsDict['LeagueGameLog']\n",
    "\n",
    "    winLossList = []\n",
    "    homeAwayDict = {}\n",
    "    for i in range(0,len(listOfTeams),2):  # Loops through every other team\n",
    "        if '@' in listOfTeams[i]['MATCHUP']:  # @ in matchup indicates that the current team is away\n",
    "            awayTeam = listOfTeams[i]['TEAM_NAME']\n",
    "            homeTeam = listOfTeams[i+1]['TEAM_NAME']\n",
    "\n",
    "            winLossList.append(listOfTeams[i+1]['WL'])  # Appends if the home team won or lost to list\n",
    "\n",
    "        else:\n",
    "            awayTeam = listOfTeams[i+1]['TEAM_NAME']\n",
    "            homeTeam = listOfTeams[i]['TEAM_NAME']\n",
    "\n",
    "            winLossList.append(listOfTeams[i]['WL'])  # Appends if the home team won or lost to the list\n",
    "\n",
    "        homeAwayDict.update({homeTeam:awayTeam})  # Adds current game to list of all games for that day\n",
    "\n",
    "    matchupsResultCombined = [homeAwayDict, winLossList]  # Combines games and win/loss results into one list\n",
    "    return(matchupsResultCombined)\n",
    "\n",
    "\n",
    "# Function to get you the games on a specified date (Home vs. Away)\n",
    "# Used for dates in the present or future\n",
    "# Return value is a list where index 0 is a dict holding the games  {Home:Away}\n",
    "# Enter a date in the format mm/dd/yyyy\n",
    "def dailyMatchupsPresent(date):\n",
    "\n",
    "    # Obtains all games that are set to occur on specified date\n",
    "    dailyMatchups = scoreboard.Scoreboard(league_id='00', game_date=date, headers=customHeaders, timeout=120)\n",
    "    dailyMatchupsDict = dailyMatchups.get_normalized_dict()\n",
    "    listOfGames = dailyMatchupsDict['GameHeader']\n",
    "\n",
    "    homeAwayDict = {}\n",
    "\n",
    "    for game in listOfGames:  # Loops through each game on date\n",
    "\n",
    "        homeTeamID = game['HOME_TEAM_ID']\n",
    "\n",
    "        for team, teamID in teams.items():  # Finds name of the home team that corresponds with teamID\n",
    "            if teamID == homeTeamID:\n",
    "                homeTeamName = team\n",
    "\n",
    "        awayTeamID = game['VISITOR_TEAM_ID']\n",
    "\n",
    "        for team, teamID in teams.items():  # Finds name of the away team that corresponds with teamID\n",
    "            if teamID == awayTeamID:\n",
    "                awayTeamName = team\n",
    "\n",
    "        homeAwayDict.update({homeTeamName:awayTeamName})\n",
    "\n",
    "    return homeAwayDict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "075e7f94-3f1e-4559-a590-771266228c48",
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
