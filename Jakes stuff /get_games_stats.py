{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2aced890-8a2c-4af0-b9bc-954740617355",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(25024, 21)\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from time import sleep, time\n",
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "\n",
    "def get_data(url, dataset_name):\n",
    "    HEADERS = {'Host': 'stats.nba.com',\n",
    "    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',\n",
    "    'Referer': 'https://stats.nba.com/game/0021900253/'}\n",
    "\n",
    "    response = requests.get(url, headers=HEADERS)\n",
    "    status_200_ok = response.status_code == 200\n",
    "    nb_error = 0\n",
    "    \n",
    "    while not status_200_ok and nb_error < 5:\n",
    "        sleep(1)\n",
    "        response = requests.get(url)\n",
    "        status_200_ok = response.status_code == 200\n",
    "        nb_error += 1\n",
    "    \n",
    "    # print(response.status_code, url)\n",
    "\n",
    "    if nb_error == 5:\n",
    "        return None\n",
    "    \n",
    "    json = response.json()\n",
    "    \n",
    "    json_dataset = [elem for elem in json['resultSets'] if elem['name'] == dataset_name][0]\n",
    "\n",
    "    df = pd.DataFrame(json_dataset['rowSet'], columns=json_dataset['headers'])\n",
    "    return df\n",
    "\n",
    "\n",
    "t0 = time()\n",
    "\n",
    "def get_game_detail(game_id: str):\n",
    "    url = 'https://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=0&GameID='+str(game_id) \\\n",
    "        +'&RangeType=0&Season=2019-20&SeasonType=Regular+Season&StartPeriod=1&StartRange=0'\n",
    "    df = get_data(url, dataset_name='PlayerStats')\n",
    "    # print(game_id, '- time elapsed : %.2fs'%(time()-t0))\n",
    "    return df\n",
    "\n",
    "\n",
    "def format_game_id(df):\n",
    "    return df['GAME_ID'].apply(lambda x: '00'+str(x))\n",
    "\n",
    "\n",
    "games_df = pd.read_csv('games.csv')\n",
    "print(games_df.shape)\n",
    "games_df['GAME_ID'] = format_game_id(games_df)\n",
    "games_df = games_df.sort_values('GAME_DATE_EST', ascending=False)\n",
    "games_df['FILTER'] = games_df['GAME_ID'].str[3:5].astype(int)\n",
    "games_df = games_df[games_df['FILTER'] < 9]\n",
    "\n",
    "games_detail = list()\n",
    "season = '08'\n",
    "\n",
    "for idx, row in games_df.iterrows():\n",
    "    game_id = row['GAME_ID']\n",
    "    \n",
    "    if game_id[3:5] != season and len(games_detail) > 0:\n",
    "        print(season)\n",
    "        games_detail_df = pd.concat(games_detail)\n",
    "        games_detail_df.to_csv('games_details_20'+season+'.csv', index=False)\n",
    "        print('games_details_20'+season+'.csv', '- time elapsed : %.2fs'%(time()-t0), games_detail_df.shape)\n",
    "        season = game_id[3:5]\n",
    "\n",
    "    games_detail.append(get_game_detail(row['GAME_ID']))\n",
    "\n",
    "# games_detail = games_df['GAME_ID'].iloc[0:4].apply(lambda x: get_game_detail(x, last_season))\n",
    "games_detail_df = pd.concat(games_detail)\n",
    "\n",
    "games_detail_df.to_csv('games_details.csv', index=False)\n",
    "print('games_details.csv', '- time elapsed : %.2fs'%(time()-t0))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2c66b4ed-96fc-4bae-be5d-42feb4311ba9",
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
