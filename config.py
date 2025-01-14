class AppConfig:
    # 应用标签页title
    app_title: str = "flc-template"

    port: int = 8000

    # 初始地图中心
    defultCenter: dict = {"lng": 0, "lat": 0}

    # 初始缩放级别
    zoomLevel: int = 8
