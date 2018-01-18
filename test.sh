curl -i -X GET http://localhost:5000/api -o output.txt
sed '1!d' output.txt > http_responses_log.txt
var=$1
awk '{print $2}' http_responses_log.txt > $var
head $var
