from pyspark import SparkConf
from pyspark import SparkContext
import json
HDFS_MASTER = 'HEAD_NODE_IP'
def mapJSON(line):
    obj = json.loads(line)
    return (obj["user"]["id"],1)
conf = SparkConf()
conf.setMaster('yarn-client')
conf.setAppName('spark-wordcount')
conf.set('spark.executor.instances', 10)
sc = SparkContext(conf=conf)
distFile = sc.textFile('hdfs://{0}:9000/tmp/enron/*/*.txt'.format(HDFS_MASTER))
nonempty_lines = distFile.filter(lambda x: len(x) > 0)
text = nonempty_lines.map(lambda line: mapJSON(line)).reduceByKey(lambda x,y: x+y)
