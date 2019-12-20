import os.path
import re
paths = [
    "/home/",
    "/../",
    "/home//foo/",
    "/a/./b/../../c/",
    "/a/../../b/../c//.//",
    "/ad//bd////cd/da//././/..",
    "/.././em/jl///../.././../E/"
]

# path = paths[-]


def simplifyPath(path: str) -> str:

  path += '/'

  while '//' in path:
    path = path.replace('//', '/')
  while '/./' in path:
    path = path.replace('/./', '/')

  while '/../' in path[1:]:
    path = re.sub(r'([^/]+)/\.\./', '', path, 1)

  path = path.replace('/../', '/')

  if len(path) > 1:
    path = path[:-1]

  return path


for path in paths:
  print(simplifyPath(path))
  print(os.path.normpath(path))
