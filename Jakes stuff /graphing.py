{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9daebd84-6183-4d36-984c-9486e6de9b5a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import math\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import scipy.stats as sci_stats\n",
    "from sklearn.linear_model import LinearRegression\n",
    "import statistics as stats\n",
    "import statsmodels.api as sm\n",
    "from statsmodels.compat import lzip\n",
    "from yellowbrick.regressor import ResidualsPlot\n",
    "\n",
    "\n",
    "def pred_vs_actual(predictions, target, r_squared, out_path=None):\n",
    "    \"\"\"Create and returnsa scatter plot of a model's predictions versus target variables\n",
    "    Args:\n",
    "        predictions: The predictions from a regression\n",
    "        target: The target variable of a regression\n",
    "        r_squared: The r_squared of a regression\n",
    "        out_path: An optional path to save the graph to\n",
    "    Returns:\n",
    "        The predicted vs. actual graph\n",
    "    \"\"\"\n",
    "\n",
    "    # Generate coordinates for a 1:1 line\n",
    "    minimum = int(predictions.min()) - 1\n",
    "    maximum = int(predictions.max()) + 1\n",
    "    diag_line_x = [i for i in range(minimum, maximum)]\n",
    "    diag_line_y = [i for i in diag_line_x]\n",
    "\n",
    "    # Build Scatterplot\n",
    "    fig, ax = plt.subplots()\n",
    "    ax.scatter(predictions, target)\n",
    "    ax.set_title(\"Predicted vs. Actual\")\n",
    "    ax.set_xlabel(\"Predicted\")\n",
    "    ax.set_ylabel(\"Actual\")\n",
    "    ax.axhline(0, c=\"k\", linewidth=0.25)\n",
    "    ax.plot(diag_line_x, diag_line_y, c=\"r\")\n",
    "    ax.text(0.1, 0.9, \"R^2 = {}\".format(r_squared), transform=ax.transAxes, bbox=dict(fill=False))\n",
    "\n",
    "    if out_path:\n",
    "        fig.savefig(fname=out_path)\n",
    "    return fig\n",
    "\n",
    "\n",
    "def residuals_vs_fitted(predictions, residuals, out_path=None):\n",
    "    \"\"\"Create and return a scatter plot of a model's fitted values (predictions) versus the residuals\n",
    "    Args:\n",
    "        predictions: The predictions from a regression\n",
    "        residuals: The residuals from a regression\n",
    "        out_path: An optional path to save the graph to\n",
    "    Returns:\n",
    "        The residuals vs. fitted graph\n",
    "    \"\"\"\n",
    "    # Get Jarque-bera test of normality\n",
    "    name = ['Jarque-Bera', 'Chi^2 two-tail prob.', 'Skew', 'Kurtosis']\n",
    "    test = sm.stats.jarque_bera(residuals)\n",
    "    jarque_bera = lzip(name, test)\n",
    "    p_value = jarque_bera[1][1]\n",
    "\n",
    "    mu = 0\n",
    "    variance = stats.variance(residuals)\n",
    "    sigma = math.sqrt(variance)\n",
    "    x = np.linspace(mu-4*sigma, mu+4*sigma, 100)\n",
    "\n",
    "    # Build Scatterplot\n",
    "    fig, ax = plt.subplots(nrows=1, ncols=2, gridspec_kw={'width_ratios': [3, 1]})\n",
    "    ax[0].scatter(predictions, residuals)\n",
    "    ax[0].set_title(\"Residuals vs. Fitted Values\")\n",
    "    ax[0].set_xlabel(\"Fitted Values\")\n",
    "    ax[0].set_ylabel(\"Residuals\")\n",
    "    ax[0].axhline(0, c=\"k\", linewidth=0.5)\n",
    "    ax[1].hist(residuals, bins=30, orientation=\"horizontal\")\n",
    "    # ax[1].set_xticks(np.linspace(0, round(ax[1].get_xbound()[1]), 3))\n",
    "    ax2 = ax[1].twiny()\n",
    "    # ax2.set_xticks(np.linspace(0, round(ax2.get_xbound()[1], 2), 3))\n",
    "    ax2.plot(sci_stats.norm.pdf(x, mu, sigma), x, color=\"red\")\n",
    "    ax[1].set_xlabel(\"Frequency\")\n",
    "    ax[1].set_title(\"Residual Distribution\")\n",
    "    fig.tight_layout()\n",
    "    align_xaxis(ax[1], 0, ax2, 0)\n",
    "    if out_path:\n",
    "        fig.savefig(out_path)\n",
    "    return fig\n",
    "\n",
    "\n",
    "def cooks_distance(cooks_d, out_path=None):\n",
    "    \"\"\"Create and return a cook's distance graph\n",
    "    Args:\n",
    "        cooks_d: Cook's distance from a regression\n",
    "        out_path: optional path to save the figure to\n",
    "    Returns:\n",
    "        The cook's distance graph\n",
    "    \"\"\"\n",
    "    fig, ax = plt.subplots()\n",
    "    ax.stem(np.arange(len(cooks_d)), cooks_d)\n",
    "    ax.set_title(\"Cook's Distance\")\n",
    "    ax.set_xlabel(\"Residuals\")\n",
    "    ax.set_ylabel(\"Cook's Distance\")\n",
    "    if out_path:\n",
    "        fig.savefig(out_path)\n",
    "    return fig\n",
    "\n",
    "\n",
    "def residual_independence(residuals):\n",
    "    \"\"\"Create a residual time series plot to check for independence.\n",
    "    Row number on X-axis, Residual on Y-axis\n",
    "    Args:\n",
    "        residuals: Pandas series holding residuals\n",
    "    \"\"\"\n",
    "    indices = [x for x in range(len(residuals))]\n",
    "    fig, ax = plt.subplots()\n",
    "    ax.stem(indices, residuals)\n",
    "    ax.set_title(\"Residual Independence\")\n",
    "    ax.set_xlabel(\"Row Number\")\n",
    "    ax.set_ylabel(\"Residual\")\n",
    "    return fig\n",
    "\n",
    "\n",
    "def align_xaxis(ax1, v1, ax2, v2):\n",
    "    \"\"\"adjust ax2 ylimit so that v2 in ax2 is aligned to v1 in ax1\"\"\"\n",
    "    _, x1 = ax1.transData.transform((0, v1))\n",
    "    _, x2 = ax2.transData.transform((0, v2))\n",
    "    inv = ax2.transData.inverted()\n",
    "    _, dx = inv.transform((0, 0)) - inv.transform((0, x1-x2))\n",
    "    minx, maxx = ax2.get_xlim()\n",
    "    ax2.set_xlim(minx+dx, maxx+dx)\n",
    "\n",
    "\n",
    "def residuals_yellowbrick(predictors, target):\n",
    "    \"\"\"Returns a residuals vs. fitted graph with a histogram. Not currently functional.\n",
    "    For future development. uses yellowbrick, which makes good graphs, but experiencing an unexplained missing\n",
    "    argument TypeError\n",
    "    \"\"\"\n",
    "    lm = LinearRegression\n",
    "    visualizer = ResidualsPlot(lm)\n",
    "    visualizer.fit(predictors, target)\n",
    "    return visualizer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "143f7b60-85ea-45c4-b867-a33174769857",
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
