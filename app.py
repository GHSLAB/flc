import dash
from dash import html
import feffery_antd_components as fac
import feffery_leaflet_components as flc

from server import app
from config import AppConfig

from map import tileslecter


# main
app.layout = html.Div(
    fac.AntdSider(),
    [
        flc.LeafletMap(
            flc.LeafletTileLayer(id="tile-layer", zIndex=1),
            #  定义地图框高度
            style={"height": "100vh", "width": "100%"},
            #  定义地图中心点和缩放级别
            center=AppConfig.defultCenter,
            zoom=AppConfig.zoomLevel,
            editToolbar=True,
            # editToolbarControlsOptions={
            #     "position": "topright",  # 工具栏位置
            #     "drawText": True,
            #     "oneBlock": True,  # 工具栏单块
            #     "cutPolygon": True,  # 允许裁剪多边形
            # },
            showMeasurements=True,  # 显示图形测量信息
            measureControl=True,  # 显示测量工具
            # measureControlOptions={"position": "topleft"},  # 工具位置
        ),
        # 底图切换器
        flc.LeafletTileSelect(
            id="tile-select",
            # 默认底图
            selectedUrl=tileslecter.basemap[0]["url"],
            # 底图url
            urls=tileslecter.basemap,
            containerVisible=False,
            # 缩略图参数
            center=AppConfig.defultCenter,
            zoom=7,
        ),
        # flc.LeafletMapListener(),
    ],
)

if __name__ == "__main__":
    app.run(debug=True, port=AppConfig.port)  # develop
    # app.run(host="0.0.0.0", debug=False, port=AppConfig.port)  # deploy
