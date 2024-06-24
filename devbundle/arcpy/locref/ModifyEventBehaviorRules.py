# Generated documentation for module arcpy.locref


class ModifyEventBehaviorRules(object):
    """
    Modifies event behavior rules for the registered event layer or feature class.
    """

    @property
    def description(self) -> str:
        return """

        ModifyEventBehaviorRules_locref(in_feature_class, {calibrate_rule}, {retire_rule}, {extend_rule}, {reassign_rule}, {realign_rule}, {reverse_rule}, {carto_realign_rule})

        Modifies event behavior rules for the registered event layer or
        feature class.

     INPUTS:
      in_feature_class (Feature Layer):
          The event feature class.
      calibrate_rule {String}:
          Specifies the event behavior rule that will be defined for the
          calibrate activity.STAY_PUT-The geographic location of the event will
          be preserved;
          measures may change. This is the default.RETIRE-Both measure and
          geographic location will be preserved; the
          event will be retired.MOVE-The measures of the event will be
          preserved; the geographic
          location may change.
      retire_rule {String}:
          Specifies the event behavior rule that will be defined for the retire
          activity.STAY_PUT-The geographic location of the event will be
          preserved;
          measures may change. This is the default.RETIRE-Both measure and
          geographic location will be preserved; the
          event will be retired.MOVE-The measures of the event will be
          preserved; the geographic
          location may change.SNAP-The location of an event will be preserved by
          snapping the event
          to a reassigned or abandoned route; measures may change.
      extend_rule {String}:
          Specifies the event behavior rule that will be defined for the extend
          activity.STAY_PUT-The geographic location of the event will be
          preserved;
          measures may change. This is the default.RETIRE-Both measure and
          geographic location will be preserved; the
          event will be retired.MOVE-The measures of the event will be
          preserved; the geographic
          location may change.COVER-The geometric location and measure of a line
          event will be
          modified to include a new or newly modified section.
      reassign_rule {String}:
          Specifies the event behavior rule that will be defined for the
          reassign activity.STAY_PUT-The geographic location of the event will
          be preserved;
          measures may change. This is the default.RETIRE-Both measure and
          geographic location will be preserved; the
          event will be retired.MOVE-The measures of the event will be
          preserved; the geographic
          location may change.SNAP-The geographic location of an event will be
          preserved by snapping
          the event to a concurrent route; measures may change.
      realign_rule {String}:
          Specifies the event behavior rule that will be defined for the realign
          activity.STAY_PUT-The geographic location of the event will be
          preserved;
          measures may change. This is the default.RETIRE-Both measure and
          geographic location will be preserved; the
          event will be retired.MOVE-The measures of the event will be
          preserved; the geographic
          location may change.SNAP-The geographic location of an event will be
          preserved by snapping
          the event to a concurrent route; measures may change.COVER-The
          geometric location and measure of a line event will be
          modified to include a new or newly modified section.
      reverse_rule {String}:
          Specifies the event behavior rule that will be defined for the reverse
          activity.STAY_PUT-The geographic location of the event will be
          preserved;
          measures may change. This is the default.RETIRE-Both measure and
          geographic location will be preserved; the
          event will be retired.MOVE-The measures of the event will be
          preserved; the geographic
          location may change.
      carto_realign_rule {String}:
          Specifies the event behavior rule that will be defined for the
          cartographic realignment activity.HONOR_ROUTE_MEASURE-The measure of
          the event will be preserved or will
          change proportionally to the route's measure change. This is the
          default.HONOR_REFERENT_LOCATION-The referent location of the event
          will be
          preserved.

        """