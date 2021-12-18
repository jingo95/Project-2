{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b8b86bd-e66f-48b8-87c7-1f6c949efc45",
   "metadata": {},
   "outputs": [],
   "source": [
    "import datetime\n",
    "import pandas as pd\n",
    "from Scrapper import Scrapper\n",
    "from time import sleep\n",
    "\n",
    "\n",
    "def get_date(days: int):\n",
    "    date = datetime.date.today() - datetime.timedelta(days=days)\n",
    "    return date.strftime('%Y-%m-%d')\n",
    "\n",
    "\n",
    "def merge_news_old(new_df, old_df):\n",
    "    return pd.concat([new_df, old_df], sort=False).drop_duplicates().reset_index(drop=True)\n",
    "\n",
    "\n",
    "def get_data(url, datasets_name, headers):\n",
    "\n",
    "    scrapper = Scrapper(headers=headers, max_call_errors=5)\n",
    "    json = scrapper.retrieve_json_api_from_url(url=url)\n",
    "\n",
    "    if json == None:\n",
    "        return None\n",
    "\n",
    "    dfs = {}\n",
    "    for elem in json['resultSets']:\n",
    "        if elem['name'] not in datasets_name:\n",
    "            continue\n",
    "\n",
    "        df = pd.DataFrame(elem['rowSet'], columns=elem['headers'])\n",
    "        dfs[elem['name']] = df\n",
    "\n",
    "    return dfs\n",
    "\n",
    "\n",
    "def get_game_detail(game_id, headers):\n",
    "    if type(game_id) != type(str()):\n",
    "        game_id = '00' + str(game_id)\n",
    "\n",
    "    url = 'https://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=0&GameID='+str(game_id) \\\n",
    "        + '&RangeType=0&Season=2019-20&SeasonType=Regular+Season&StartPeriod=1&StartRange=0'\n",
    "\n",
    "    print(url)\n",
    "\n",
    "    df = get_data(url, datasets_name=['PlayerStats'], headers=headers)\n",
    "    sleep(0.2)\n",
    "    return df['PlayerStats']"
   ]
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
