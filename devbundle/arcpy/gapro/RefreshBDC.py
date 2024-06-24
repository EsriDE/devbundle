# Generated documentation for module arcpy.gapro


class RefreshBDC(object):
    """
    Refreshes an existing multifile feature connection (MFC) and registers any new datasets that have been added to the source location.
    """

    @property
    def description(self) -> str:
        return """

        RefreshBDC_gapro(bdc_file, {visible_geometry}, {visible_time})

        Refreshes an existing multifile feature connection (MFC) and registers
        any new datasets that have been added to the source location.

     INPUTS:
      bdc_file (File):
          The MFC file to refresh.
      visible_geometry {Boolean}:
          Specifies whether the fields used to identify the geometry will be
          included (visible) as fields for analysis when the MFC file is used in
          other geoprocessing tools. When geometry fields are not visible,
          geometry is still applied to the dataset. The geometry visibility
          setting can be modified in the MFC.GEOMETRY_VISIBLE-Geometry fields
          will be included as fields for
          analysis. This is the default.GEOMETRY_NOT_VISIBLE-Geometry fields
          will not be included as fields
          for analysis.
      visible_time {Boolean}:
          Specifies whether the fields used to indicate the time will be
          included (visible) as fields for analysis when the MFC file is used in
          other geoprocessing tools. When time fields are not visible, time is
          still applied to the dataset. The time visibility setting can be
          modified in the MFC.TIME_VISIBLE-Time fields will be included as
          fields for analysis. This
          is the default.TIME_NOT_VISIBLE-Time fields will not be included as
          fields for
          analysis.

        """