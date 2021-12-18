{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16707684-a8b0-46df-88eb-a14a882921c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "----- START -----\n"
     ]
    }
   ],
   "source": [
    "from time import time\n",
    "import pandas as pd\n",
    "import requests\n",
    "\n",
    "def get_data(url, datasets_name):\n",
    "    HEADERS = {'Host': 'stats.nba.com',\n",
    "    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',\n",
    "    'Referer': 'https://stats.nba.com/game/0021900253/'}\n",
    "\n",
    "    response = requests.get(url, headers=HEADERS)\n",
    "    status_200_ok = response.status_code == 200\n",
    "    nb_error = 0\n",
    "    \n",
    "    # If there are too much call, just try 5 times to be sure that we can't have the data\n",
    "    while not status_200_ok and nb_error < 5:\n",
    "        sleep(1)\n",
    "        response = requests.get(url)\n",
    "        status_200_ok = response.status_code == 200\n",
    "        nb_error += 1\n",
    "    \n",
    "    if nb_error == 5:\n",
    "        return None\n",
    "    \n",
    "    json = response.json()\n",
    "    dfs = {}\n",
    "    for elem in json['resultSets']:\n",
    "        if elem['name'] not in datasets_name:\n",
    "            continue\n",
    "        \n",
    "        df = pd.DataFrame(elem['rowSet'], columns=elem['headers'])\n",
    "        dfs[elem['name']] = df\n",
    "    \n",
    "    return dfs\n",
    "\n",
    "\n",
    "def get_team_detail(team_id: int):\n",
    "    url = 'https://stats.nba.com/stats/teamdetails?TeamID='+str(team_id)    \n",
    "    df = get_data(url, datasets_name=['TeamBackground'])\n",
    "    return df['TeamBackground']\n",
    "\n",
    "def main():\n",
    "    print('----- START -----')\n",
    "    t0 = time()\n",
    "\n",
    "    # Load all teams\n",
    "    url = 'https://stats.nba.com/stats/commonteamyears?LeagueID=00'\n",
    "    teams = get_data(url, datasets_name=['TeamYears'])\n",
    "    teams = teams['TeamYears']\n",
    "\n",
    "    # Get team detail\n",
    "    teams_detail = teams['TEAM_ID'].apply(lambda x: get_team_detail(x))\n",
    "    teams_detail = pd.concat(teams_detail.values)\n",
    "\n",
    "    # Merge both datasets\n",
    "    teams_full = teams.merge(teams_detail, on=['TEAM_ID','ABBREVIATION'])\n",
    "\n",
    "    # Save teams dataset\n",
    "    teams_full.to_csv('data/teams.csv', index=False)\n",
    "\n",
    "    print('-----  END  ----- execution time : %.2fs'%(time()-t0))\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "79ad3bfb-ccc3-4220-89da-2a7a6c9dd1b4",
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
