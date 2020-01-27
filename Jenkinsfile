#make sure prerequisites are satisfied
sudo apt update
sudo apt install -y python3
sudo apt install -y python3-venv
sudo apt install -y python3-pip
# install the service script
sudo cp flask-app.service /etc/systemd/system/
# reload the service scripts
sudo systemctl daemon-reload
# stop the old service
sudo systemctl stop flask-app
# install the application files
install_dir=/opt/flask-app
sudo rm -rf ${install_dir}
sudo mkdir ${install_dir}
sudo cp -r ./* ${install_dir}
sudo chown -R pythonadm:pythonadm ${install_dir}
# configure python virtual environment and install dependencies
sudo su - pythonadm << EOF
cd ${install_dir}
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
EOF
# start the flask app
sudo systemctl start flask-app
