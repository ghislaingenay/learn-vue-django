export enum FormTemplateStatus {
  ACTIVE = "active",
  INACTIVE = "inactive",
  DELETED = "deleted",
}

export interface FormTemplate {
  id: number;
  name: string;
  description?: string;
  created_at: string; // ISO date string
  updated_at: string; // ISO date string
  user_id: number;
  deleted_at?: string; // ISO date string, optional
  status: FormTemplateStatus;
  fields: FormTemplateField[];
}

export enum FormFieldType {
  TEXT = "text",
  CHECKBOX = "checkbox",
  SELECT = "select",
  RADIO = "radio",
  TEXTAREA = "textarea",
  DATE = "date",
  NUMBER = "number",
}

export interface FormTemplateField {
  id: number;
  template: number; // Form Template ID
  field_name: string;
  required: boolean;
  is_active: boolean;
  deleted_at?: string; // ISO date string, optional
  options: { label: string; value: string }[]; // For select, radio, checkbox
  field_type: FormFieldType; // e.g., "text", "checkbox", "select"
  restrictions: any;
  default_value?: string;
}
