{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c3acb624-c401-497a-a52a-d4687c0c7ac0",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3097813698.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"/var/folders/pb/9nrds4y576x41j1jw01gnkc40000gn/T/ipykernel_14815/3097813698.py\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    today=$(date +'%Y-%m-%d')\u001b[0m\n\u001b[0m          ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "#!/bin/bash\n",
    "today=$(date +'%Y-%m-%d')\n",
    "\n",
    "echo 'Save data'\n",
    "zip $PWD/data/save/save_$today.zip $PWD/data/*.csv\n",
    "\n",
    "echo 'Get new games'\n",
    "python $PWD'/scripts/get_new_games.py'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18544786-0915-4642-8422-d9f39262ce69",
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
