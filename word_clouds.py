#Function to create word clouds for each class of documents
#Output to PIL Image in /outputs

from wordcloud import WordCloud
import pandas as pd

def create_wordcloud(input_file_1):

    cleaned_combined_df =  pd.read_csv(input_file_1)

    clouds = []
    for i in range(0,2):
        df = None
        df = cleaned_combined_df[cleaned_combined_df['label']==i]
        list = ','.join(list(df['original_text']))

        wordcloud = WordCloud(background_color = 'white', contour_width = 3, countour_color = 'steelblue')
        viz = wordcloud.generate(list)
        clouds.append(viz)

    return clouds

    if __name__ == '__main__':
        import argparse

        parser = argparse.ArgumentParser()
        parser.add_argument('input_file_1', help='Cleaned combined df (CSV)')
        parser.add_argument('output_file_1', help='First wordcloud (PNG)')
        parser.add_argument('output_file_2', help='Second wordcloud (PNG)')

        args = parser.parse_args()

        wordclouds = create_wordcloud(args.input_file_1)
        wordclouds[0].to_file(args.output_file_1)
        wordclodus[1].to_file(args.output_file_2)
