{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "01552b19-f7f2-440a-be10-4e701c2b4fb6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "====== GAMES ======\n",
      "(25024, 21)\n",
      "Min date : 2003-10-05\n",
      "Max date : 2021-11-17\n",
      "====== GAMES DETAILS ======\n",
      "(626111, 29)\n",
      "N uniques games ID : 24881\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/pb/9nrds4y576x41j1jw01gnkc40000gn/T/ipykernel_13844/956678312.py:22: DtypeWarning: Columns (6) have mixed types.Specify dtype option on import or set low_memory=False.\n",
      "  main()\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "\n",
    "def main():\n",
    "    datasets = ['games.csv','games_details.csv']\n",
    "\n",
    "    games = pd.read_csv('games.csv')\n",
    "\n",
    "    print('====== GAMES ======')\n",
    "    print(games.shape)\n",
    "    print('Min date : %s'%(games['GAME_DATE_EST'].min()))\n",
    "    print('Max date : %s'%(games['GAME_DATE_EST'].max()))\n",
    "\n",
    "\n",
    "    games_details = pd.read_csv('games_details.csv')\n",
    "    print('====== GAMES DETAILS ======')\n",
    "    print(games_details.shape)\n",
    "    print('N uniques games ID : %i'%(games_details['GAME_ID'].nunique()))\n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a1d56dcd-a0b2-40fd-8715-c5283fc7cefc",
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
