from collections import Iterable

from twitter.common.lang import Compatibility

from pkg_resources import Requirement


REQUIRED_ATTRIBUTES = (
    'extras',
    'key',
    'project_name',
    'specs',
)


def quacks_like_req(req):
  return all(hasattr(req, attr) for attr in REQUIRED_ATTRIBUTES)


def maybe_requirement(req):
  if isinstance(req, Requirement) or quacks_like_req(req):
    return req
  elif isinstance(req, Compatibility.string):
    return Requirement.parse(req)
  raise ValueError('Unknown requirement %r' % (req,))


def maybe_requirement_list(reqs):
  if isinstance(reqs, (Compatibility.string, Requirement)) or quacks_like_req(reqs):
    return [maybe_requirement(reqs)]
  elif isinstance(reqs, Iterable):
    return [maybe_requirement(req) for req in reqs]
  raise ValueError('Unknown requirement list %r' % (reqs,))
