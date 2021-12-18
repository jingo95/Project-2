{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ab2ebb41-3cc1-4b80-9c5e-06456a55e7ee",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'nbapredict'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/pb/9nrds4y576x41j1jw01gnkc40000gn/T/ipykernel_7281/3924874423.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mlxml\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mhtml\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mnbapredict\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhelpers\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mbr_references\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mLocation\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mOutcome\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mTEAM_ABBREVIATIONS_TO_TEAM\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'nbapredict'"
     ]
    }
   ],
   "source": [
    "from lxml import html\n",
    "\n",
    "from nbapredict.helpers.br_references import Location, Outcome, TEAM_ABBREVIATIONS_TO_TEAM\n",
    "\n",
    "\n",
    "def parse_location(symbol):\n",
    "    if symbol == \"@\":\n",
    "        return Location.AWAY\n",
    "    elif symbol == \"\":\n",
    "        return Location.HOME\n",
    "    raise ValueError(\"Unknown symbol: {symbol}\".format(symbol=symbol))\n",
    "\n",
    "\n",
    "def parse_outcome(symbol):\n",
    "    if symbol == \"W\":\n",
    "        return Outcome.WIN\n",
    "    elif symbol == \"L\":\n",
    "        return Outcome.LOSS\n",
    "    raise ValueError(\"Unknown symbol: {symbol}\".format(symbol=symbol))\n",
    "\n",
    "\n",
    "def parse_seconds_played(formatted_playing_time):\n",
    "    if formatted_playing_time == \"\":\n",
    "        return 0\n",
    "\n",
    "    # It seems like basketball reference formats everything in MM:SS\n",
    "    # even when the playing time is greater than 59 minutes, 59 seconds.\n",
    "    #\n",
    "    # Because of this, we can't use strptime / %M as valid values are 0-59.\n",
    "    # So have to parse time by splitting on \":\" and assuming that\n",
    "    # the first part is the minute part and the second part is the seconds part\n",
    "    time_parts = formatted_playing_time.split(\":\")\n",
    "    minutes_played = time_parts[0]\n",
    "    seconds_played = time_parts[1]\n",
    "    return 60 * int(minutes_played) + int(seconds_played)\n",
    "\n",
    "\n",
    "def parse_player_box_score(row):\n",
    "    return {\n",
    "        \"name\": str(row[1].text_content()),\n",
    "        \"team\": TEAM_ABBREVIATIONS_TO_TEAM[row[2].text_content()],\n",
    "        \"location\": parse_location(row[3].text_content()),\n",
    "        \"opponent\": TEAM_ABBREVIATIONS_TO_TEAM[row[4].text_content()],\n",
    "        \"outcome\": parse_outcome(row[5].text_content()),\n",
    "        \"seconds_played\": int(parse_seconds_played(row[6].text_content())),\n",
    "        \"made_field_goals\": int(row[7].text_content()),\n",
    "        \"attempted_field_goals\": int(row[8].text_content()),\n",
    "        \"made_three_point_field_goals\": int(row[10].text_content()),\n",
    "        \"attempted_three_point_field_goals\": int(row[11].text_content()),\n",
    "        \"made_free_throws\": int(row[13].text_content()),\n",
    "        \"attempted_free_throws\": int(row[14].text_content()),\n",
    "        \"offensive_rebounds\": int(row[16].text_content()),\n",
    "        \"defensive_rebounds\": int(row[17].text_content()),\n",
    "        \"assists\": int(row[19].text_content()),\n",
    "        \"steals\": int(row[20].text_content()),\n",
    "        \"blocks\": int(row[21].text_content()),\n",
    "        \"turnovers\": int(row[22].text_content()),\n",
    "        \"personal_fouls\": int(row[23].text_content()),\n",
    "        \"game_score\": float(row[25].text_content()),\n",
    "    }\n",
    "\n",
    "\n",
    "def parse_player_box_scores(page):\n",
    "    tree = html.fromstring(page)\n",
    "    rows = tree.xpath('//table[@id=\"stats\"]//tbody/tr[not(contains(@class, \"thead\"))]')\n",
    "    return list(map(lambda row: parse_player_box_score(row), rows))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7745d76-8c84-4688-858c-42d7027104e0",
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
