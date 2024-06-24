# Generated documentation for module arcpy.defense


class GenerateReferenceSystemGRGFromArea(object):
    """
    Creates Gridded Reference Graphics (GRG) based on Military Grid Reference System (MGRS) or United States National Grid (USNG) reference grids.
    """

    @property
    def description(self) -> str:
        return """

        GenerateReferenceSystemGRGFromArea_defense(in_features, output_feature_class, grid_reference_system, grid_square_size, {large_grid_handling})

        Creates Gridded Reference Graphics (GRG) based on Military Grid
        Reference System (MGRS) or United States National Grid (USNG)
        reference grids.

     INPUTS:
      in_features (Feature Set):
          The input polygon feature on which the GRG will be based.
      grid_reference_system (String):
          Specifies the reference system the GRG will use.MGRS-Military Grid
          Reference System will be used. This is the
          default.USNG-United States National Grid will be used.
      grid_square_size (String):
          Specifies the grid square size that will be used for the cells in the
          GRG.GRID_ZONE_DESIGNATOR-The size of the grid cells will be a Grid
          Zone.
          This is the default.100000M_GRID-The size of the grid cells will be
          100,000-meter grid
          squares.10000M_GRID-The size of the grid cells will be 10,000-meter
          grid
          squares.1000M_GRID-The size of the grid cells will be 1,000-meter grid
          squares.100M_GRID-The size of the grid cells will be 100-meter grid
          squares.50M_GRID-The size of the grid cells will be 50-meter grid
          squares.25M_GRID-The size of the grid cells will be 25-meter grid
          squares.10M_GRID-The size of the grid cells will be 10-meter grid
          squares.
      large_grid_handling {String}:
          Specifies how large input areas that may contain many features will be
          handled.NO_LARGE_GRIDS-Processing will stop when 2000 features are
          created.
          This is the default.ALLOW_LARGE_GRIDS-Large grids are supported.

     OUTPUTS:
      output_feature_class (Feature Class):
          The output polygon feature class containing the GRG.

        """