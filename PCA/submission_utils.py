import pandas as pd
import sklearn.metrics
import numpy as np


def write_submission_csv(prediction_df, filename):
    """Take a dataframe of predictions in the same form as data.labels_df and
    write a submission csv"""

    print("Shape of prediction_df: %s" % str(prediction_df.shape))
    clipnames = sorted(prediction_df.index.values)

    submission = "ID,Probability\n"
    for clipname in clipnames:
        for call_id in sorted(prediction_df.columns.values):
            # 'DataFrame' object has no attribute 'ix'
            # submission += "%s_classnumber_%s,%f\n" % (clipname, call_id, prediction_df.ix[clipname, call_id])
            submission += "%s_classnumber_%s,%f\n" % (clipname, call_id, prediction_df.loc[clipname, call_id])

    with open(filename, 'w') as f:
        f.write(submission)


    # # print("Shape of prediction_df: %s" % str(prediction_df.shape))
    # clipnames = sorted(prediction_df.index.values)

    # f = open("result.csv", "w")

    # submission = "ID,Probability\n"
    # for clipname in clipnames:
    #     # for call_id in sorted(prediction_df.columns.values):
    #     #     # 'DataFrame' object has no attribute 'ix'
    #     #     # submission += "%s_classnumber_%s,%f\n" % (clipname, call_id, prediction_df.ix[clipname, call_id])
    #     #     submission += "%s_classnumber_%s,%f\n" % (clipname, call_id, prediction_df.loc[clipname, call_id])

    #     maxscore = prediction_df.loc[clipname].max()
    #     maxid = prediction_df.loc[clipname].argmax()
    #     print("Clipname: %s\tClass: %d\tMaxscore: %f" % (clipname, maxid+1, maxscore))
    #     f.write("Clipname: %s\tClass: %d\tMaxscore: %f\n" % (clipname, maxid+1, maxscore))


def parse_submission_csv(filename):

    df = pd.read_csv(filename)
    df['filename'] = df.ID.map(lambda x: x.split('.')[0] + '.wav')
    df['call_id'] = df.ID.map(lambda x: int(x.split('.')[1].split('_')[-1]))
    return df.pivot(index='filename', values='Probability', columns='call_id')


def evaluate(prediction_df, truth_df):

    return sklearn.metrics.roc_auc_score(truth_df.values.ravel(), prediction_df.values.ravel())


def normalized_even_blend(pred_dfs, fold):
    # Shape of prediction_df: (48, 87)
    # return np.sum([df/df.mean().mean() for df in pred_dfs]) / len(pred_dfs)

    pred_dfs_values = np.array([pred_df.values for pred_df in pred_dfs])
    print(pred_dfs_values.shape)
    pred_dfs_sum = np.sum(pred_dfs_values, axis=2)
    print(pred_dfs_sum.shape)
    pred_dfs_norm = pred_dfs_values / pred_dfs_sum[:,:,np.newaxis]
    print(pred_dfs_norm.shape)

    pred_dfs_mean = np.mean(pred_dfs_norm, axis=0)
    print(pred_dfs_mean.shape)

    pred_values = pred_dfs_mean

    return pd.DataFrame(pred_values, index=fold.clipnames, columns=fold.call_ids)