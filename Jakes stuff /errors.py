{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c3e8e18c-8ee1-40f9-ada1-7e0a7f61d036",
   "metadata": {},
   "outputs": [],
   "source": [
    "class InvalidDate(Exception):\n",
    "    def __init__(self, day, month, year):\n",
    "        message = \"Date with year set to {year}, month set to {month}, and day set to {day} is invalid\"\\\n",
    "            .format(\n",
    "                year=year,\n",
    "                month=month,\n",
    "                day=day,\n",
    "            )\n",
    "        super().__init__(message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "12c55db4-af76-49e2-9fbb-a1e0c091c983",
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
