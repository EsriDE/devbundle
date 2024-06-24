# Generated documentation for module arcpy.gapro


class CreateBDC(object):
    """
    Creates a multifile feature connection file (.mfc) and item. Datasets registered in a multifile feature connection (MFC) can be used as input to GeoAnalytics Desktop tools and other geoprocessing tools.
    """

    @property
    def description(self) -> str:
        return """

        CreateBDC_gapro(bdc_location, bdc_name, connection_type, {data_source_folder}, {visible_geometry}, {visible_time})

        Creates a multifile feature connection file (.mfc) and item. Datasets
        registered in a multifile feature connection (MFC) can be used as
        input to GeoAnalytics Desktop tools and other geoprocessing tools.

     INPUTS:
      bdc_location (Folder):
          The folder where the .mfc file will be created.
      bdc_name (String):
          The name of the .mfc file to be created.
      connection_type (String):
          Specifies the type of connection to be created.FOLDER-Connect to a
          file system location. This is the default.
      data_source_folder {Folder}:
          The folder containing the datasets to be registered with the MFC.
      visible_geometry {Boolean}:
          Specifies whether the fields used to specify the geometry will be
          visible as fields when the MFC file is used as input to other
          geoprocessing tools. When the geometry fields are not visible,
          geometry is still applied to the dataset. The geometry visibility
          setting can be modified in the MFC.GEOMETRY_VISIBLE-Geometry fields
          will be included as fields for
          analysis. This is the default.GEOMETRY_NOT_VISIBLE-Geometry fields
          will not be included as fields
          for analysis.
      visible_time {Boolean}:
          Specifies whether the fields used to specify the time will be visible
          as fields when the MFC file is used as input to other geoprocessing
          tools. When the time fields are not visible, time is still applied to
          the dataset. The time visibility setting can be modified in the
          MFC.TIME_VISIBLE-Time fields will be included as fields for analysis.
          This
          is the default.TIME_NOT_VISIBLE-Time fields will not be included as
          fields for
          analysis.

        """