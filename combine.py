import pandas as pd


def combine(input_file_1, input_file_2, input_file_3):
    df1 = pd.read_csv(
            input_file_1
    )

    df2 = pd.read_csv(
            input_file_2
    )

    df3 = pd.read_csv(
            input_file_3
    )

    df = pd.concat([df1, df2, df3], ignore_index=True)

    df['original_text'] = df['original_text'].str.lower()

    return df


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input_file_1', help='First data file to combine (CSV)')
    parser.add_argument('input_file_2', help='Second data file to combine (CSV)')
    parser.add_argument('input_file_3', help='Third data file to combine (CSV)')
    parser.add_argument('output_file', help='Combined data file (CSV)')
    args = parser.parse_args()

    combine = combine(args.input_file_1, args.input_file_2, args.input_file_3)
    combine.to_csv(args.output_file, index=False)