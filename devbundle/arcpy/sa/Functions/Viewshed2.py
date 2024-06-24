# Generated documentation for module arcpy.sa.Functions


class Viewshed2(object):
    """
    Determines the raster surface locations visible to a set of observer features using geodesic methods.
    """

    @property
    def description(self) -> str:
        return """

        Viewshed2_sa(in_raster, in_observer_features, {out_agl_raster}, {analysis_type}, {vertical_error}, {out_observer_region_relationship_table}, {refractivity_coefficient}, {surface_offset}, {observer_elevation}, {observer_offset}, {inner_radius}, {inner_radius_is_3d}, {outer_radius}, {outer_radius_is_3d}, {horizontal_start_angle}, {horizontal_end_angle}, {vertical_upper_angle}, {vertical_lower_angle}, {analysis_method}, {analysis_target_device})

        Determines the raster surface locations visible to a set of observer
        features using geodesic methods.

     INPUTS:
      in_raster (Composite Geodataset):
          The input surface raster. It can be an integer or a floating-point
          raster.The input raster is transformed into a 3D geocentric coordinate
          system
          during the visibility calculation. NoData cells on the input raster do
          not block the visibility determination.
      in_observer_features (Composite Geodataset):
          The input feature class that identifies the observer locations. It can
          be point, multipoint, or polyline features.The input feature class is
          transformed into a 3D geocentric coordinate
          system during the visibility calculation. Observers outside of the
          extent of the surface raster or located on NoData cells will be
          ignored in the calculation.
      analysis_type {String}:
          Specifies the type of visibility analysis that will be performed,
          either determining how visible each cell is to the observers or
          identifying the observers that are visible for each surface
          location.FREQUENCY-The number of times that each cell location in the
          input
          surface raster can be seen by the input observation locations (as
          points or as vertices for polyline observer features) will be recorded
          in the output. This is the default.OBSERVERS-The observer points that
          are visible from each raster
          surface location will be identified in the output. The maximum number
          of input observer locations allowed for this analysis type is 32.
      vertical_error {Linear Unit}:
          The amount of uncertainty (the root mean square [RMS] error) in the
          surface elevation values. It is a floating-point value representing
          the expected error of the input elevation values. When this parameter
          is assigned a value greater than 0, the output visibility raster will
          be floating point. In this case, each cell value on the output
          visibility raster represents the sum of probabilities that the cell is
          visible to any of the observers.When the analysis_type parameter value
          is OBSERVERS or the
          analysis_method parameter value is PERIMETER_SIGHTLINES, this
          parameter is disabled.
      refractivity_coefficient {Double}:
          The coefficient of the refraction of visible light in air.The default
          value is 0.13.
      surface_offset {Linear Unit / Field}:
          A vertical distance to be added to the z-value of each cell as it is
          considered for visibility. It must be a positive integer or floating-
          point value.You can select a field in the input observers dataset, or
          you can
          specify a numerical value.For example, if the object to be observed is
          a vehicle, specify the
          height of the vehicle here.When this parameter is set to a value, the
          value will be used by all
          the observers. To specify different values for each observer, set this
          parameter to a field in the input observer features dataset.The
          default value is 0.
      observer_elevation {Linear Unit / Field}:
          The surface elevations of the observer points or vertices.You can
          select a field in the input observers dataset, or you can
          specify a numerical value.When this parameter is not specified, the
          observer elevation will be
          obtained from the surface raster using bilinear interpolation. If this
          parameter is set to a value, the value will be applied to all the
          observers. To specify different values for each observer, set this
          parameter to a field in the input observer features dataset.
      observer_offset {Linear Unit / Field}:
          A vertical distance to be added to the observer elevation. It must be
          a positive integer or floating-point value.You can select a field in
          the input observers dataset, or you can
          specify a numerical value.For example, if an observer is looking from
          a tower, specify the
          height of the tower here.When this parameter is set to a value, the
          value will be applied to
          all the observers. To specify different values for each observer, set
          this parameter to a field in the input observer features dataset.The
          default value is 1 meter.
      inner_radius {Linear Unit / Field}:
          The start distance from which visibility is determined. Cells closer
          than this distance are not visible in the output but can still block
          visibility of the cells between inner radius and outer radius.You can
          select a field in the input observers dataset, or you can
          specify a numerical value.When this parameter is set to a value, the
          value will be applied to
          all the observers. To specify different values for each observer, set
          this parameter to a field in the input observer features dataset.The
          default value is 0.
      inner_radius_is_3d {Boolean}:
          Specifies the type of distance that will be used for the inner radius
          parameter.GROUND-The inner radius will be interpreted as a 2D
          distance. This is
          the default.3D-The inner radius will be interpreted as a 3D distance.
      outer_radius {Linear Unit / Field}:
          The maximum distance from which visibility is determined. Cells beyond
          this distance are excluded from the analysis.You can select a field in
          the input observers dataset, or you can
          specify a numerical value.When this parameter is set to a value, the
          value will be applied to
          all the observers. To specify different values for each observer, set
          this parameter to a field in the input observer features dataset.
      outer_radius_is_3d {Boolean}:
          Specifies the type of distance that will be used for the outer radius
          parameter.GROUND-The outer radius will be interpreted as a 2D
          distance. This is
          the default.3D-The outer radius will be interpreted as a 3D distance.
      horizontal_start_angle {Double / Field}:
          The start angle of the horizontal scan range. Provide the value in
          degrees from 0 to 360 with 0 oriented to north. The value can be
          integer or floating point. The default value is 0.You can select a
          field in the input observers dataset, or you can
          specify a numerical value.When this parameter is set to a value, the
          value will be applied to
          all the observers. To specify different values for each observer, set
          this parameter to a field in the input observer features dataset.
      horizontal_end_angle {Double / Field}:
          The end angle of the horizontal scan range. Provide the value in
          degrees from 0 to 360 with 0 oriented to north. The value can be
          integer or floating point. The default value is 360.You can select a
          field in the input observers dataset, or you can
          specify a numerical value.When this parameter is set to a value, the
          value will be applied to
          all the observers. To specify different values for each observer, set
          this parameter to a field in the input observer features dataset.
      vertical_upper_angle {Double / Field}:
          The upper vertical angle limit of the scan relative to the horizontal
          plane. Provide the value in degrees from above -90 up to and including
          90. The value can be integer or floating point. The default value is
          90 (straight up). This parameter value must be greater than
          theparameter value.
          Vertical lower angleYou can select a field in the input observers
          dataset, or you can
          specify a numerical value.When this parameter is set to a value, the
          value will be applied to
          all the observers. To specify different values for each observer, set
          this parameter to a field in the input observer features dataset.The
          default value is 90 (straight up).
      vertical_lower_angle {Double / Field}:
          The lower vertical angle limit of the scan relative to the horizontal
          plane. Provide the value in degrees from -90 up to but not including
          90. The value can be integer or floating point. The default value is
          -90 (straight down). This parameter value must be less than
          theparameter value.
          Vertical upper angleYou can select a field in the input observers
          dataset, or you can
          specify a numerical value.When this parameter is set to a value, the
          value will be applied to
          all the observers. To specify different values for each observer, set
          this parameter to a field in the input observer features dataset.The
          default value is -90 (straight down).
      analysis_method {String}:
          Specifies the method that will be used to calculate visibility. This
          parameter allows you to decide on performance level.ALL_SIGHTLINES-A
          sightline will be run to every cell on the raster to
          establish visible areas, which may decrease performance depending on
          the number of sightlines. This is the default
          method.PERIMETER_SIGHTLINES-Sightlines will only be run to the cells
          on the
          perimeter of the visible areas to establish visibility areas, which
          can increase performance because fewer sightlines are run in the
          calculation.
      analysis_target_device {String}:
          Specifies the device that will be used to perform the
          calculation.GPU_THEN_CPU-If a compatible GPU is found, it will be used
          to perform
          the calculation. Otherwise, the CPU will be used. This is the
          default.CPU_ONLY-The calculation will only be performed on the
          CPU.GPU_ONLY-The calculation will only be performed on the GPU.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.For the FREQUENCY analysis type, when the vertical
          error parameter is
          0 or not specified, the output raster records the number of times that
          each cell location in the input surface raster can be seen by the
          input observation points. When the vertical error parameter is greater
          than 0, each cell on the output raster records the sum of
          probabilities that the cell is visible to any of the observers. For
          the OBSERVERS analysis type, the output raster records the unique
          region IDs for the visible areas, which can be related back to the
          observer features through the output observer-region relationship
          table.
      out_agl_raster {Raster Dataset}:
          The output above ground level (AGL) raster.The AGL result is a raster
          in which each cell value is the minimum
          height that must be added to a cell that is not visible to make it
          visible by at least one observer. Cells that are already visible will
          be assigned 0 in this output raster.When the vertical error parameter
          is 0, the output AGL raster will be
          a one-band raster. When the vertical error is greater than 0, to
          account for the random effects from the input raster, the output AGL
          raster will be created as a three-band raster. The first band
          represents the mean AGL values, the second band represents the minimum
          AGL values, and the third band represents the maximum AGL values.
      out_observer_region_relationship_table {Table}:
          The output table for identifying the regions that are visible to each
          observer. This table can be related to the input observer feature
          class and the output visibility raster for identifying the regions
          visible to given observers.This output is only created when the
          analysis type is OBSERVERS.

        """