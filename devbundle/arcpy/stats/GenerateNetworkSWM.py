# Generated documentation for module arcpy.stats


class GenerateNetworkSWM(object):
    """
    Constructs a spatial weights matrix file (.swm) using a network dataset, defining spatial relationships in terms of the underlying network structure.
    """

    @property
    def description(self) -> str:
        return """

        GenerateNetworkSWM_stats(Input_Feature_Class, Unique_ID_Field, Output_Spatial_Weights_Matrix_File, Input_Network_Data_Source, Travel_Mode, {Impedance_Distance_Cutoff}, {Impedance_Temporal_Cutoff}, {Impedance_Cost_Cutoff}, {Maximum_Number_of_Neighbors}, {Time_of_Day}, {Time_Zone}, {Barriers}, {Search_Tolerance}, {Conceptualization_of_Spatial_Relationships}, {Exponent}, {Row_Standardization})

        Constructs a spatial weights matrix file (.swm) using a network
        dataset, defining spatial relationships in terms of the underlying
        network structure.

     INPUTS:
      Input_Feature_Class (Feature Class):
          The point feature class representing locations on the network. For
          each feature, neighbors and weights are calculated and stored in the
          output spatial weights matrix file.
      Unique_ID_Field (Field):
          An integer field containing a unique value for each feature in
          the input feature class. If you don't have a field with unique ID
          values, you can create one by adding an integer field to your feature
          class table and calculating the field values to equal theorfield.
          FIDOBJECTID
      Input_Network_Data_Source (Network Data Source):
          The network dataset used to find neighbors of each input feature.
          Network datasets usually represent street networks but can also
          represent other kinds of transportation networks such as railroads or
          walking paths. The network dataset must include at least one attribute
          related to distance, travel time, or cost.
      Travel_Mode (String):
          The mode of transportation for the analysis. A travel mode defines how
          a pedestrian, car, truck, or other medium of transportation moves
          through the network and represents a collection of network settings,
          such as travel restrictions and U-turn policies.An arcpy.na.TravelMode
          object and a string containing the valid JSON
          representation of a travel mode can also be used as input to the
          parameter.
      Impedance_Distance_Cutoff {Linear Unit}:
          The maximum impedance distance allowed for neighbors of a feature. Any
          feature whose distance is farther than this value will not be used as
          a neighbor. By default, no distance cutoff is used.
      Impedance_Temporal_Cutoff {Time Unit}:
          The maximum impedance travel time allowed for neighbors of a feature.
          Any feature whose travel time is longer than this value will not be
          used as a neighbor. By default, no temporal cutoff is used.
      Impedance_Cost_Cutoff {Double}:
          The maximum impedance cost allowed for neighbors of a feature. Any
          feature whose cost of travel is larger than this value will not be
          used as a neighbor. By default, no cost cutoff is used.
      Maximum_Number_of_Neighbors {Long}:
          An integer reflecting the maximum number of neighbors for each
          feature. The actual number of neighbors used for each feature may be
          smaller due to impedance cutoffs.
      Time_of_Day {Date}:
          The time of day traffic conditions will be considered in the analysis.
          Traffic conditions can impact the distance that can be traveled over a
          given time. If no date or time is provided, the analysis will not
          consider the impact of traffic.Instead of using a particular date, you
          can specify a day of the week
          using the following
          dates:Today-12/30/1899Sunday-12/31/1899Monday-1/1/1900Tuesday-
          1/2/1900Wednesday-1/3/1900Thursday-1/4/1900Friday-1/5/1900Saturday-
          1/6/1900For example, to specify that travel should begin at 5:00 p.m.
          on
          Tuesday, specify the parameter value as 1/2/1900 5:00 PM.
      Time_Zone {String}:
          Specifies the time zone for the Time_of_Day
          parameter.LOCAL_TIME_AT_LOCATIONS-The time zone in which the
          Input_Feature_Class
          is located will be used. This is the default.UTC-Coordinated universal
          time (UTC) will be used.
      Barriers {Feature Layer}:
          The features that represent blocked intersections, road closures,
          accident sites, or other locations where travel is blocked along the
          network.
      Search_Tolerance {Linear Unit}:
          The maximum distance used to assign each input feature to a location
          on the network. If any of the input points do not fall exactly on a
          line of the network, they will be assigned to the closest location on
          the network for the analysis. However, if the feature is farther than
          the search tolerance value from any location on the network, it will
          not be assigned to the network and will not be included in the
          analysis.
      Conceptualization_of_Spatial_Relationships {String}:
          Specifies how weights will be defined for each
          neighbor.INVERSE-Features farther in distance, time, or cost will have
          a
          smaller weight than features nearby. The weights decrease by their
          inverse to an exponent.FIXED-All neighbors will be given equal weight.
          This is the default.
      Exponent {Double}:
          The exponent used when INVERSE option is specified for the
          Conceptualization_of_Spatial_Relationships parameter. The weights
          assigned to each neighbor are calculated by taking the inverse
          distance, time, or cost to the power of the exponent. The default
          value is 1, and the value must be between 0.01 and 4. Weights drop off
          more rapidly as the exponent increases.
      Row_Standardization {Boolean}:
          Specifies whether row standardization will be applied. Row
          standardization is recommended when the locations of the input points
          are potentially biased due to sampling design or an imposed
          aggregation scheme. It is also recommended that you standardize rows
          when weighting neighbors based on inverse distance, time, or
          cost.ROW_STANDARDIZATION-Spatial weights will be standardized by row.
          Each
          weight is divided by its row sum. This is the
          default.NO_STANDARDIZATION-No standardization of spatial weights will
          be
          applied.

     OUTPUTS:
      Output_Spatial_Weights_Matrix_File (File):
          The output network spatial weights matrix file (.swm) that will store
          the neighbors and weights for each input feature.

        """