wavscp=/data/aishell2/eval-dataset/wavscp
text=/data/aishell2/eval-dataset/trans
result=/data/aishell2/eval-dataset/datalist

#data.list
  tools/make_raw_list.py $wavscp/2019_wav.scp $text/2019_trans.txt \
	$result/2019_data.list  
#/home/luo/hungarian-asr/data/prefile/${project}/wav.scp /home/luo/hungarian-asr/data/prefile/${project}/text \
       # /home/luo/hungarian-asr/data/prefile/${project}/data.list

