Config = {
    "model_path": "output",
    "train_data_path": "train_evaluate_data.csv",
    "valid_data_path": "valid_evaluate_data.csv",
    "vocab_path": "chars.txt",
    "model_type": "lstm",
    "max_length": 30,
    "hidden_size": 256,
    "kernel_size": 3,
    "num_layers": 2,
    "epoch": 15,
    "batch_size": 128,
    "pooling_style": "max",
    "optimizer": "adam",
    "learning_rate": 1e-3,
    "pretrain_model_path": r"../../week6/bert-base-chinese",
    "seed": 987,
    "class_num": 2
}
