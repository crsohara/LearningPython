import time

def getbytes():
	rx_bytes = open('/sys/class/net/eth0/statistics/rx_bytes', 'r')
	tx_bytes = open('/sys/class/net/eth0/statistics/tx_bytes','r')
	rx = float(rx_bytes.read().rstrip())
	tx = float(tx_bytes.read().rstrip())
	return (rx, tx)

while True:
	rx, tx = getbytes()
	time.sleep(1)
	rx2, tx2 = getbytes()
	print "DL: ",round((rx2-rx)/1048576, 2),"Mb/s\t UL: ",round((tx2-tx)/1048576,2),"Mb/s"