export type VineError<T extends Record<string, any>> = {
  field: keyof T;
  message: string;
  rule: keyof T;
};

export type VineErrorResponse<T extends Record<string, any>> = {
  messages: VineError<T>[];
};
