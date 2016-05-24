#!/bin/bash


cat /dev/null > file.txt
grep -A 2 "  def" "swagger_client/apis/apisautoscalingv_api.py" | sed 's/def//g' | sed 's/ //g' | sed 's/self, //g' | sed 's/**kwargs//g' | sed '/"""/d' | sed 's/self, //g' | sed 's/, ):/)/g' | sed 's/://g' | sed 's/,)/)/g' | sed -e '1,7d' | awk 'NR % 3 == 1 {sub(/^/,"`")} {print}' | awk 'NR % 3 == 1 {sub(/$/,"`")} {print}' | sed -e $'s/^/\\\n/g' >> file.txt


#grep -A 2 "  def" "swagger_client/apis/apiv_api.py" | sed 's/^/```/' | sed 's/$/```/' | sed 's/def//g' | sed 's/     //g' | sed 's/self, //g' | sed 's/**kwargs//g' | sed 's/, ):/)/g' | sed 's/://g' | sed '/"""/d' | while read -r line ; do
#    echo "$line"
#done

#sed 's/^/`/' | sed 's/$/`/' |
