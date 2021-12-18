{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1fa23fac-80f0-4066-a8e8-9526c5a22e1e",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'nbapredict'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/pb/9nrds4y576x41j1jw01gnkc40000gn/T/ipykernel_7319/571819632.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     10\u001b[0m \u001b[0;31m# Local Imports\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 11\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mnbapredict\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdatabase\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdbinterface\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mDBInterface\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     12\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mnbapredict\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpredict\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mbets\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     13\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mnbapredict\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mscrapers\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mscraper\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'nbapredict'"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "This module runs the entire NBA_bet project.\n",
    "This module wraps the entire project into a single script with run_all() as the function which drives the script. First,\n",
    "it sets up the database and session connections. Then, it scrapes all new data. Finally, it predicts all games for which\n",
    "data is available. Most session.commit() calls in the project are performed here. However, note predict_all() requires\n",
    "a commit during the process in order to function correctly.\n",
    "\"\"\"\n",
    "from sqlalchemy.orm import Session\n",
    "\n",
    "# Local Imports\n",
    "from nbapredict.database.dbinterface import DBInterface\n",
    "from nbapredict.predict import bets\n",
    "from nbapredict.scrapers import scraper\n",
    "from nbapredict.configuration import Config\n",
    "\n",
    "\n",
    "def run_all():\n",
    "    \"\"\"Run the entire NBA_bet project.\"\"\"\n",
    "    db = DBInterface()\n",
    "    year = Config.get_property(\"league_year\")\n",
    "    session = Session(bind=db.engine)\n",
    "\n",
    "    scraper.scrape_all(db, session, year)\n",
    "    session.commit()\n",
    "\n",
    "    bets.predict_all(db, session)\n",
    "    session.commit()\n",
    "    session.close()\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    run_all()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a469ab2-8da8-4ae7-bd63-fcf5326c6722",
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
