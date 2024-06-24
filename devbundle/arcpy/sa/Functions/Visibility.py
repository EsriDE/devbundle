# Generated documentation for module arcpy.sa.Functions


class Visibility(object):
    """
    Determines the raster surface locations visible to a set of observer features, or identifies which observer points are visible from each raster surface location.
    """

    @property
    def description(self) -> str:
        return """

        Visibility_sa(in_raster, in_observer_features, {out_agl_raster}, {analysis_type}, {nonvisible_cell_value}, {z_factor}, {curvature_correction}, {refractivity_coefficient}, {surface_offset}, {observer_elevation}, {observer_offset}, {inner_radius}, {outer_radius}, {horizontal_start_angle}, {horizontal_end_angle}, {vertical_upper_angle}, {vertical_lower_angle})

        Determines the raster surface locations visible to a set of observer
        features, or identifies which observer points are visible from each
        raster surface location.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster.
      in_observer_features (Composite Geodataset):
          The feature class that identifies the observer locations.The input can
          be point or polyline features.
      analysis_type {String}:
          The visibility analysis type.FREQUENCY-The output records the number
          of times that each cell
          location in the input surface raster can be seen by the input
          observation locations (as points, or as vertices for polyline observer
          features). This is the default.OBSERVERS-The output identifies exactly
          which observer points are
          visible from each raster surface location.
      nonvisible_cell_value {Boolean}:
          Value assigned to non-visible cells.ZERO-0 is assigned to nonvisible
          cells. This is the
          default.NODATA-NoData is assigned to nonvisible cells.
      z_factor {Double}:
          Number of ground x,y units in one surface z unit.The z-factor adjusts
          the units of measure for the z units when they
          are different from the x,y units of the input surface. The z-values of
          the input surface are multiplied by the z-factor when calculating the
          final output surface.If the x,y units and z units are in the same
          units of measure, the
          z-factor is 1. This is the default.If the x,y units and z units are in
          different units of measure, the
          z-factor must be set to the appropriate factor, or the results will be
          incorrect. For example, if your z units are feet and your x,y units
          are meters, you would use a z-factor of 0.3048 to convert your z units
          from feet to meters (1 foot = 0.3048 meter).
      curvature_correction {Boolean}:
          Specifies whether correction for the earth's curvature will be
          applied.FLAT_EARTH-No curvature correction will be applied. This is
          the
          default.CURVED_EARTH-Curvature correction will be applied.
      refractivity_coefficient {Double}:
          The coefficient of the refraction of visible light in air.The default
          value is 0.13.
      surface_offset {String}:
          A vertical distance to be added to the z-value of each cell as it is
          considered for visibility. It must be a positive integer or floating-
          point value.You can select a field in the input observers dataset, or
          you can
          specify a numerical value. By default, a numerical fieldis used
          if it exists in the input
          observer features attribute table. You may overwrite it by specifying
          another numerical field or a value. OFFSETBIf this parameter is
          unspecified and the default field does not exist
          in the input observer features attribute table, the default value is
          0.
      observer_elevation {String}:
          The surface elevations of the observer points or vertices.You can
          select a field in the input observers dataset, or you can
          specify a numerical value. By default, a numerical fieldis used
          if it exists in the input
          observer features attribute table. You may overwrite it by specifying
          another numerical field or a value. SPOTIf this parameter is
          unspecified and the default field does not exist
          in the input observer features attribute table, it will be estimated
          through bilinear interpolation with the surface elevation values in
          the neighboring cells of the observer location.
      observer_offset {String}:
          A vertical distance to be added to the observer elevation. It must be
          a positive integer or floating-point value.You can select a field in
          the input observers dataset, or you can
          specify a numerical value. By default, a numerical fieldis used
          if it exists in the input
          observer features attribute table. You may overwrite it by specifying
          another numerical field or a value. OFFSETAIf this parameter is
          unspecified and the default field does not exist
          in the input observer features attribute table, it defaults to 1.
      inner_radius {String}:
          The start distance from which visibility is determined. Cells closer
          than this distance are not visible in the output but can still block
          visibility of the cells between inner radius and outer radius.It can
          be a positive or negative integer or floating point value. If
          it is a positive value, then it is interpreted as three-dimensional,
          line-of-sight distance. If it is a negative value, then it is
          interpreted as two-dimensional planimetric distance.You can select a
          field in the input observers dataset, or you can
          specify a numerical value. By default, a numerical fieldis used
          if it exists in the input
          observer features attribute table. You may overwrite it by specifying
          another numerical field or a value. RADIUS1If this parameter is
          unspecified and the default field does not exist
          in the input observer features attribute table, the default value is
          0.
      outer_radius {String}:
          The maximum distance from which visibility is determined. Cells beyond
          this distance are excluded from the analysis.It can be a positive or
          negative integer or floating point value. If
          it is a positive value, then it is interpreted as three-dimensional,
          line-of-sight distance. If it is a negative value, then it is
          interpreted as two-dimensional planimetric distance.You can select a
          field in the input observers dataset, or you can
          specify a numerical value. By default, a numerical fieldis used
          if it exists in the input
          observer features attribute table. You may overwrite it by specifying
          another numerical field or a value. RADIUS2If this parameter is
          unspecified and the default field does not exist
          in the input observer features attribute table, it defaults to
          infinity.
      horizontal_start_angle {String}:
          The start angle of the horizontal scan range. Provide the value in
          degrees from 0 to 360 with 0 oriented to north. The value can be
          integer or floating point. The default value is 0.You can select a
          field in the input observers dataset, or you can
          specify a numerical value. By default, a numerical fieldis used
          if it exists in the input
          observer features attribute table. You may overwrite it by specifying
          another numerical field or a value. AZIMUTH1If this parameter
          is unspecified and the default field does not exist
          in the input observer features attribute table, the default value is
          0.
      horizontal_end_angle {String}:
          The end angle of the horizontal scan range. Provide the value in
          degrees from 0 to 360 with 0 oriented to north. The value can be
          integer or floating point. The default value is 360.You can select a
          field in the input observers dataset, or you can
          specify a numerical value. By default, a numerical fieldis used
          if it exists in the input
          observer features attribute table. You may overwrite it by specifying
          another numerical field or a value. AZIMUTH2If this parameter
          is unspecified and the default field does not exist
          in the input observer features attribute table, it defaults to 360.
      vertical_upper_angle {String}:
          The upper vertical angle limit of the scan relative to the horizontal
          plane. Provide the value in degrees from above -90 up to and including
          90. The value can be integer or floating point. The default value is
          90 (straight up). This parameter value must be greater than
          theparameter value.
          Vertical lower angleYou can select a field in the input observers
          dataset, or you can
          specify a numerical value. By default, a numerical fieldis used
          if it exists in the input
          observer features attribute table. You may overwrite it by specifying
          another numerical field or a value. VERT1If this parameter is
          unspecified and the default field does not exist
          in the input observer features attribute table, it defaults to 90.
      vertical_lower_angle {String}:
          The lower vertical angle limit of the scan relative to the horizontal
          plane. Provide the value in degrees from -90 up to but not including
          90. The value can be integer or floating point. The default value is
          -90 (straight down). This parameter value must be less than
          theparameter value.
          Vertical upper angleYou can select a field in the input observers
          dataset, or you can
          specify a numerical value. By default, a numerical fieldis used
          if it exists in the input
          observer features attribute table. You may overwrite it by specifying
          another numerical field or a value. VERT2If this parameter is
          unspecified and the default field does not exist
          in the input observer features attribute table, it defaults to -90.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.The output will either record the number of times
          that each cell
          location in the input surface raster can be seen by the input
          observation locations (the frequency analysis type), or record which
          observer locations are visible from each cell in the raster surface
          (the observers type).
      out_agl_raster {Raster Dataset}:
          The output above-ground-level (AGL) raster.The AGL result is a raster
          where each cell value is the minimum height
          that must be added to an otherwise nonvisible cell to make it visible
          by at least one observer.Cells that were already visible will have a
          value of 0 in this output
          raster.

        """