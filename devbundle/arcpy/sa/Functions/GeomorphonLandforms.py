# Generated documentation for module arcpy.sa.Functions


class GeomorphonLandforms(object):
    """
    Calculates the geomorphon pattern of each cell of an input surface raster and classifies calculated geomorphons into common landform types.
    """

    @property
    def description(self) -> str:
        return """

        GeomorphonLandforms_sa(in_surface_raster, {out_geomorphons_raster}, {angle_threshold}, {distance_units}, {search_distance}, {skip_distance}, {z_unit})

        Calculates the geomorphon pattern of each cell of an input surface
        raster and classifies calculated geomorphons into common landform
        types.

     INPUTS:
      in_surface_raster (Composite Geodataset):
          The input surface raster.
      angle_threshold {Double}:
          The angle threshold (in degrees) below which the target cell will be
          classified as flat.The default value is 1 degree. Specifying a larger
          value than the
          default is recommended for low resolution DEMs.
      distance_units {String}:
          Specifies the distance unit that will be used for
          theandparameters. Search distanceSkip distance        Distance
          will be measured in the specified unit or number of
          cells. The default is. CellsSpecifies the distance unit that
          will be used for the search_distance
          and skip_distance parameters.Distance will be measured in the
          specified unit or number of cells.
          The default is CELLS.CELLS-The distance unit will be cells.METERS-The
          distance unit will be
          meters.CENTIMETERS-The distance unit will be
          centimeters.KILOMETERS-The distance unit will be kilometers.INCHES-The
          distance unit will be inches.FEET-The distance unit will be
          feet.YARDS-The distance unit will be yards.MILES-The distance unit
          will be miles.
      search_distance {Double}:
          The distance away from the target cell that defines the radius of the
          area that will be used to identify the geomorphon pattern.The default
          value is 10. Use a search distance value that matches the
          type and size of the landforms that you want to classify.
      skip_distance {Double}:
          The distance away from the target cell where the analysis area starts.
          Neighboring cells that fall within this distance will be skipped and
          won't contribute to identification of the geomorphon pattern.The
          classification of each individual cell is determined by assessing
          the neighboring cells within the skip distance from the target cell
          center.
      z_unit {String}:
          Specifies the linear unit that will be used for vertical z-values.It
          is defined by a vertical coordinate system if it exists. If a
          vertical coordinate system does not exist, define the z-unit using the
          unit list to ensure correct geodesic computation. The default is
          meter.INCH-The linear unit will be inches.FOOT-The linear unit will be
          feet.YARD-The linear unit will be yards.MILE_US-The linear unit will
          be miles.NAUTICAL_MILE-The linear unit will be nautical
          miles.MILLIMETER-The linear unit will be millimeters.CENTIMETER-The
          linear unit will be centimeters.METER-The linear unit will be
          meters.KILOMETER-The linear unit will be kilometers.DECIMETER-The
          linear unit will be decimeters.

     OUTPUTS:
      out_landforms_raster (Raster Dataset):
          The output classified landforms raster.The output is of integer
          type.Each value corresponds to a specific landform type: Flat-cell
          value 1,
          Peak-cell value 2, Ridge-cell value 3, Shoulder-cell value 4,
          Spur-cell value 5, Slope-cell value 6, Hollow-cell value 7,
          Footslope-cell value 8, Valley-cell value 9, Pit-cell value 10.
      out_geomorphons_raster {Raster Dataset}:
          Each geomorphon pattern will be assigned a unique identifier, which is
          stored for each cell in the output geomorphons raster.The output is of
          integer type.

        """