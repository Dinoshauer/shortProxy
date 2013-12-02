import string
import random
from redis import StrictRedis

__REDIS_HOST__ = 'localhost'
__REDIS_PORT__ = 6379

class ShortProxy:
	def __init__(self):
		self.r = StrictRedis(__REDIS_HOST__, __REDIS_PORT__)

	def redirect_to(self, inputurl, data):
		self.r.rpush('l_{}'.format(inputurl), data)
		return self.r.get(inputurl)

	def generate_url(self, origin, target):
		return self.r.set('{}{}'.format(origin, self._randomString()), target)

	def _randomString(self, size=6, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for x in xrange(size))
