import pandas as pd
from ml import inference
import argparse

def main():
    arg = argparse.ArgumentParser()
    arg.add_argument('-i', '--input', type=str, default='../df_encoded.csv')
    arg.add_argument('-o', '--output', type=str, default='predictions.csv')
    args = arg.parse_args()
    params = vars(args)

    #df = pd.read_csv('../df_encoded.csv').drop(['loan_status'], axis=1)
    df = pd.read_csv(params['input']).drop(['loan_status'], axis=1)
    y_pr = inference(df)

    df_pr = pd.DataFrame(y_pr, index=df.index, columns=['loan_status'])
    df_pr.to_csv(params['output'])
    #df_pr.to_csv('predictions.csv')


if __name__ == '__main__':
    main()