d=`date +%d.%m.%Y_%H.%M`
unbuffer toxsocks python sod.py | tee -a ./report/sod.$d
#toxsocks python sod.py | tee -a ./report/sod.$d
#|tee -a ./report/sod.$d
