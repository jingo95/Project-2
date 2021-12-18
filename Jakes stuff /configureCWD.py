{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f75b4fbe-cb3b-44c5-83f4-651918f9d274",
   "metadata": {},
   "outputs": [],
   "source": [
    "# configureCWD.py - Sets current working directory relative to where program folder is located\n",
    "\n",
    "import os\n",
    "\n",
    "# Sets current working directory relative to where program folder is located\n",
    "def setCurrentWorkingDirectory(directoryName):\n",
    "\n",
    "    programDirectory = os.path.dirname(os.path.abspath(__file__))\n",
    "    newCurrentWorkingDirectory = os.path.join(programDirectory, directoryName)\n",
    "    os.chdir(newCurrentWorkingDirectory)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6876394-2b7f-4fdf-b652-b0685c0e1b4f",
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
