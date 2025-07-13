class CreateFormTemplateDto:
  name: str
  description: str = None
  can_respond: bool = True
  can_use_multiple_times: bool = True
  is_active: bool = True
  deleted_at: str = None  # Soft delete
  fields: list = []  # List of field definitions for the form template
  created_at: str = None  # Automatically set to current time
  updated_at: str = None  # Automatically set to current time
