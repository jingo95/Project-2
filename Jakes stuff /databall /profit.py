{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f2899e2a-07b3-4250-9270-bb849e10c6ad",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "\n",
    "def profit(data, var_predict='HOME_SPREAD_WL', bet_amount=100):\n",
    "    grouped = data.groupby('GAME_DATE')\n",
    "    num_games = 0\n",
    "    days = []\n",
    "    cumulative_correct = []\n",
    "    cumulative_percent = []\n",
    "    cumulative_profit = []\n",
    "    cumulative_investment = []\n",
    "\n",
    "    for day in grouped.groups:\n",
    "        games = grouped.get_group(day)\n",
    "        num = len(games)\n",
    "        num_games += num\n",
    "        days += [day]\n",
    "        num_correct = sum(games[var_predict] == games[var_predict + '_PRED'])\n",
    "        daily_profit = bet_amount * num_correct - bet_amount * (num - num_correct)\n",
    "\n",
    "        if len(cumulative_correct) == 0:\n",
    "            cumulative_correct += [num_correct]\n",
    "            cumulative_profit += [daily_profit]\n",
    "            cumulative_investment += [bet_amount * num]\n",
    "        else:\n",
    "            cumulative_correct += [num_correct + cumulative_correct[-1]]\n",
    "            cumulative_profit += [daily_profit + cumulative_profit[-1]]\n",
    "            cumulative_investment += [bet_amount * num + cumulative_investment[-1]]\n",
    "\n",
    "        cumulative_percent += [cumulative_correct[-1] / num_games]\n",
    "\n",
    "    return days, np.array(cumulative_percent), np.array(cumulative_profit)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dab11410-74f6-4659-8fab-aadca12d7bd9",
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
