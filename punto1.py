from pyspark import SparkConf
from pyspark import SparkContext

HDFS_MASTER = 'HEAD_NODE_IP'

conf = SparkConf()
conf.setMaster('yarn-client')
conf.setAppName('spark-wordcount')
conf.set('spark.executor.instances', 10)
sc = SparkContext(conf=conf)
distFile = sc.textFile('hdfs://{0}:9000/tmp/enron/*/*.txt'.format(HDFS_MASTER))
nonempty_lines = distFile.filter(lambda x: len(x) > 0)
words = nonempty_lines.flatMap(lambda x: x.split(' '))
valid_words = words.filter(lambda x: x=="TRUMP" or x=="DICTATOR" or x=="MAGA" or x=="IMPEACH" or x=="DRAIN" or x=="SWAP" or x=="CHANGE")
result = valid_words.map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y)
