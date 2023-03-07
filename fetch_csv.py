import json
import pymongo
import pandas as pd
import jason

client = pymongo.MongoClient("mongodb+srv://khan:Remember1@cluster0.kgaamxe.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r"D:\MachineLearningProject\MachineLearningProject\insurance.csv")
DATABASE_NAME = "InsuranceML"
COLLECTION_NAME = "Ml_Project"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)