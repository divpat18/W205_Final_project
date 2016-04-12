for i in $@ 
do
        python transform_json.py $i
        echo $i
done
