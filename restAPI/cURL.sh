curl -i -X GET http://localhost:5000/api -o output.txt
sed '1!d' output.txt > http_responses_log.txt
awk '{print $2}' http_responses_log.txt > tmp1.txt
head tmp1.txt