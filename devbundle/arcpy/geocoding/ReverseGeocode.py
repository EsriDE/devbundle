# Generated documentation for module arcpy.geocoding


class ReverseGeocode(object):
    """
    Creates addresses from point locations in a feature class. The reverse geocoding process searches for the nearest address, place, or intersection for the point location based on optimized distance values for locators created with the Create Locator tool.
    """

    @property
    def description(self) -> str:
        return """

        ReverseGeocode_geocoding(in_features, in_address_locator, out_feature_class, {address_type}, {search_distance}, {feature_type;feature_type...}, {location_type})

        Creates addresses from point locations in a feature class. The reverse
        geocoding process searches for the nearest address, place, or
        intersection for the point location based on optimized distance values
        for locators created with the Create Locator tool.

     INPUTS:
      in_features (Feature Layer):
          A point feature class or layer from which matching places or addresses
          will be returned based on the features' point location.
      in_address_locator (Address Locator):
          The locator that will be used to reverse geocode the input feature
          class or layer.
      address_type {String}:
          Output Address Type
      search_distance {Linear Unit}:
          Search Distance
      feature_type {String}:
          Specifies the possible match types that will be returned. A single
          value or multiple values can be selected. If a single value is
          selected, the search tolerance for the input feature type is 500
          meters. If multiple values are included, the default search distances
          specified in the feature type hierarchy table will be applied. See
          Feature types for details about the feature_type parameter for reverse
          geocoding.This parameter is not supported for all
          locators.SUBADDRESS-The match will be limited to a street address
          based on
          points that represent house and building subaddress locations. This
          option requires a locator created in ArcGIS Pro 2.8 or later and
          ArcGIS Enterprise 10.9 or later if published as a
          service.POINT_ADDRESS-The match will be limited to a street address
          based on
          points that represent house and building locations.PARCEL-The match
          will be limited to a plot of land that is considered
          real property and can include one or more homes or other structures.
          This match type typically has an address and a parcel identification
          number assigned to it.STREET_ADDRESS-The match will be limited to a
          street address that
          differs from POINT_ADDRESS because the house number is interpolated
          from a range of numbers. STREET_ADDRESS matches include the house
          number range for the matching street segment rather than the
          interpolated house number value.STREET_INTERSECTION-The match will be
          limited to a street address
          consisting of a street intersection along with city and optional state
          and postal code information. This is derived from STREET_ADDRESS
          reference data, for example, Redlands Blvd & New York St, Redlands,
          CA, 92373.STREET_NAME-The match will be limited to a street address
          similar to
          STREET_ADDRESS but without house numbers along with administrative
          divisions and optional postal code, for example, W Olive Ave,
          Redlands, CA, 92373.LOCALITY-The match will be limited to a place-name
          representing a
          populated place.POSTAL-The match will be limited to a postal code.
          Reference data is
          postal code points, for example, 90210 USA.POINT_OF_INTEREST-The match
          will be limited to a point of interest.
          Reference data consists of administrative division place-names,
          businesses, landmarks, and geographic features, for example,
          Starbucks.DISTANCE_MARKER-The match will be limited to a street
          address that
          represents the linear distance along a street, typically in kilometers
          or miles, from a designated origin location, for example, Mile 25 I-5
          N, San Diego, CA.
      location_type {String}:
          Specifies the preferred output geometry that will be returned for
          POINT_ADDRESS matches. The options for this parameter are
          ROUTING_LOCATION, which is the side of street location that can be
          used for routing and ADDRESS_LOCATION, which is the location that
          represents the rooftop, parcel centroid for the address, or front
          door. If the preferred location does not exist in the data, the
          default location of ROUTING_LOCATION will be returned. For geocode
          results with Addr_type=PointAddress, the x,y attribute values describe
          the coordinates of the address along the street, and the DisplayX and
          DisplayY values describe the rooftop or building centroid coordinates.
          See the REST API web help for details about the locationType parameter
          for reverseGeocode.This parameter is not supported for all
          locators.ADDRESS_LOCATION-Geometry for geocode results that represent
          an
          address location such as a rooftop, building centroid, or front door
          will be returned.ROUTING_LOCATION-Geometry for geocode results that
          represent a
          location close to the side of the street that can be used for vehicle
          routing, will be returned. This is the default.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class.Saving the output to shapefile format is not
          supported due to
          shapefile limitations.

        """