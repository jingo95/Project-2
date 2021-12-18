{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6547bc41-b650-4d86-b147-4411034774b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import HTML, display\n",
    "\n",
    "\n",
    "def print_df(df):\n",
    "    display(HTML(df.to_html(index=False)))\n",
    "\n",
    "\n",
    "def select_columns(data, attributes, columns):\n",
    "    return data[:, [index for index, col in enumerate(columns) if any(name in col for name in attributes)]]\n",
    "\n",
    "\n",
    "def stat_names():\n",
    "    basic = ['FGM', 'FGA', 'FG3M', 'FG3A', 'FTM', 'FTA', 'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK']\n",
    "    advanced = ['OFF_RTG', 'DEF_RTG', 'NET_RTG', 'EFG', 'TOV_PCT', 'OREB_PCT', 'DREB_PCT', 'FT_PER_FGA',\n",
    "                'FOUR_FACTORS', 'FOUR_FACTORS_REB']\n",
    "    stats = ['TEAM_' + s for s in basic] + ['OPP_' + s for s in basic]\n",
    "    stats += [s + '_AWAY' for s in stats]\n",
    "    stats += ['TEAM_' + s for s in advanced] + ['TEAM_' + s + '_AWAY' for s in advanced]\n",
    "    stats += ['PACE', 'POSSESSIONS', 'PACE_AWAY', 'POSSESSIONS_AWAY', 'HOME_SPREAD']\n",
    "    return stats"
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
