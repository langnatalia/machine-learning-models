// types.ts

export enum ModelType {
  LINEAR_REGRESSION = 'linear_regression',
  DECISION_TREE = 'decision_tree',
  RANDOM_FOREST = 'random_forest',
  NEURAL_NETWORK = 'neural_network',
}

export enum DataType {
  NUMERIC = 'numeric',
  CATEGORICAL = 'categorical',
  TEXT = 'text',
}

export type ModelParams = {
  model_type: ModelType;
  hyperparameters: {
    [key: string]: any;
  };
};

export type TrainingData = {
  X: any[][];
  y: any[];
  data_type: DataType;
};

export type EvaluationMetrics = {
  accuracy: number;
  precision: number;
  recall: number;
  f1_score: number;
  mean_squared_error: number;
};