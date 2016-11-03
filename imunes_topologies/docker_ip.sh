#!/bin/bash


for i in $(docker ps -aq); 
do
printf $i && docker exec $i ifconfig | grep 'inet addr:10' | awk '{print $2}'
done

