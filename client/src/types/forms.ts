import type { LogTimestamp } from "./database";

export interface Form extends LogTimestamp {
  id: string;
  title: string;
  ownerId: string;
  customerTitle: string;
  description?: string;
}

export enum FormFielType {
  TEXT = "text",
  CHECKBOX = "checkbox",
  SELECT = "select",
  RADIO = "radio",
  TEXTAREA = "textarea",
  DATE = "date",
  NUMBER = "number",
}
export interface FormField {
  id: string;
  type: FormFielType; // e.g., "text", "checkbox", "select"
  /** Seen by user or customer */
  customerLabel: string;
  /** Label used  */
  label?: string;
  templateId?: string; // For template fields
  isRequired: boolean;
  options?: string[]; // For select, radio, checkbox
  placeholder?: string; // For text, textarea
  defaultValue?: string; // For text, textarea, number
  min?: number; // For number
  max?: number; // For number
  step?: number; // For number
}

export interface FormResponse extends Form {
  formId: string;
}

export interface FormResponseField extends FormField {
  formResponseId: string;
}
