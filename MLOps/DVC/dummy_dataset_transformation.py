import pandas as pd 

if __name__ == "__main__":
    
    df = pd.read_csv("./data/dataset.csv")
    df = df.drop(columns="Genre")
    df.to_csv("./data/dataset.csv")
    
    print("Dataset modified.")