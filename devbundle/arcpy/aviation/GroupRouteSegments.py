# Generated documentation for module arcpy.aviation


class GroupRouteSegments(object):
    """
    Derives additional cumulative information such as the total distance of a route or route portion from individual segments to prepare data for charting.
    """

    @property
    def description(self) -> str:
        return """

        GroupRouteSegments_aviation(target_atsroute_features, target_enroute_table, target_routeportion_table, in_association_table)

        Derives additional cumulative information such as the total distance
        of a route or route portion from individual segments to prepare data
        for charting.

     INPUTS:
      target_atsroute_features (Feature Layer):
          The input feature class for the ATSRoute feature class that
          contains polylines. Theand theattributes will be updated.
          Enrouteinformation_IdRoutePortion_Id
      target_enroute_table (Table View):
          The table that will be updated to contain entries for the en
          routes identified during processing. Theattribute is set to the total
          length of the en route's segments. Distance_val
          Theattribute is updated and kept up to date on new and
          existing en routes. Distance_val
      target_routeportion_table (Table View):
          The table that will be updated to contain entries for the
          route portions identified during processing. Theattribute is set to
          the total length of the route portions' segments. The route
          portions'andattributes will also be updated to refer to the start and
          end point of a route portion.
          Distance_valStartPoint_IdEndPoint_Id
      in_association_table (Table View):
          The association table, DesigPoint_NavaidAssoc, that contains
          the relationships between designated points and NAVAID systems. The
          ATSRoute feature class's start and end designated point'sfield will
          reference entries in this table. This table indicates whether a point
          is collocated with a NAVAID and helps determine the grouping of route
          segments. GFID

        """