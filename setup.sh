echo "Activating Virtual Environment..."
if test -f ../global_venv/bin/activate;
then 
source ../global_venv/bin/activate
echo "Virtual Environment Activation Succeed!"
else
virtualenv ../global_venv
source ../global_venv/bin/activate
fi
pip3 install -r requirements.txt
echo "Starting the system..."
clear
python3 startup_script.py
echo "Exiting..."