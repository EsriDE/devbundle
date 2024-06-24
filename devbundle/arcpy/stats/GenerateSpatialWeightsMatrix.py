# Generated documentation for module arcpy.stats


class GenerateSpatialWeightsMatrix(object):
    """
    Generates a spatial weights matrix file (.swm) to represent the spatial relationships among features in a dataset.
    """

    @property
    def description(self) -> str:
        return """

        GenerateSpatialWeightsMatrix_stats(Input_Feature_Class, Unique_ID_Field, Output_Spatial_Weights_Matrix_File, Conceptualization_of_Spatial_Relationships, {Distance_Method}, {Exponent}, {Threshold_Distance}, {Number_of_Neighbors}, {Row_Standardization}, {Input_Table}, {Date_Time_Field}, {Date_Time_Interval_Type}, {Date_Time_Interval_Value}, {Use_Z_values})

        Generates a spatial weights matrix file (.swm) to represent the
        spatial relationships among features in a dataset.

     INPUTS:
      Input_Feature_Class (Feature Class):
          The feature class for which spatial relationships of features will be
          assessed.
      Unique_ID_Field (Field):
          An integer field containing a different value for every
          feature in the input feature class. If you don't have a Unique ID
          field, you can create one by adding an integer field to your feature
          class table and calculating the field values to equal theorfield.
          FIDOBJECTID
      Conceptualization_of_Spatial_Relationships (String):
          Specifies how spatial relationships among features will be
          conceptualized.INVERSE_DISTANCE-The impact of one feature on another
          feature will
          decrease with distance.FIXED_DISTANCE-Everything within a specified
          critical distance of each
          feature will be included in the analysis. Everything outside the
          critical distance will be excluded.K_NEAREST_NEIGHBORS-The closest k
          features will be included in the
          analysis; k is a specified numeric
          parameter.CONTIGUITY_EDGES_ONLY-Polygon features that share a boundary
          will be
          neighbors.CONTIGUITY_EDGES_CORNERS-Polygon features that share a
          boundary or
          share a node will be neighbors.DELAUNAY_TRIANGULATION-A mesh of
          nonoverlapping triangles will be
          created from feature centroids, and features associated with triangle
          nodes that share edges will be neighbors.SPACE_TIME_WINDOW-Features
          within a specified critical distance and
          specified time interval of each other will be
          neighbors.CONVERT_TABLE-Spatial relationships will be defined in a
          table.
      Distance_Method {String}:
          Specifies how distances will be calculated from each feature to
          neighboring features.EUCLIDEAN-The straight-line distance between two
          points (as the crow
          flies) will be calculated. This is the default.MANHATTAN-The distance
          between two points measured along axes at right
          angles (city block) will be calculated by summing the (absolute)
          difference between the x- and y-coordinates.
      Exponent {Double}:
          The value for inverse distance calculation. A typical value is 1 or 2.
      Threshold_Distance {Double}:
          The cutoff distance for the Conceptualization_of_Spatial_Relationships
          parameter's INVERSE_DISTANCE and FIXED_DISTANCE options. Enter this
          value using the units specified in the environment output coordinate
          system. This defines the size of the space window for the
          SPACE_TIME_WINDOW option.When this parameter is left blank, a default
          threshold value is
          computed based on the output feature class extent and the number of
          features. For the inverse distance conceptualization of spatial
          relationships, a value of zero indicates that no threshold distance
          will be applied and all features will be neighbors of every other
          feature.
      Number_of_Neighbors {Long}:
          An integer reflecting either the minimum or the exact number of
          neighbors. When the Conceptualization_of_Spatial_Relationships
          parameter is set to K_NEAREST_NEIGHBORS, each feature will have
          exactly this specified number of neighbors. For the INVERSE_DISTANCE
          or FIXED_DISTANCE option, each feature will have at least this many
          neighbors (the threshold distance will be temporarily extended to
          ensure this many neighbors, if necessary). When the
          CONTIGUITY_EDGES_ONLY or CONTIGUITY_EDGES_CORNERS option is chosen,
          each polygon will be assigned this minimum number of neighbors. For
          polygons with fewer than this number of contiguous neighbors,
          additional neighbors will be based on feature centroid proximity.
      Row_Standardization {Boolean}:
          Specifies whether spatial weights will be standardized by row. Row
          standardization is recommended whenever feature distribution is
          potentially biased due to sampling design or to an imposed aggregation
          scheme.ROW_STANDARDIZATION-Spatial weights will be standardized by
          row. Each
          weight is divided by its row sum. This is the
          default.NO_STANDARDIZATION-No standardization of spatial weights will
          be
          applied.
      Input_Table {Table}:
          A table containing numeric weights relating every feature to
          every other feature in the input feature class. Required fields for
          the table are theparameter value,(neighbor ID), and. Unique ID
          FieldNIDWEIGHT
      Date_Time_Field {Field}:
          A date field with a time stamp for each feature.
      Date_Time_Interval_Type {String}:
          Specifies the units that will be used for measuring time.SECONDS-The
          unit will be seconds.MINUTES-The unit will be
          minutes.HOURS-The unit will be hours.DAYS-The unit will be
          days.WEEKS-The unit will be weeks.MONTHS-The unit will be 30
          days.YEARS-The unit will be years.
      Date_Time_Interval_Value {Long}:
          An integer reflecting the number of time units comprising the time
          window.For example, if you choose HOURS for the
          Date_Time_Interval_Type
          parameter and specify 3 for the Date_Time_Interval_Value parameter,
          the time window will be 3 hours. Features within the specified space
          window and within the specified time window will be neighbors.
      Use_Z_values {Boolean}:
          Specifies whether z-coordinates will be used in the construction of
          the spatial weights matrix if the input features are
          z-enabled.USE_Z_VALUES-Z-values will be used in the construction of
          the spatial
          weights matrix.DO_NOT_USE_Z_VALUES-Z-values will not be used. They
          will be ignored
          and only x- and y-coordinates will be considered in the construction
          of the spatial weights matrix. This is the default.

     OUTPUTS:
      Output_Spatial_Weights_Matrix_File (File):
          The full path for the output spatial weights matrix file (.swm).

        """