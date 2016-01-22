from .version import *
# just importing does the work
import monkeyPatch


def acceptArgs(argList):
    def decorator(fn):
        @wraps(fn)
        def taskFn(*args,**kwargs):
            needed=[]
            argsIndex=0
            # figure out which arguments we've been provided with
            for a in argList:
                if a['name'] not in kwargs:
                    if argsIndex>=len(args):
                        needed.append(a)
                    else:
                        argsIndex+=1

            # request the rest
            for n in needed:
                kwargs[n['name']]=raw_input('Enter a value for "{}" ({}): '.format(n['name'],n['type']))

            return fn(*args,**kwargs)
        return taskFn
    return decorator

# @acceptArgs([{'name':'environment','type':'string',},{'name':'scriptName','type':'string'}])
