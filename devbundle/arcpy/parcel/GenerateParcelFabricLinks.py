# Generated documentation for module arcpy.parcel


class GenerateParcelFabricLinks(object):
    """
    Generates displacement links for parcel fabric points that have changed locations in a specified time period.
    """

    @property
    def description(self) -> str:
        return """

        GenerateParcelFabricLinks_parcel(target_parcel_fabric, out_links_feature_class, out_anchor_points_feature_class, from_date, {to_date}, {min_link_length}, {extent})

        Generates displacement links for parcel fabric points that have
        changed locations in a specified time period.

     INPUTS:
      target_parcel_fabric (Parcel Layer):
          The parcel fabric that will be used to generate links. The parcel
          fabric must be published as a feature service and the default version
          is used to generate links.
      from_date (Date):
          The date from which to search the parcel fabric for points that have
          changed locations. Links and anchor points will be only be generated
          for points on or after this date.
      to_date {Date}:
          The end date of the time period in which to search the parcel
          fabric for points that have changed locations. Links and anchor points
          will only be generated for points on or before this date. If no To
          date is specified, links and anchor points will be generated for all
          points on or after the specified. If theis specified at a future date,
          links will be generated in the time period between theand the current
          date and time. From DateTo DateFrom Date
      min_link_length {Linear Unit}:
          The minimum length of the generated links. If the link length between
          the current points and their original locations is smaller than the
          specified value, anchor points are created for the original locations
          of the points.
      extent {Extent}:
          The extent of the dataset to be processed. Only features that fall
          within the specified extent will be processed.MAXOF-The maximum extent
          of all inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.

     OUTPUTS:
      out_links_feature_class (Feature Class):
          The output line feature class that will store the generated links.
      out_anchor_points_feature_class (Feature Class):
          The output point feature class that will store the anchor points.

        """