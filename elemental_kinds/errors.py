from elemental_core import ElementalError


class AttributeKindError(ElementalError):
    """
    Base class for Errors relating to Attribute Kinds.
    """
    pass


class AttributeKindValueProcessingError(AttributeKindError):
    pass


class AttributeKindValueValidationError(AttributeKindError):
    pass
