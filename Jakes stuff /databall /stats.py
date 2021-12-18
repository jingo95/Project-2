{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "656750ff-f1d5-42d5-b7fc-080ad6cdcca3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def eff_fg_pct(data, group=''):\n",
    "    return (data[group + 'FGM'] + 0.5 * data[group + 'FG3M']) / data[group + 'FGA']\n",
    "\n",
    "\n",
    "def fg_pct(data, group=''):\n",
    "    return data[group + 'FGM'] / data[group + 'FGA']\n",
    "\n",
    "\n",
    "def fg2a(data, group=''):\n",
    "    return data[group + 'FGA'] - data[group + 'FG3A']\n",
    "\n",
    "\n",
    "def fg2m(data, group=''):\n",
    "    return data[group + 'FGM'] - data[group + 'FG3M']\n",
    "\n",
    "\n",
    "def fg2_pct(data, group=''):\n",
    "    return fg2m(data, group) / fg2a(data, group)\n",
    "\n",
    "\n",
    "def fg3_pct(data, group=''):\n",
    "    return data[group + 'FG3M'] / data[group + 'FG3A']\n",
    "\n",
    "\n",
    "def fg3a_rate(data, group=''):\n",
    "    return data[group + 'FG3A'] / data[group + 'FGA']\n",
    "\n",
    "\n",
    "def ft_pct(data, group=''):\n",
    "    return data[group + 'FTM'] / data[group + 'FTA']\n",
    "\n",
    "\n",
    "def ft_per_fga(data, group=''):\n",
    "    return data[group + 'FTM'] / data[group + 'FGA']\n",
    "\n",
    "\n",
    "def ft_rate(data, group=''):\n",
    "    return data[group + 'FTA'] / data[group + 'FGA']\n",
    "\n",
    "\n",
    "def tov_pct(data, group=''):\n",
    "    return data[group + 'TOV'] / (data[group + 'FGA'] + 0.44 * data[group + 'FTA'] + data[group + 'TOV'])\n",
    "\n",
    "\n",
    "def ts_pct(data, group=''):\n",
    "    return data[group + 'PTS'] / (2 * (data[group + 'FGA'] + 0.44 * data[group + 'FTA']))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e95c929a-474a-4901-8ad7-dbc32b38642b",
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
