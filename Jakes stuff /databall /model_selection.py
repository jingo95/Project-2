{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "895f1064-b259-4fec-ab83-14d127fa06b9",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'hyperopt'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/pb/9nrds4y576x41j1jw01gnkc40000gn/T/ipykernel_9127/3657372110.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mhyperopt\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mTrials\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfmin\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mspace_eval\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtpe\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmodel_selection\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mStratifiedKFold\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcross_val_score\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpipeline\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mmake_pipeline\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'hyperopt'"
     ]
    }
   ],
   "source": [
    "from functools import partial\n",
    "\n",
    "import pandas as pd\n",
    "from hyperopt import Trials, fmin, space_eval, tpe\n",
    "from sklearn.model_selection import StratifiedKFold, cross_val_score\n",
    "from sklearn.pipeline import make_pipeline\n",
    "from sklearn.preprocessing import FunctionTransformer, LabelEncoder\n",
    "\n",
    "from databall.util import select_columns, stat_names\n",
    "\n",
    "\n",
    "def calculate_metrics(models, x, y, attributes, param_name, param_vec, k=6):\n",
    "    # Initialize list of results\n",
    "    results = [[]]\n",
    "\n",
    "    # Make transformer that selects the desired attributes from the DataFrame\n",
    "    selector = FunctionTransformer(partial(select_columns, attributes=attributes, columns=x.columns))\n",
    "\n",
    "    for i in range(len(models)):\n",
    "        for param in param_vec:\n",
    "            # Make a pipeline that selects the desired attributes prior to the classifier\n",
    "            model = make_pipeline(selector, models[i](**{param_name: param}))\n",
    "            metrics = cross_val_scoring(model, x, y, k)\n",
    "\n",
    "            # Calculate performance metrics\n",
    "            if i == len(results):\n",
    "                results += [[metrics]]\n",
    "            else:\n",
    "                results[i] += [metrics]\n",
    "\n",
    "    return results\n",
    "\n",
    "\n",
    "def cross_val_scoring(model, x, y, k=6, random_state=8):\n",
    "    # Define metrics\n",
    "    scoring = ['accuracy', 'precision', 'recall', 'roc_auc', 'average_precision']\n",
    "\n",
    "    # Create cross validator\n",
    "    kfold = StratifiedKFold(n_splits=k, random_state=random_state)\n",
    "\n",
    "    # Calculate metrics\n",
    "    return [cross_val_score(model, x, y, cv=kfold, scoring=score).mean() for score in scoring]\n",
    "\n",
    "\n",
    "def objective(params, model, x, y, attributes, k=6, random_state=8):\n",
    "    model.set_params(**params)\n",
    "    kfold = StratifiedKFold(n_splits=k, random_state=random_state)\n",
    "    score = cross_val_score(model, x[attributes], y, cv=kfold, scoring='accuracy')\n",
    "    return 1 - score.mean()\n",
    "\n",
    "\n",
    "def optimize_params(model, x, y, attributes, space, k=6, max_evals=100, eval_space=False):\n",
    "    trials = Trials()\n",
    "    best = fmin(partial(objective, model=model, x=x, y=y, attributes=attributes, k=k),\n",
    "                space, algo=tpe.suggest, max_evals=max_evals, trials=trials)\n",
    "\n",
    "    param_values = [t['misc']['vals'] for t in trials.trials]\n",
    "    param_values = [{key: value for key in params for value in params[key]} for params in param_values]\n",
    "\n",
    "    if eval_space:\n",
    "        param_values = [space_eval(space, params) for params in param_values]\n",
    "\n",
    "    param_df = pd.DataFrame(param_values)\n",
    "    param_df['accuracy'] = [1 - loss for loss in trials.losses()]\n",
    "    return space_eval(space, best), param_df\n",
    "\n",
    "\n",
    "def train_test_split(data, start_season, end_season, test_season_start=None, xlabels=None, ylabel='HOME_SPREAD_WL'):\n",
    "    if test_season_start is None:\n",
    "        test_season_start = end_season\n",
    "\n",
    "    if xlabels is None:\n",
    "        xlabels = stat_names()\n",
    "\n",
    "    if 'SEASON' in data.columns:\n",
    "        data = data[xlabels + [ylabel]].dropna()\n",
    "    else:\n",
    "        data = data[xlabels + ['SEASON', ylabel]].dropna()\n",
    "\n",
    "    x, y = data[xlabels], LabelEncoder().fit_transform(data[ylabel])\n",
    "    x_train = x[(start_season <= data.SEASON) & (data.SEASON < test_season_start)].copy()\n",
    "    y_train = y[(start_season <= data.SEASON) & (data.SEASON < test_season_start)].copy()\n",
    "    x_test = x[(test_season_start <= data.SEASON) & (data.SEASON <= end_season)].copy()\n",
    "    y_test = y[(test_season_start <= data.SEASON) & (data.SEASON <= end_season)].copy()\n",
    "    return x_train, y_train, x_test, y_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c71624b4-c193-4ed6-b1b6-a7d8e9d15d42",
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
