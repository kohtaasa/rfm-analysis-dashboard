from dash import Dash, html, dcc, Output, Input
import pandas as pd
import dash_bootstrap_components as dbc

from components import create_treemap, create_bubble_chart, create_recency_hist, create_frequency_hist, \
    create_recency_bar, create_frequency_bar, create_monetary_bar, create_table_dataset, create_pie_chart

df = pd.read_csv('data/rfm_output.csv')

# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.MATERIA]
# external_stylesheets = [dbc.themes.DARKLY]
app = Dash(__name__, external_stylesheets=external_stylesheets)

card_header_style = {'text-align': 'left', 'margin-left': '20px', 'margin-top': '10px', 'margin-bottom': '0px'}
card_header_style_2 = {'text-align': 'left', 'margin-left': '20px', 'margin-top': '10px', 'margin-bottom': '10px'}

description = """
    This RFM (Recency, Frequency, Monetary) analysis dashboard provides insights 
    into customer segmentation based on their purchasing behavior using the 
    E-Commerce Data from a UK retailer, available on Kaggle.

    The RFM analysis helps identify and understand customer segments based on 
    three key factors:
    - Recency: How recently did a customer make a purchase?
    - Frequency: How often do they make purchases?
    - Monetary: How much do they spend on each purchase?

    By segmenting customers based on these factors, businesses can tailor their 
    marketing strategies and optimize customer engagement, retention, and 
    profitability.

    This dashboard visualizes the distribution of customers across different RFM 
    segments and provides actionable insights to drive data-driven decision-making 
    for marketing and sales teams.

    Data Source: [Kaggle - E-Commerce Data Actual transactions from UK retailer]
    (https://www.kaggle.com/carrie1/ecommerce-data)
"""

app.layout = dbc.Container([
    dbc.Row([
        html.H1('RFM Analysis Dashboard'),
    ], style={'padding': '20px', 'text-align': 'center'}),

    dbc.Row(
        dbc.Col(
            dbc.Card(
                [
                    html.H4("Description"),
                    dcc.Markdown(description, style={'textAlign': 'justify'}),
                ], style={'padding': '20px'}
            ),
        ),
        justify="center",
    ),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H5('Number of The Customers in Each Segment',
                        className="card-title",
                        style=card_header_style
                        ),
                dcc.Graph(figure=create_treemap(df),
                          style={'height': '380px'},
                          id='treemap',
                          config={'displayModeBar': False}
                          )
            ])
        ]),
        dbc.Col([
            dbc.Card([
                html.H5('Monetary Percentage by Segment', className="card-title", style=card_header_style_2),
                dcc.Graph(figure=create_pie_chart(df),
                          style={'height': '370px'},
                          id='pie-chart',
                          config={'displayModeBar': False})
            ])
        ])
    ]),

    html.Br(),

    dbc.Row(
        dbc.Col(
            dbc.Card([
                html.H5('R and F Scores by Segment', className="card-title", style=card_header_style),
                dcc.Graph(figure=create_bubble_chart(df),
                          style={'height': '380px'},
                          id='bubble-chart',
                          config={'displayModeBar': False})
            ])
        )
    ),

    html.Br(),

    dbc.Row([
        dbc.Col([
            html.H5('Segment Selector'),
            dcc.Dropdown(
                df['segment'].unique(),
                id='segment-dropdown',
                # style=dropdown_style
            )
        ])
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H5('R Value Distribution', className="card-title", style=card_header_style),
                dcc.Graph(figure=create_recency_hist(df),
                          style={'height': '250px'},
                          id='recency-hist',
                          config={'displayModeBar': False})
            ])
        ], width=6),

        dbc.Col([
            dbc.Card([
                html.H5('F Value Distribution', className="card-title", style=card_header_style),
                dcc.Graph(figure=create_frequency_hist(df),
                          style={'height': '250px'},
                          id='frequency-hist',
                          config={'displayModeBar': False})
            ])
        ], width=6)
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H5('R Score and Average R Value', className="card-title", style=card_header_style),
                dcc.Graph(figure=create_recency_bar(df),
                          style={'height': '220px'},
                          id='recency-bar',
                          config={'displayModeBar': False}
                          )
            ])
        ], width=4),

        dbc.Col([
            dbc.Card([
                html.H5('F Score and Average F Value', className="card-title", style=card_header_style),
                dcc.Graph(figure=create_frequency_bar(df),
                          style={'height': '220px'},
                          id='frequency-bar',
                          config={'displayModeBar': False})
            ])
        ], width=4),

        dbc.Col([
            dbc.Card([
                html.H5('M Score and Average M Value', className="card-title", style=card_header_style),
                dcc.Graph(figure=create_monetary_bar(df),
                          style={'height': '220px'},
                          id='monetary-bar',
                          config={'displayModeBar': False})
            ])
        ], width=4)

    ], justify='around'),

    html.Br(),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                html.H5('Segment Table', className="card-title", style=card_header_style_2),
                dbc.Table.from_dataframe(create_table_dataset(df), striped=False, bordered=False, hover=True, size='sm')
            ])
        ])
    ]),

    html.Br()

], style={'max-width': '1350px', 'margin': 'auto'})


@app.callback(
    Output('recency-hist', 'figure'),
    Output('frequency-hist', 'figure'),
    Output('recency-bar', 'figure'),
    Output('frequency-bar', 'figure'),
    Output('monetary-bar', 'figure'),
    Input('segment-dropdown', 'value')
)
def update_graph(selected_segment):
    if selected_segment:  # Check if a value is selected
        filtered_df = df[df['segment'] == selected_segment]
        return create_recency_hist(filtered_df), create_frequency_hist(filtered_df), create_recency_bar(filtered_df), \
            create_frequency_bar(filtered_df), create_monetary_bar(filtered_df)
    else:
        # Return an empty figure or any other default behavior
        return create_recency_hist(df), create_frequency_hist(df), create_recency_bar(df), create_frequency_bar(df), \
            create_monetary_bar(df)


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=False)
