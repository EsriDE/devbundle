class SoftwareProduct(object):
    """
    Represents the base class of a software product.
    """

    def __init__(self, name: str, description: str, url: str) -> None:
        """
        Creates a new software product.

        :param str name: The name of the software product.
        :param str description: The description of the software product.
        :param str url: The website url of the software product.
        """
        self._name = name
        self._description = description
        self._url = url

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description
    
    @property
    def url(self) -> str:
        return self._url
    
    def __repr__(self) -> str:
        return f'{self.name}: {self.description}'


class ArcGISEnterprise(SoftwareProduct):
    """
    Represents ArcGIS Enterprise.
    """

    def __init__(self) -> None:
        super().__init__(
            'ArcGIS Enterprise', 
            'Deliver industry-leading mapping and analytics to your infrastructure and the cloud.',
            'https://enterprise.arcgis.com/en/'
        )


class ArcGISNotebookServer(SoftwareProduct):
    """
    Represents ArcGIS Notebook Server.
    """

    def __init__(self) -> None:
        super().__init__(
            'ArcGIS Notebook Server', 
            'The power of data science in your enterprise GIS.',
            'https://enterprise.arcgis.com/en/notebook/'
        )


class ArcGISKnowledge(SoftwareProduct):
    """
    Represents ArcGIS Knowledge.
    """

    def __init__(self) -> None:
        super().__init__(
            'ArcGIS Knowledge', 
            'Where knowledge graphs and link analysis meet GIS.',
            'https://enterprise.arcgis.com/en/knowledge/'
        )


class ArcGISGeoEventServer(SoftwareProduct):
    """
    Represents ArcGIS GeoEvent Server.
    """

    def __init__(self) -> None:
        super().__init__(
            'ArcGIS GeoEvent Server', 
            'Real-time visualization and analytics in your frontline GIS apps.',
            'https://enterprise.arcgis.com/en/geoevent/'
        )


class ArcGISGeoAnalyticsServer(SoftwareProduct):
    """
    Represents ArcGIS GeoAnalytics Server.
    """

    def __init__(self) -> None:
        super().__init__(
            'ArcGIS GeoAnalytics Server', 
            'Bring advanced big data analytics to your organization.',
            'https://enterprise.arcgis.com/en/geoanalytics/'
        )


class ArcGISImageServer(SoftwareProduct):
    """
    Represents ArcGIS Image Server.
    """

    def __init__(self) -> None:
        super().__init__(
            'ArcGIS Image Server', 
            'Share large volumes of imagery and power raster analytics.',
            'https://enterprise.arcgis.com/en/image/'
        )