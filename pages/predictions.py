from joblib import load
pipeline = load('assets/pipeline1.joblib')

# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('## Criteria', className='mb-5'), 
        dcc.Markdown('#### Year'), 
        dcc.RangeSlider(
            id='Year', 
            min=1900, 
            max=2022, 
            step=1, 
            value=[1902, 2020], 
            marks={n: str(n) for n in range(1900,2022,20)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### Genre'), 
        dcc.Checklist(
           id='Genre', 
            options = [
                {'label': 'Action', 'value': 'Action'}, 
                {'label': 'Adventure', 'value': 'Adventure'}, 
                {'label': 'Animation', 'value': 'Animation'}, 
                {'label': 'Biography', 'value': 'Biography'}, 
                {'label': 'Comedy', 'value': 'Comedy'},
                {'label': 'Crime', 'value': 'Crime'}, 
                {'label': 'Documentary', 'value': 'Documentary'}, 
                {'label': 'Drama', 'value': 'Drama'}, 
                {'label': 'Family', 'value': 'Family'}, 
                {'label': 'Fantasy', 'value': 'Fantasy'}, 
                {'label': 'Film Noir', 'value': 'Film Noir'}, 
                {'label': 'History', 'value': 'History'}, 
                {'label': 'Horror', 'value': 'Horror'}, 
                {'label': 'Music', 'value': 'Music'}, 
                {'label': 'Musical', 'value': 'Musical'},
                {'label': 'Mystery', 'value': 'Mystery'}, 
                {'label': 'Romance', 'value': 'Romance'}, 
                {'label': 'Sci-Fi', 'value': 'Sci-Fi'}, 
                {'label': 'Short Film', 'value': 'Short Film'}, 
                {'label': 'Sport', 'value': 'Sport'}, 
                {'label': 'Superhero', 'value': 'Superhero'}, 
                {'label': 'Thriller', 'value': 'Thriller'}, 
                {'label': 'War', 'value': 'War'},
                {'label': 'Western', 'value': 'Western'}, 
            ], 
            className='mb-5', 
        ),
        dcc.Markdown('#### Runtime in Minutes'), 
        dcc.RangeSlider(
            id = 'Runtime',
            min=2,
            max=260,
            step=1,
            marks={
                2: '2', 
                65: '65', 
                130: '130',
                195: '195', 
                260: '260'
            },
            value=[2, 260]
        ), 
        dcc.Markdown('#### Age'), 
        dcc.Checklist(
           id='Age', 
            options = [
                {'label': 'All', 'value': 'All'}, 
                {'label': '7+', 'value': '7+'}, 
                {'label': '13+', 'value': '13+'}, 
                {'label': '16+', 'value': '16+'}, 
                {'label': '18+', 'value': '18+'},  
            ], 
            className='mb-5', 
        ),
        dcc.Markdown('#### Streaming Platform'), 
        dcc.Checklist(
           id='Streaming', 
            options = [
                {'label': 'Netflix', 'value': 'Netflix'}, 
                {'label': 'Hulu', 'value': 'Hulu'}, 
                {'label': 'Prime Video', 'value': 'Prime Video'}, 
                {'label': 'Disney+', 'value': 'Disney+'}  
            ], 
            className='mb-5', 
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Movie', className = 'mb-5'),
        html.Div(id='output', className = 'lead')
    ]
)

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

@app.callback(
    Output('output', 'children'),
    [Input('Year', 'value'), 
     Input('Action', 'value'), 
     Input('Adventure', 'value'), 
     Input('Animation', 'value'), 
     Input('Biography', 'value'), 
     Input('Comedy', 'value'), 
     Input('Crime', 'value'), 
     Input('Documentary', 'value'), 
     Input('Drama', 'value'), 
     Input('Family', 'value'), 
     Input('Fantasy', 'value'), 
     Input('Film Noir', 'value'), 
     Input('History', 'value'), 
     Input('Horror', 'value'), 
     Input('Music', 'value'), 
     Input('Musical', 'value'), 
     Input('Mystery', 'value'), 
     Input('Romance', 'value'), 
     Input('Sci-Fi', 'value'), 
     Input('Short Film', 'value'), 
     Input('Sport', 'value'), 
     Input('Superhero', 'value'), 
     Input('Thriller', 'value'), 
     Input('War', 'value'), 
     Input('Western', 'value'), 
     Input('Runtime', 'value'), 
     Input('All', 'value'), 
     Input('7+', 'value'), 
     Input('13+', 'value'), 
     Input('16+', 'value'), 
     Input('18+', 'value'), 
     Input('Netflix', 'value'), 
     Input('Hulu', 'value'), 
     Input('Prime Video', 'value'), 
     Input('Disney+', 'value'), 
    ],
)
def predict(Year, Genre, Runtime, Age, Streaming):
    df = pd.DataFrame(
        columns = ['Year', 'Genre', 'Runtime', 'Age', 'Streaming'], 
        data = [[Year, Genre, Runtime, Age, Streaming]]
    )
    y_pred = pipeline.predict(df)[0]
    return "test"

if __name__ == '__main__':
    app.run_server(debug=True)

layout = dbc.Row([column1, column2])