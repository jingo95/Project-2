{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "0a11c6e6-bb1f-466e-8f04-30b564d45b6f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ast_pct(data):\n",
    "    return data.TEAM_AST / data.TEAM_FGM\n",
    "\n",
    "\n",
    "def blk_pct(data):\n",
    "    return data.TEAM_BLK / (data.OPP_FGA - data.OPP_FG3A)\n",
    "\n",
    "\n",
    "def def_rating(data):\n",
    "    return 100 * data.OPP_PTS / possessions(data)\n",
    "\n",
    "\n",
    "def dreb_pct(data):\n",
    "    return data.TEAM_DREB / (data.TEAM_DREB + data.OPP_OREB)\n",
    "\n",
    "\n",
    "def off_rating(data):\n",
    "    return 100 * data.TEAM_PTS / possessions(data)\n",
    "\n",
    "\n",
    "def oreb_pct(data):\n",
    "    return data.TEAM_OREB / (data.TEAM_OREB + data.OPP_DREB)\n",
    "\n",
    "\n",
    "def pace(data):\n",
    "    min_per_game = 240\n",
    "    min_played = data.TEAM_MIN\n",
    "\n",
    "    if min_played[0] < min_per_game:\n",
    "        min_played *= 5\n",
    "\n",
    "    return possessions(data) / min_played * min_per_game\n",
    "\n",
    "\n",
    "def possessions(data):\n",
    "    return (data.TEAM_FGA + 0.4 * data.TEAM_FTA + data.TEAM_TOV -\n",
    "            1.07 * (data.TEAM_OREB / (data.TEAM_OREB + data.OPP_DREB)) * (data.TEAM_FGA - data.TEAM_FGM) +\n",
    "            data.OPP_FGA + 0.4 * data.OPP_FTA + data.OPP_TOV -\n",
    "            1.07 * (data.OPP_OREB / (data.OPP_OREB + data.TEAM_DREB)) * (data.OPP_FGA - data.OPP_FGM)) / 2\n",
    "\n",
    "\n",
    "def reb_pct(data):\n",
    "    return data.TEAM_REB / (data.TEAM_REB + data.OPP_REB)\n",
    "\n",
    "\n",
    "def stl_pct(data):\n",
    "    return data.TEAM_STL / possessions(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d54c2a51-1df1-4947-8cc3-8cf470e562ea",
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
