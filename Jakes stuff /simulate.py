{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "35023bed-0a82-4aee-97de-0bdccf11a7d9",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'hyperopt'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/pb/9nrds4y576x41j1jw01gnkc40000gn/T/ipykernel_9184/3434420014.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mhyperopt\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mfmin\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mspace_eval\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtpe\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmodel_selection\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mStratifiedKFold\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcross_val_score\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpreprocessing\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mLabelEncoder\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'hyperopt'"
     ]
    }
   ],
   "source": [
    "from hyperopt import fmin, space_eval, tpe\n",
    "from sklearn.model_selection import StratifiedKFold, cross_val_score\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "\n",
    "def simulate(model, data, season, predictors, output, build=None, evolve=False, freq=1):\n",
    "    result = output + '_PRED'\n",
    "    data = data.copy()\n",
    "    encoder = LabelEncoder().fit(data[output])\n",
    "    data[output] = encoder.transform(data[output])\n",
    "    train, test = data[data.SEASON < season].copy(), data[data.SEASON == season].copy()\n",
    "\n",
    "    if build is None:\n",
    "        build = fit\n",
    "\n",
    "    if evolve:\n",
    "        test[result] = test[output]\n",
    "        test_groups = test.groupby('GAME_DATE')\n",
    "        count = 0\n",
    "\n",
    "        for day in test_groups.groups:\n",
    "            if count == freq or count == 0:\n",
    "                build(model, train[predictors], train[output])\n",
    "                count = 0\n",
    "\n",
    "            games = test_groups.get_group(day)\n",
    "            test.loc[games.index, [result]] = model.predict(games[predictors])\n",
    "            train = train.append(games)\n",
    "            count += 1\n",
    "    else:\n",
    "        build(model, train[predictors], train[output])\n",
    "        test[result] = model.predict(test[predictors])\n",
    "\n",
    "    test[output] = encoder.inverse_transform(test[output])\n",
    "    test[result] = encoder.inverse_transform(test[result])\n",
    "    return test\n",
    "\n",
    "\n",
    "def fit(model, x, y):\n",
    "    model.fit(x, y)\n",
    "\n",
    "\n",
    "class HyperOptFit:\n",
    "    def __init__(self, space, max_evals=10, n_splits=10, scoring='roc_auc', random_state=8):\n",
    "        self.space = space\n",
    "        self.max_evals = max_evals\n",
    "        self.n_splits = n_splits\n",
    "        self.scoring = scoring\n",
    "        self.random_state = random_state\n",
    "\n",
    "    def fit(self, model, x, y):\n",
    "        best = fmin(lambda params: self.objective(model, params, x, y),\n",
    "                    self.space, algo=tpe.suggest, max_evals=self.max_evals)\n",
    "        best_params = space_eval(self.space, best)\n",
    "        model.set_params(**best_params)\n",
    "        model.fit(x, y)\n",
    "\n",
    "    def objective(self, model, params, x, y):\n",
    "        model.set_params(**params)\n",
    "        cv = StratifiedKFold(n_splits=self.n_splits, random_state=self.random_state)\n",
    "        score = cross_val_score(model, x, y, cv=cv, scoring=self.scoring)\n",
    "        return 1 - score.mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2459d311-ba8d-4289-92f7-4bb75681a317",
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
