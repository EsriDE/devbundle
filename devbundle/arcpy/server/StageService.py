# Generated documentation for module arcpy.server


class StageService(object):
    """
    Stages a service definition. A staged service definition file (.sd) contains all the necessary information to share a web layer, locator, web tool, or service.
    """

    @property
    def description(self) -> str:
        return """

        StageService_server(in_service_definition_draft, out_service_definition, {staging_version})

        Stages a service definition. A staged service definition file (.sd)
        contains all the necessary information to share a web layer, locator,
        web tool, or service.

     INPUTS:
      in_service_definition_draft (File):
          The input draft service definition. Service definition drafts can be
          created using the arcpy.sharing module or the CreateGeocodeSDDraft or
          CreateGPSDDraft ArcPy functions.
      staging_version {Long}:
          The version of the published service definition.When sharing a
          feature, a tile, or an imagery layer to ArcGIS
          Enterprise, use 5 for the value. When sharing a map image layer or web
          tool to ArcGIS Enterprise, and any layer type to ArcGIS Online, use
          102 for the value. This is the default.When sharing a web tool or
          geoprocessing service to ArcGIS Enterprise
          or ArcGIS Server using the GeoprocessingSharingDraft or
          CreateGPSDDraft function, use the value corresponding to the version
          number from the following list:11.3--
          33011.2-32011.1-31011.0-30010.9.1-20910.9-20810.8.1-20610.8-2051
          0.7.1-20410.7-20310.6.1-20210.6-20110.5.1-200

     OUTPUTS:
      out_service_definition (File):
          The resulting service definition. The default is to write the service
          definition to the same directory as the draft service definition.

        """