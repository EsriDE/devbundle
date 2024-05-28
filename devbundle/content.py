from typing import List
from .software import SoftwareProduct, ArcGISEnterprise, ArcGISNotebookServer, ArcGISKnowledge, ArcGISGeoEventServer, ArcGISGeoAnalyticsServer, ArcGISImageServer


class DevBundle(object):
    """
    Represents the ArcGIS Developer Bundle.
    """

    def __init__(self) -> None:
        self._software = [
            ArcGISEnterprise(),
            ArcGISNotebookServer(),
            ArcGISKnowledge(),
            ArcGISGeoEventServer(),
            ArcGISGeoAnalyticsServer(),
            ArcGISImageServer()
        ]

    @property
    def software(self) -> List[SoftwareProduct]:
        return self._software
    
    @property
    def software_names(self) -> List[SoftwareProduct]:
        return [software.name for software in self.software]
    
    @property
    def websites(self) -> List[str]:
        return [software.url for software in self.software]
    
    def __repr__(self) -> str:
        return f'Includes {", ".join([software.name for software in self.software])}'