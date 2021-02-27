import dash
import dash_html_components as html
# Initialise the app
app = dash.Dash(__name__)

# Define the app
app.layout = html.Div(children=[
                      html.Div(className='row',  # Define the row element
                               children = [
                                  html.H2('Dash - STOCK PRICES'),
                                  html.P('''Visualising time series with Plotly - Dash'''),
                                  html.P('''Pick one or more stocks from the dropdown below.''')
])
])
                                
# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# html.Div([
#     html.H1('Hello Dash'),
#     html.Div([
#         html.P('Dash converts Python classes into HTML'),
#         html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
#     ])
# ])



