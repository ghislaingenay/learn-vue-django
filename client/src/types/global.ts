export type VineError = {
  field: string;
  message: string;
};

export type VineErrorResponse = {
  hasErrors: boolean;
  errors: VineError[];
};
