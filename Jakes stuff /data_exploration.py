{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "8639b0c5-2da6-44c1-8f20-93b72fb7ce16",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from scipy.stats import norm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "54b61727-896c-43ed-9d9b-9d449d8f37aa",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'databall'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[0;32m/var/folders/pb/9nrds4y576x41j1jw01gnkc40000gn/T/ipykernel_8939/2133253240.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      7\u001b[0m     \u001b[0msys\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmodule_path\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mdataball\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdatabase\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mDatabase\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     10\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mdataball\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mplotting\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mformat_538\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkde\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0mdataball\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mutil\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mprint_df\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'databall'"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import sys\n",
    "\n",
    "module_path = os.path.abspath(os.path.join('..'))\n",
    "\n",
    "if module_path not in sys.path:\n",
    "    sys.path.append(module_path)\n",
    "\n",
    "from databall.database import Database\n",
    "from databall.plotting import format_538, kde\n",
    "from databall.util import print_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d532c92a-9d40-45b2-baaa-e3f83935cf5a",
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
