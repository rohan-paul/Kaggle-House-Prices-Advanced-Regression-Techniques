from subprocess import check_output
print(check_output(["ls", "../input/santander-value-prediction-challenge/"]).decode("utf8"))

# Note the file structure
# "../input/name-of-the-kaggle-competition/"