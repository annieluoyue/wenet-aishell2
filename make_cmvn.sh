project=aishell1_whisperaishell2
# 创建cmvn
train_config=./conf/train_conformer.yaml
tools/compute_cmvn_stats.py --num_workers 1 --train_config $train_config \
    --in_scp /data/wenet/examples/aishell/s1/utils/${project}/wav.scp \
    --out_cmvn /data/wenet/examples/aishell/s1/utils/${project}/global_cmvn
