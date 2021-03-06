# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from state_estimator/LandmarkReading.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import state_estimator.msg

class LandmarkReading(genpy.Message):
  _md5sum = "b6297115c9296944dda00cf56fb301f4"
  _type = "state_estimator/LandmarkReading"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# The landmark for which this reading was created
state_estimator/Landmark landmark

# The range from the robot's location to the landmark above
float64 range

# The bearing of this landmark relative to the robot's orientation
float64 bearing

================================================================================
MSG: state_estimator/Landmark
# The x coordinate of this landmark
float64 x

# The y coordinate of this landmark
float64 y

"""
  __slots__ = ['landmark','range','bearing']
  _slot_types = ['state_estimator/Landmark','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       landmark,range,bearing

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LandmarkReading, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.landmark is None:
        self.landmark = state_estimator.msg.Landmark()
      if self.range is None:
        self.range = 0.
      if self.bearing is None:
        self.bearing = 0.
    else:
      self.landmark = state_estimator.msg.Landmark()
      self.range = 0.
      self.bearing = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_4d().pack(_x.landmark.x, _x.landmark.y, _x.range, _x.bearing))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.landmark is None:
        self.landmark = state_estimator.msg.Landmark()
      end = 0
      _x = self
      start = end
      end += 32
      (_x.landmark.x, _x.landmark.y, _x.range, _x.bearing,) = _get_struct_4d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_4d().pack(_x.landmark.x, _x.landmark.y, _x.range, _x.bearing))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.landmark is None:
        self.landmark = state_estimator.msg.Landmark()
      end = 0
      _x = self
      start = end
      end += 32
      (_x.landmark.x, _x.landmark.y, _x.range, _x.bearing,) = _get_struct_4d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
