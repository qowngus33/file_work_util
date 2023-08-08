import plotly.express as px
import pandas as pd

if __name__ == "__main__":
    Train_data_dis = pd.DataFrame({'class': ["glasses", "safety glasses", "sandals", "shoes","glasses", "safety glasses", "sandals", "shoes"],
                                   'count': [376,        369,              6464,      6120,   4445,      4791,             476,       492],
                                   'Kind' : ['Crawl','Crawl','Crawl','Crawl','Lab','Lab','Lab','Lab']})

    Test_data_dis = pd.DataFrame({'class': ["glasses", "safety glasses", "sandals", "shoes", "glasses",      "safety glasses",  "sandals",         "shoes"],
                                  'count': [30,         25,               169,       256,     320,            119,              93,                574],
                                  'Kind' : ['VIG',     'VIG',             'VIG',    'VIG',   'Kiosk Collect','Kiosk Collect',   'Kiosk Collect',   'Kiosk Collect']})

    long_df = px.data.medals_long()
    print(type(long_df))
    print(long_df)
    print(Test_data_dis)
    print(sum(Test_data_dis.get('count')))

    fig = px.bar(Test_data_dis, x="class", y="count", color="Kind", title="Test data distribution",text='count')
    fig.update_traces(
        textfont_size=20,
        textposition='auto',
    )
    fig.show()
