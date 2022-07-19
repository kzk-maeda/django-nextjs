import os

def validate_file_extension(name: str) -> bool:
  isValid = True

  ext = os.path.splitext(name)[1] # ('image', '.pdf)
  valid_extentions = ['.pdf', '.png']

  if not ext.lower() in valid_extentions:
    isValid = False
  
  return isValid