import pandas as pd


# Need to clear ut_transcription.csv.
# Need to populate ut_transcription.csv with transcription_scv_builder.
# Need to clear '../data/analysis_base_tables/master_audio.csv'
master_audio = '/Users/boydbrown/Cross_Capture_Sentiment_Analysis/omni_retail_project/data/analysis_base_tables/master_audio.csv'


def make_audio_df(transcription_dir):
    df_audio = pd.read_csv(transcription_dir,
                           names=['Tester_id', 'Audio_text'])
    df_audio.insert(loc=0, column='Test_id', value=df_audio['Tester_id'].apply(
        lambda x: x[:-1]))
    df_audio.to_csv(master_audio, header=True, index=True)
    print df_audio.head()

if __name__ == '__main__':
    ffn = '/Users/boydbrown/Cross_Capture_Sentiment_Analysis/omni_retail_project/data/analysis_base_tables/master_audio.csv'
    make_audio_df(ffn)
