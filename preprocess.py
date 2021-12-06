import string

import pandas as pd

paths = ["train", "dev", "test"]
df_dict = {}

""" Combine the data and answers files into one file. (subtask A) """

for path in paths:
    taska_data_df = pd.read_csv(f"./OriginalDataset/{path}/subtaskA_data.csv")
    taska_answers_df = pd.read_csv(f"./OriginalDataset/{path}/subtaskA_answers.csv")
    # join the two files on id
    merged_df = taska_data_df.join(taska_answers_df.set_index("id"), on="id", how="inner")
    df_dict[path] = merged_df

# merge the dev data with the train data
taska_merged_train_df = df_dict.get("train").append(df_dict.get("dev"), ignore_index=True)
# save the processed data into csv files
taska_merged_train_df.to_csv("./ProcessedDataset/train/subtaskA.csv", index=False)
df_dict.get("test").to_csv("./ProcessedDataset/test/subtaskA.csv", index=False)

""" Combine the data and answers files into one file. (subtask B) """

for path in paths:
    taskb_data_df = pd.read_csv(f"./OriginalDataset/{path}/subtaskB_data.csv")
    taskb_answers_df = pd.read_csv(f"./OriginalDataset/{path}/subtaskB_answers.csv")
    # join the two files on id
    merged_df = taskb_data_df.join(taskb_answers_df.set_index("id"), on="id", how="inner")
    df_dict[path] = merged_df

# merge the dev data with the train data
df_dict["train"] = df_dict.get("train").append(df_dict.get("dev"), ignore_index=True)

""" Additional preprocessing for subtask B """

paths = ["train", "test"]

for path in paths:
    taskb_df = df_dict.get(path)
    taska_df = pd.read_csv(f"./ProcessedDataset/{path}/subtaskA.csv")
    # fetch the correct sentences from subtaskA data and include in subtaskB data
    dictionary = {0:"sent1", 1:"sent0"}
    correct_sents = [taska_df[dictionary.get(label)][index] for index, label in enumerate(taska_df["label"])]
    taskb_df["correct_sent"] = correct_sents
    # update the labels from alphabets to numbers
    mapping = {"A":0, "B":1, "C":2}
    taskb_df["label"] = [mapping.get(x) for x in taskb_df["label"]]
    # update the column names
    taskb_df.columns = ["id", "false_sent", "explanation0", "explanation1", "explanation2", "label", "correct_sent"]
    # reorder the columns
    taskb_df = taskb_df[["id", "false_sent", "correct_sent", "explanation0", "explanation1", "explanation2", "label"]]
    # save the processed data into csv file
    taskb_df.to_csv(f"./ProcessedDataset/{path}/subtaskB.csv", index=False)

