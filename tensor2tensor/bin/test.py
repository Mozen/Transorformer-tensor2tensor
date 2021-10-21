
_PROBLEMS = {}
def register_problem(name=None):
  """Register a Problem. name defaults to cls name snake-cased."""

  def decorator(p_cls, registration_name=None):
    """Registers & returns p_cls with registration_name or default name."""
    p_name = registration_name
    
    _PROBLEMS[p_name] = p_cls
    p_cls.name = p_name
    return p_cls

  
  return lambda p_cls: decorator(p_cls, name)

a = register_problem('1111')
print(a('aaa'))