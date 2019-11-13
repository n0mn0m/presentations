spark-submit --master local \
             --deploy-mode client \
             --driver-memory 12g \
             --driver-cores 2 \
             --executor-memory 12g \
             --executor-cores 2 \
             $1
