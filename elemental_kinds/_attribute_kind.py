from elemental_core import ElementalBase


class AttributeKind(ElementalBase):
    """
    Base class for Attribute Kinds.
    """

    @staticmethod
    def process_value(cls, value, **params):
        pass

    @staticmethod
    def validate_value(cls, value, **params):
        pass
