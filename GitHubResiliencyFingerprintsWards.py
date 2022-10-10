# Import Packages
import plotly.express as px
import pandas as pd

# Read Data
df = pd.read_csv(r'')
print(df)
# Select Subward
#df = df[df['ward'].isin(['Mikocheni'])]
#print(df)

# Convert from wide data to long data to plot radar chart
df = pd.melt(df, id_vars=['subward'], var_name='category', value_name='rating',
             value_vars=['Built Density', 'Building Diversity', 'Integration',
                         'Connectivity','Microclimate','Heat Stress','Population Density'],
             )
print(df)

# Create Radar Chart
fig = px.line_polar(df, r='rating', theta='category', color='subward', line_close=True,
                            line_shape='linear',  # or spline
                    hover_name='subward',
                    hover_data={'subward':False},
                    markers=True,
                    # labels={'rating':'stars'},
                    # text='Hotelid',
                    range_r=[0,1],
                    direction='clockwise',  # or counterclockwise
                    start_angle=45
                    )
#fig.update_traces(fill='toself')
fig.show()