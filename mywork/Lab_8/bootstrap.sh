apt update -y
apt upgrade -y

apt install -y python3
apt install -y git
apt install -y nginx

systemctl start nginx
systemctl enable nginx