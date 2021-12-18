{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "23e1a43c-a5e5-49ec-a973-3fa367d9ab95",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime\n",
    "from json import JSONEncoder\n",
    "from enum import Enum\n",
    "\n",
    "\n",
    "class BasketballReferenceJSONEncoder(JSONEncoder):\n",
    "    def default(self, obj):\n",
    "        if isinstance(obj, datetime):\n",
    "            return obj.isoformat()\n",
    "\n",
    "        if isinstance(obj, Enum):\n",
    "            return obj.value\n",
    "\n",
    "        return JSONEncoder.default(self, obj)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee17e9af-feb3-4000-84f4-5e14f1240844",
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
