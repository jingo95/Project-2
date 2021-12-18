{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1409fe5f-05e8-4894-85ba-5cfad5e339b3",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'nbapredict'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/pb/9nrds4y576x41j1jw01gnkc40000gn/T/ipykernel_8220/2295272221.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;31m# Local Imports\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 7\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mnbapredict\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpredict\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mget\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      8\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mnbapredict\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mconfiguration\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mConfig\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mnbapredict\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmodels\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfour_factor_regression\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mlm\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'nbapredict'"
     ]
    }
   ],
   "source": [
    "\"\"\"Predict.games contains functions oriented around predicting games\"\"\"\n",
    "\n",
    "from sqlalchemy import Integer, ForeignKey, String, UniqueConstraint\n",
    "from sqlalchemy.orm import Session, relationship\n",
    "\n",
    "# Local Imports\n",
    "import nbapredict.predict.get as get\n",
    "from nbapredict.configuration import Config\n",
    "import nbapredict.models.four_factor_regression as lm\n",
    "import nbapredict.database.dbinterface as dbinterface\n",
    "\n",
    "\n",
    "def create_prediction_table(database, data, tbl_name):\n",
    "    \"\"\"Create a prediction table from the data and with the table name in the database.\n",
    "    ToDo: This will need a big overhaul\n",
    "    Args:\n",
    "        database: An initialized DBInterface class from database.dbinterface.py\n",
    "        data: An initialized DataOperator object, from database.manipulator, with prediction data\n",
    "        tbl_name: The desired table name (with year as the last four characters)\n",
    "    \"\"\"\n",
    "    # Create columns from data\n",
    "    sql_types = data.get_sql_type()\n",
    "    # Add new columns\n",
    "    year = tbl_name[-4:]\n",
    "    schedule_name = \"sched_{}\".format(year)\n",
    "    additional_cols = [{'game_id': [Integer, ForeignKey(schedule_name + \".id\")]}, {\"MOV\": Integer}]\n",
    "    for col in additional_cols:\n",
    "        sql_types.update(col)\n",
    "    constraint = {UniqueConstraint: [\"start_time\", \"home_team\", \"away_team\"]}\n",
    "    # Map prediction table\n",
    "    database.map_table(tbl_name, sql_types, constraint)\n",
    "\n",
    "    # Get tables for relationships\n",
    "    sched_tbl = database.get_table_mappings(schedule_name)\n",
    "\n",
    "    # Create Relationships\n",
    "    if \"game_preds_{}\".format(year) not in sched_tbl.__mapper__.relationships.keys():\n",
    "        sched_tbl.predictions = relationship(database.Template)\n",
    "\n",
    "    database.create_tables()\n",
    "    database.clear_mappers()\n",
    "\n",
    "\n",
    "def main():\n",
    "    db = dbinterface.DBInterface()\n",
    "    session = Session(bind=db.engine)\n",
    "    league_year = Config.get_property(\"league_year\")\n",
    "\n",
    "    regression = lm.main(db, session)\n",
    "    sched_tbl = db.get_table_mappings(\"sched_{}\".format(league_year))\n",
    "\n",
    "    if not db.table_exists(\"pred\"):\n",
    "        # Returns a data manipulator class\n",
    "        sample = get.sample_prediction(db, session, ref_tbl=sched_tbl, model=regression)\n",
    "        create_prediction_table(db, sample, \"game_pred_{}\".format(league_year))\n",
    "\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f470c663-0464-4ee4-a062-c1fd10b2bd20",
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
