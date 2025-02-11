import pydeck as pdk
import pandas as pd

data = pd.DataFrame({
    "latitude": [48.8566],
    "longitude": [2.3522]
})

layer = pdk.Layer(
    "ScatterplotLayer",
    data,
    get_position=["longitude", "latitude"],
    get_fill_color=[255, 0, 0],
    get_radius=100,
)

view_state = pdk.ViewState(latitude=48.8566, longitude=2.3522, zoom=10)

pdk.Deck(layers=[layer], initial_view_state=view_state).show()
