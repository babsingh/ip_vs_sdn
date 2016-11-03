#!/bin/bash


for i in $(docker ps -aq); 
do
echo $i && docker exec $i ifconfig | grep 'inet addr:10' 
done

