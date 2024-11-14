import dash
from dash.dependencies import Output, Input, State

import feffery_leaflet_components as flc
from feffery_dash_utils.style_utils import style
from server import app

from config import AppConfig


# 回调函数。
# 输入组件"tile-select"的"selectedUrl"属性发生变化时，触发回调函数。
# 函数作用将新选择图层URL传递给"tile-layer"，从而改变地图的底图图层。
@app.callback(Output("tile-layer", "url"), Input("tile-select", "selectedUrl"))
def change_tile_layer(selectedUrl):
    return selectedUrl
