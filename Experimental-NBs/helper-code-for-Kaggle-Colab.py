# Kaggle Code to print all Kaggle Input file names for dataset,
# So I can refer them correctly within a Kaggle notebook
from subprocess import check_output
print(check_output(["ls", "../input/santander-value-prediction-challenge/"]).decode("utf8"))

# Note the file structure
# "../input/name-of-the-kaggle-competition/"

# *****************************************

# Colab - Code to include input file for data-set in Colab from Github
url = 'https://raw.githubusercontent.com/rohan-paul/Kaggle-House-Prices-Advanced-Regression-Techniques/master/input/house-prices-advanced-regression-techniques/train.csv'
df_train = pd.read_csv(url)

# *****************************************