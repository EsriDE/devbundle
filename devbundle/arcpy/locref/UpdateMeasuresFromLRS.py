# Generated documentation for module arcpy.locref


class UpdateMeasuresFromLRS(object):
    """
    Populates or updates the measures and route ID on Utility Network (UN) features such as pipes, devices, and junctions or on features in feature classes that are not UN or LRS feature classes.
    """

    @property
    def description(self) -> str:
        return """

        UpdateMeasuresFromLRS_locref(lrs_network, lrs_date, in_features, route_id_field, from_measure_field, {to_measure_field})

        Populates or updates the measures and route ID on Utility Network (UN)
        features such as pipes, devices, and junctions or on features in
        feature classes that are not UN or LRS feature classes.

     INPUTS:
      lrs_network (Feature Layer):
          The feature layer that contains the routes, route IDs, and measures.
      lrs_date (Date):
          The date used to define the temporal view of the network for
          collecting the route and measure values.
      in_features (Feature Layer):
          The layer that includes route ID and measure fields that will be
          updated based on feature geometry relative to routes in the
          lrs_network parameter.
      route_id_field (Field):
          The field in the in_features layer that contains the route ID value.
      from_measure_field (Field):
          The field in the in_features layer that contains the from measure
          value for polyline features.
      to_measure_field {Field}:
          The field in the in_features layer that contains the measure value for
          point features or the to measure value for polyline features.

        """