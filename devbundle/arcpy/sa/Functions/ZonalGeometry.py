# Generated documentation for module arcpy.sa.Functions


class ZonalGeometry(object):
    """
    Calculates the specified geometry measure (area, perimeter, thickness, or the characteristics of an ellipse) for each zone in a dataset.
    """

    @property
    def description(self) -> str:
        return """

        ZonalGeometry_sa(in_zone_data, zone_field, {geometry_type}, {cell_size})

        Calculates the specified geometry measure (area, perimeter, thickness,
        or the characteristics of an ellipse) for each zone in a dataset.

     INPUTS:
      in_zone_data (Composite Geodataset):
          The dataset that defines the zones.The zones can be defined by an
          integer raster or a feature layer.
      zone_field (Field):
          The field that contains the values that define each zone.It must be an
          integer field of the zone dataset.
      geometry_type {String}:
          Specifies the geometry type that will be calculated.AREA-The area for
          each zone will be calculated.PERIMETER-The perimeter
          for each zone will be calculated.THICKNESS-The deepest (or thickest)
          point within the zone from its
          surrounding cells will be calculated.CENTROID-The centroids of each
          zone will be calculated.
      cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output zonal geometry raster.

        """