import dash
# import dash_html_components as html
from dash import html

from dash.dependencies import Input, Output
from tkinter import filedialog, Tk
import pandas as pd
import joblib
import os
import joblib as old_joblib
from scipy.stats import mode
from sklearn.tree import DecisionTreeClassifier

# Load the model using the older version of scikit-learn

clf = old_joblib.load('dt.pkl')
# model_path=os.path.join('C:/Users/LAVANYA/Desktop/Main_Project/','models/dt_tree.sav')
# random_for=joblib.load(model_path)



# Re-save the model using the current version of joblib
# joblib.dump(clf, 'decision_tree_revised.pkl')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div(style={'background-color': 'blue'}),
    html.H1(children=' INTRUSION Detection USING MACHINE LEARNING', style={'marginBottom': '12px'}),
    html.H2("SELECT Input Data TO TEST", style={'marginBottom': '6px'}),
    html.Button(id='submit-button', n_clicks=0, children='UPLOAD THE Test Data DETAILS',
                style={'marginTop': 15, 'marginBottom': 25}),
    html.Div(id='result-div'),
], style={'textAlign': 'center'})


@app.callback(
    Output('result-div', 'children'),
    [Input('submit-button', 'n_clicks')]
)
def display_predicted_result(n_clicks):
    if n_clicks > 0:
        try:
            root = Tk()
            root.attributes("-topmost", True)  # Bring the Tkinter window to the top
            path = 'D:/Lavanya/dataset/input'  # Use forward slashes for file paths
            root.filename = filedialog.askopenfilename(initialdir=path, title="Select file",
                                                        filetypes=(("Network files", "*.csv"), ("all files", "*.*")))
            root.destroy()

            if root.filename:
                # Load the data
                df = pd.read_csv(root.filename)
                X = df.values
                
                # Make predictions
                Class = clf.predict(X)
                print('Class:', Class)
                val = mode(Class)[0]
                val=int(val)

                d = {0: 'BENIGN', 1: 'DoS Hulk', 2: 'PortScan', 3: 'DDoS', 4: 'DoS GoldenEye', 5: 'FTP-Patator',
                     6: 'SSH-Patator', 7: 'DoS slowloris', 8: 'DoS Slowhttptest', 9: 'Bot',
                     10: 'Web Attack Brute Force',
                     11: 'Web Attack XSS', 12: 'Infiltration', 13: 'Web Attack Sql Injection', 14: 'Heartbleed'}
                predicted_result = 'Predicted Result: ' + d[val]

                # return html.H1(predicted_result, style={'marginBottom': '10px'})
                return html.H1(predicted_result, style={'marginBottom': '10px'})


            else:
                return html.H1('No file selected!', style={'marginBottom': '10px'})
        except Exception as e:
            return html.H1(f"Error: {e}", style={'marginBottom': '10px'})


if __name__ == '__main__':
    app.run_server()
