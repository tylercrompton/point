import itertools
import operator

class Point(tuple):
	"""This class is intended to be a unitless Cartesian point of n dimensions where that n is a positive integer. Note that more than three dimensions are allowed. This is intended to be an immutable object. Modifying it may or may not have negative effects."""

	allowed_numeric_types = {float, int}

	def __abs__(self):
		"""This method returns a new point equidistant from the origin in the first orthant."""
		return self.__class__(map(abs, self))

	def __add__(self, other):
		"""This method returns a new point in which each dimension is summed up. If the operands' numbers of dimensions do not match, the operand with the fewest dimensions is treated as if the "missing" dimensions are 0."""
		return self.__class__(itertools.starmap(operator.add, itertools.zip_longest(self, other, fillvalue = 0)))

	@classmethod
	def cartesian_product(cls, *args):
		"""This methods returns the Cartesian product of n number of points."""
		for product in itertools.product(*args):
			yield cls(product)

	def count(value):
		"""This method is inherited from a superclass but doesn't make sense for this class. The best way to remove it is to just overload it and raise a `NotImplementedError`."""
		raise NotImplementedError()

	def __ge__(self, other):
		"""This method is inherited from a superclass but doesn't make sense for this class. The best way to remove it is to just overload it and raise a `NotImplementedError`."""
		raise NotImplementedError()

	def __gt__(self, other):
		"""This method is inherited from a superclass but doesn't make sense for this class. The best way to remove it is to just overload it and raise a `NotImplementedError`."""
		raise NotImplementedError()

	def index(index):
		"""This method is inherited from a superclass but doesn't make sense for this class. The best way to remove it is to just overload it and raise a `NotImplementedError`."""
		raise NotImplementedError()

	def __le__(self, other):
		"""This method is inherited from a superclass but doesn't make sense for this class. The best way to remove it is to just overload it and raise a `NotImplementedError`."""
		raise NotImplementedError()

	def __lt__(self, other):
		"""This method is inherited from a superclass but doesn't make sense for this class. The best way to remove it is to just overload it and raise a `NotImplementedError`."""
		raise NotImplementedError()

	def __mul__(self, other):
		"""This method is inherited from a superclass but doesn't make sense for this class. The best way to remove it is to just overload it and raise a `NotImplementedError`."""
		raise NotImplementedError()

	def __rmul__(self, other):
		"""This method is inherited from a superclass but doesn't make sense for this class. The best way to remove it is to just overload it and raise a `NotImplementedError`."""
		raise NotImplementedError()

	def __new__(cls, arg, *args):
		"""This method is called before `__init__` and handles formats the arguments into a manner in which `__init__` understands. There is no difference in the meaning between `arg` and `*args`. We just want to make sure the object has at least one dimension."""
		if isinstance(arg, (list, tuple)):
			return super(Point, cls).__new__(cls, arg)
		return super(Point, cls).__new__(cls, (arg,) + tuple(dimension for dimension in args))

	@property
	def numberOfDimensions(self):
		"""This method returns the number of dimensions specified in this point."""
		return len(self)

	def __repr__(self):
		"""This method returns a string representation of the initialization of an identical object."""
		return '%s(%s)' % (self.__class__.__name__, ', '.join(map(str, self)))

	def __radd__(self, other):
		"""This method returns a new point in which each dimension is summed up. If the operands' numbers of dimensions do not match, the operand with the fewest dimensions is treated as if the "missing" dimensions are 0."""
		return self.__class__(itertools.starmap(operator.add, itertools.zip_longest(self, other, fillvalue = 0)))

	def __rsub__(self, other):
		"""This method returns a new point in which the second operand's dimensions are subtracted from the first operand. If the operands' numbers of dimensions do not match, the operand with the fewest dimensions is treated as if the "missing" dimensions are 0."""
		return self.__class__(itertools.starmap(operator.sub, itertools.zip_longest(self, other, fillvalue = 0)))

	def __str__(self):
		"""This method returns a string representation of the object."""
		return '(' + ', '.join(map(str, self)) + ')'

	def __sub__(self, other):
		"""This method returns a new point in which the second operand's dimensions are subtracted from the first operand. If the operands' numbers of dimensions do not match, the operand with the fewest dimensions is treated as if the "missing" dimensions are 0."""
		return self.__class__(itertools.starmap(operator.sub, itertools.zip_longest(self, other, fillvalue = 0)))

	@property
	def x(self):
		"""This property is implemented simply for convenience and readability."""
		return self[0]

	@property
	def y(self):
		"""This property is implemented simply for convenience and readability."""
		return self[1]

	@property
	def z(self):
		"""This property is implemented simply for convenience and readability."""
		return self[2]