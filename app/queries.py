from app.models import User
from ariadne import convert_kwargs_to_snake_case

def resolve_users(obj, info):
  try:
    users = [user.to_dict() for user in User.query.all()]
    payload = {
      "success": True,
      "users": users
    }
  except Exception as e:
    payload = {
      "success": False,
      "errors": [str(e)]
    }
  #
  return payload
  
def resolve_user(obj, info, id):
  pass