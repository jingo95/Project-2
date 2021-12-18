{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a483e61-bb59-4685-9ad1-2a1f50936537",
   "metadata": {},
   "outputs": [],
   "source": [
    "from Scrapper import Scrapper\n",
    "import datetime\n",
    "import pandas as pd\n",
    "import json\n",
    "\n",
    "\n",
    "def main():\n",
    "\n",
    "    date = datetime.datetime(2020,2,10).strftime('%Y-%m-%d')\n",
    "    url = 'https://stats.nba.com/stats/scoreboardV2?DayOffset=0&LeagueID=00&gameDate='+date\n",
    "\n",
    "    url = 'https://stats.nba.com/stats/boxscoretraditionalv2?EndPeriod=10&EndRange=0&GameID=0012000047&RangeType=0&Season=2019-20&SeasonType=Regular+Season&StartPeriod=1&StartRange=0'\n",
    "\n",
    "    datasets_name = ['GameHeader', 'LineScore',\n",
    "                'EastConfStandingsByDay', 'WestConfStandingsByDay']\n",
    "\n",
    "    HEADERS = {\n",
    "        # 'Host': 'i.cdn.turner.com',\n",
    "        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',\n",
    "        'Referer': 'https://www.nba.com/stats/',\n",
    "        'Origin': 'https://www.nba.com',    \n",
    "        'Accept': '*/*',\n",
    "        'Accept-Language': 'en-GB,en;q=0.5',\n",
    "        'Accept-Encoding': 'gzip, deflate, br',\n",
    "        'DNT': '1',\n",
    "        'Connection': 'keep-alive'\n",
    "    }\n",
    "    \n",
    "\n",
    "    scrapper = Scrapper(headers=HEADERS, max_call_errors=5)\n",
    "    json_returned = scrapper.retrieve_json_api_from_url(url=url)\n",
    "\n",
    "    if json_returned == None:\n",
    "        return\n",
    "\n",
    "    print(json.dumps(json_returned, indent=4, sort_keys=True))\n",
    "\n",
    "    # dfs = {}\n",
    "    # for elem in json_returned['resultSets']:\n",
    "    #     if elem['name'] not in datasets_name:\n",
    "    #         continue\n",
    "\n",
    "    #     df = pd.DataFrame(elem['rowSet'], columns=elem['headers'])\n",
    "    #     dfs[elem['name']] = df\n",
    "\n",
    "    \n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
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
