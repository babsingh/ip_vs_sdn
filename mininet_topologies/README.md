# mininet_topologies


##To reproduce each topology (single, linear, tree), run the python script on each folder
###i.e $sudo python /mininet_topologies/single/single_s1h2.py

##To start POX controller run the following command:
####&nbsp;&nbsp;&nbsp;&nbsp;$sudo ./pox/pox.py forwarding.l2_learning

##To run an iPerf test between the hosts, open an xterm:
####&nbsp;&nbsp;&nbsp;&nbsp;mininet> xterm h1 h2

##Run these commands on each host the following:

####&nbsp;&nbsp;&nbsp;&nbsp;h2(Server)iperf -s -p 5566 -i 1 > results_single_s1h2

####&nbsp;&nbsp;&nbsp;&nbsp;h1(Client)iperf -c 10.0.0.2 -p 5566 -t 15

###&nbsp;&nbsp;&nbsp;-s = server; -p= port; -i= interval; -c= client ip; -t= test duration

##To run a Ping test to measure RTT run the following command:

####&nbsp;&nbsp;&nbsp;&nbsp;mininet> h1 ping -c 30 h2 > ping_single_s1h2

##Files ending with extension .mn can be used to get the graphical topology on Miniedit

