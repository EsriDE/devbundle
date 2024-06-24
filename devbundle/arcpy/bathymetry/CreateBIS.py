# Generated documentation for module arcpy.bathymetry


class CreateBIS(object):
    """
    Creates a Bathymetric Information System (BIS) in a designated geodatabase workspace.
    """

    @property
    def description(self) -> str:
        return """

        CreateBIS_bathymetry(in_workspace, in_template, in_proxy_raster_location, {coordinate_system}, {config_keyword})

        Creates a Bathymetric Information System (BIS) in a designated
        geodatabase workspace.

     INPUTS:
      in_workspace (Workspace):
          The enterprise or file geodatabase in which the output BIS will be
          created.
      in_template (Table View):
          The BIS schema file that contains the table used as a template to
          define the attribute fields of the new BIS. Use the
          BisCatalog_schema_MGDB.geodatabase file located at <installation
          location>\ArcGIS\Pro\Resources\Bathymetry.
      in_proxy_raster_location (Folder):
          The specified proxy raster location that will be saved to the
          BISDetails table. You must have read and write access to the proxy
          raster location. This location is used by the Add Point Data To BIS
          tool to store proxy rasters.
      coordinate_system {Coordinate System}:
          The spatial reference of the BIS Workspace. If no coordinate system is
          provided, WGS84 will be used by default.
      config_keyword {String}:
          The configuration keyword applies to enterprise geodatabase data only.
          It determines the storage parameters of the database table.

        """