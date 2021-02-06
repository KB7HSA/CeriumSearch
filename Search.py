import pd

def load_data(path):
        dataframe = pd.read_csv(path)
        return dataframe
