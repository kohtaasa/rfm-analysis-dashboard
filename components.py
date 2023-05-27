import pandas as pd
import plotly.express as px


def create_treemap(df: pd.DataFrame) -> px.treemap:
    treemap = px.treemap(df.groupby('segment')['CustomerID'].nunique().reset_index(),
                         path=['segment'],
                         values='CustomerID',
                         labels={'CustomerID': 'Number of Customers'},
                         color='segment',
                         color_discrete_sequence=px.colors.qualitative.D3
                         )

    treemap.update_layout(margin={"r": 20, "t": 20, "l": 20, "b": 20},
                          template='plotly_white',
                          plot_bgcolor='rgba(0, 0, 0, 0)',
                          paper_bgcolor='rgba(0, 0, 0, 0)'
                          )

    return treemap


def create_bubble_chart(df: pd.DataFrame) -> px.scatter:
    bubble_chart = px.scatter(df.groupby('segment').mean().reset_index().round(2),
                              x='Recency_rank',
                              y='Frequency_rank',
                              size='Monetary_rank',
                              color='segment',
                              hover_name='segment',
                              text='segment',
                              size_max=30,
                              color_discrete_sequence=px.colors.qualitative.D3)

    bubble_chart.update_traces(textposition='bottom center')

    bubble_chart.update_layout(margin={"r": 20, "t": 20, "l": 20, "b": 20},
                               template='plotly_white',
                               plot_bgcolor='rgba(0, 0, 0, 0)',
                               paper_bgcolor='rgba(0, 0, 0, 0)',
                               xaxis_title='R Score',
                               yaxis_title='F Score',
                               showlegend=False)

    # bubble_chart.update_yaxes(gridcolor='#626363')
    # bubble_chart.update_xaxes(gridcolor='#626363')

    return bubble_chart


def create_recency_hist(df: pd.DataFrame) -> px.histogram:
    recency_hist = px.histogram(df, x='Recency')

    recency_hist.update_layout(margin={"r": 20, "t": 20, "l": 20, "b": 20},
                               template='plotly_white',
                               plot_bgcolor='rgba(0, 0, 0, 0)',
                               paper_bgcolor='rgba(0, 0, 0, 0)'
                               )

    recency_hist.update_traces(marker=dict(color='#1F77B4'))

    # recency_hist.update_yaxes(gridcolor='#626363')

    return recency_hist


def create_frequency_hist(df: pd.DataFrame) -> px.histogram:
    frequency_hist = px.histogram(df, x='Frequency')

    # f_hist.update_traces(marker=dict(color='#00cc96'))

    frequency_hist.update_layout(margin={"r": 20, "t": 20, "l": 20, "b": 20},
                                template='plotly_white',
                                plot_bgcolor='rgba(0, 0, 0, 0)',
                                paper_bgcolor='rgba(0, 0, 0, 0)'
                                )

    frequency_hist.update_traces(marker=dict(color='#1F77B4'))

    # frequency_hist.update_yaxes(gridcolor='#626363')

    return frequency_hist


def create_recency_bar(df: pd.DataFrame) -> px.bar:
    recency_bar = px.bar(df.groupby('Recency_rank')['Recency'].mean().reset_index(),
                         x='Recency_rank',
                         y='Recency',
                         labels={'Recency_rank': 'R Score', 'Recency': 'Average R Value'}
                         )

    recency_bar.update_layout(margin={"r": 20, "t": 20, "l": 20, "b": 20},
                              template='plotly_white',
                              plot_bgcolor='rgba(0, 0, 0, 0)',
                              paper_bgcolor='rgba(0, 0, 0, 0)'
                              )

    recency_bar.update_traces(marker=dict(color='#1F77B4'))

    # recency_bar.update_yaxes(gridcolor='#626363')

    return recency_bar


def create_frequency_bar(df: pd.DataFrame) -> px.bar:
    frequency_bar = px.bar(df.groupby('Frequency_rank')['Frequency'].mean().reset_index(),
                           x='Frequency_rank',
                           y='Frequency',
                           labels={'Frequency_rank': 'F Score', 'Frequency': 'Average F Value'}
                           )

    frequency_bar.update_layout(margin={"r": 20, "t": 20, "l": 20, "b": 20},
                                template='plotly_white',
                                plot_bgcolor='rgba(0, 0, 0, 0)',
                                paper_bgcolor='rgba(0, 0, 0, 0)'
                                )

    frequency_bar.update_traces(marker=dict(color='#1F77B4'))

    # frequency_bar.update_yaxes(gridcolor='#626363')

    return frequency_bar


def create_monetary_bar(df: pd.DataFrame) -> px.bar:
    monetary_bar = px.bar(df.groupby('Monetary_rank')['Monetary'].mean().reset_index(),
                          x='Monetary_rank',
                          y='Monetary',
                          labels={'Monetary_rank': 'M Score', 'Monetary': 'Average M Value'}
                          )

    monetary_bar.update_layout(margin={"r": 20, "t": 20, "l": 20, "b": 20},
                               template='plotly_white',
                               plot_bgcolor='rgba(0, 0, 0, 0)',
                               paper_bgcolor='rgba(0, 0, 0, 0)'
                               )

    monetary_bar.update_traces(marker=dict(color='#1F77B4'))

    # monetary_bar.update_yaxes(gridcolor='#626363')

    return monetary_bar


def create_table_dataset(df: pd.DataFrame) -> pd.DataFrame:
    table_df = df.drop('CustomerID', axis=1).groupby('segment').mean().reset_index().round(2)

    table_df.rename(columns={'Recency_rank': 'Average R Score',
                             'Recency': 'Average R Value',
                             'Frequency_rank': 'Average F Score',
                             'Frequency': 'Average F Value',
                             'Monetary_rank': 'Average M  Score',
                             'Monetary': 'Average M value',
                             'segment': 'Segment'}, inplace=True)

    return table_df


def create_pie_chart(df: pd.DataFrame):
    pie_chart = px.pie(df.groupby('segment')['Monetary'].sum().reset_index(),
                       values='Monetary',
                       names='segment',
                       color_discrete_sequence=px.colors.qualitative.D3)

    pie_chart.update_layout(margin={"r": 20, "t": 20, "l": 20, "b": 20},
                            template='plotly_white',
                            plot_bgcolor='rgba(0, 0, 0, 0)',
                            paper_bgcolor='rgba(0, 0, 0, 0)'
                            )
    return pie_chart