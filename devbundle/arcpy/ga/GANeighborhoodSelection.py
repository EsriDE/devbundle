# Generated documentation for module arcpy.ga


class GANeighborhoodSelection(object):
    """
    Creates a layer of points based on a user-defined neighborhood.
    """

    @property
    def description(self) -> str:
        return """

        GANeighborhoodSelection_ga(in_dataset, out_layer, point_coord, neighbors_max, neighbors_min, minor_semiaxis, major_semiaxis, angle, {shape_type})

        Creates a layer of points based on a user-defined neighborhood.

     INPUTS:
      in_dataset (Feature Layer):
          The points that will be used to create a neighborhood selection.
      point_coord (Point):
          The neighborhood center's x,y-coordinate.
      neighbors_max (Long):
          The number of points that will be used in each sector. If a sector has
          the required number of points, all points in that sector will be used.
      neighbors_min (Long):
          The minimum number of points that will be used in each sector. If the
          minimum number of required points are not available in any given
          sector, the nearest available point outside the sector will be
          selected.
      minor_semiaxis (Double):
          The size of the minor semiaxis of the search neighborhood.
      major_semiaxis (Double):
          The size of the major semiaxis of the search neighborhood.
      angle (Double):
          The angle of rotation of the neighborhood axis.
      shape_type {String}:
          Species the geometry of the neighborhood.ONE_SECTOR-The neighborhood
          will be a single ellipse.FOUR_SECTORS-The
          neighborhood will be an ellipse divided into four
          sectors.FOUR_SECTORS_SHIFTED-The neighborhood will be an ellipse
          divided into
          four sectors and shifted 45 degrees.EIGHT_SECTORS-The neighborhood
          will be an ellipse divided into eight
          sectors

     OUTPUTS:
      out_layer (Feature Layer):
          An output layer with the neighborhood selection.

        """