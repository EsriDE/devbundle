# Generated documentation for module arcpy.management


class CreateDomain(object):
    """
    Creates an attribute domain in the specified workspace.
    """

    @property
    def description(self) -> str:
        return """

        CreateDomain_management(in_workspace, domain_name, {domain_description}, {field_type}, {domain_type}, {split_policy}, {merge_policy})

        Creates an attribute domain in the specified workspace.

     INPUTS:
      in_workspace (Workspace):
          The geodatabase that will contain the new domain.
      domain_name (String):
          The name of the domain that will be created.
      domain_description {String}:
          The description of the domain that will be created.
      field_type {String}:
          Specifies the type of attribute domain that will be created. Attribute
          domains are rules that describe the accepted values of a field type.
          Specify a field type that matches the data type of the field to which
          the attribute domain will be assigned.SHORT-The field type will be
          short. Short fields support whole numbers
          between -32,768 and 32,767.LONG-The field type will be long. Long
          fields support whole numbers
          between -2,147,483,648 and 2,147,483,647. BIGINTEGER-The field
          type will be big integer. Big integer
          fields support whole numbers between -(2) and 2. 5353FLOAT-The
          field type will be float. Float fields support fractional
          numbers between -3.4E38 and 1.2E38.DOUBLE-The field type will be
          double. Double fields support fractional
          numbers between -2.2E308 and 1.8E308.TEXT-The field type will be text.
          Text fields support a string of
          characters.DATE-The field type will be date. Date fields support date
          and time
          values.DATEONLY-The field type will be date only. Date only fields
          support
          date values with no time values.TIMEONLY-The field type will be time
          only. Time only fields support
          time values with no date values.
      domain_type {String}:
          Specifies the domain type that will be created.CODED-A coded type
          domain will be created that contains a valid set of
          values for an attribute. This is the default. For example, a coded
          value domain can specify valid pipe material values such as CL-cast
          iron pipe, DL-ductile iron pipe, or ACP-asbestos concrete pipe.RANGE-A
          range type domain will be created that contains a valid range
          of values for a numeric attribute. For example, if distribution water
          mains have a pressure between 50 and 75 psi, a range domain specifies
          these minimum and maximum values.
      split_policy {String}:
          Specifies the split policy that will be used for the created domain.
          The behavior of an attribute's values when a feature that is split is
          controlled by its split policy.DEFAULT-The attributes of the two
          resulting features will use the
          default value of the attribute of the given feature class or
          subtype.DUPLICATE-The attribute of the two resulting features will use
          a copy
          of the original object's attribute value.GEOMETRY_RATIO-The attributes
          of resulting features will be a ratio of
          the original feature's value. The ratio is based on the proportion
          into which the original geometry is divided. If the geometry is
          divided equally, each new feature's attribute gets one-half the value
          of the original object's attribute. The geometry ratio policy only
          applies to range domains.
      merge_policy {String}:
          Specifies the merge policy that will be used for the created domain.
          When two features are merged into a single feature, merge policies
          control attribute values in the new feature.DEFAULT-The attribute of
          the resulting feature will use the default
          value of the attribute of the given feature class or subtype. This is
          the only merge policy that applies to nonnumeric fields and coded
          value domains.SUM_VALUES-The attribute of the resulting feature will
          use the sum of
          the values from the original feature's attribute. The sum values
          policy only applies to range domains.AREA_WEIGHTED-The attribute of
          the resulting feature will be the
          weighted average of the attribute values of the original features.
          This average is based on the original feature's geometry. The area
          weighted policy only applies to range domains.

        """