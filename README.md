### bitwarden_rs RPM Packages ###

**Installation**

Install and start mariadb:
```
yum install mariadb-server
systemctl start mariadb
systemctl enable mariadb
```

Secure mariadb installation:
```
mysql_secure_installation
```

Add repository:
```
curl -o /etc/yum.repos.d/mrmeee-bitwarden_rs-epel-7.repo https://copr.fedorainfracloud.org/coprs/mrmeee/bitwarden_rs/repo/epel-7/mrmeee-bitwarden_rs-epel-7.repo
```

Temporary fix for wrong path, will be fixed in next release:
```
sed -i 's$/opt/bitwarden-rs$/opt/bitwarden_rs$g' /etc/bitwarden_rs/bitwarden-rs.conf
```

In /etc/bitwarden_rs/bitwarden-rs.conf (what I use besides of the standard):
```
DATABASE_URL="mysql://root:*********@localhost/bitwarden"
SIGNUPS_ALLOWED=false
ADMIN_TOKEN=*********************************************************
INVITATIONS_ALLOWED=true
DOMAIN=https://bitwarden.mrmeee.dk
SMTP_HOST=localhost
SMTP_FROM=bitwarden@mrmeee.dk
SMTP_FROM_NAME=Bitwarden_RS Secure Vault
SMTP_PORT=25
SMTP_SSL=false

```
