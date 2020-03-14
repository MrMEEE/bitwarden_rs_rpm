%define  debug_package %{nil}
%global __os_install_post %{nil}

%define service_user bitwarden
%define service_group bitwarden
%define service_homedir /opt/bitwarden_rs
%define service_logdir /var/log/bitwarden_rs
%define service_configdir /etc/bitwarden_rs

Summary: Bitwarden Rust Edition Web Interface
Name: bitwarden_rs_web
Version: ¤VERSION¤
Release: 1%{dist}
Source0: bw_web_%{version}.tar.gz
License: GPLv3
Group: System Tools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
AutoReqProv: false
Requires: bitwarden_rs_web

%description
%{summary}

%prep

%install
mkdir -p $RPM_BUILD_ROOT%{service_homedir}/web

tar zxvf %{SOURCE0} -C $RPM_BUILD_ROOT%{service_homedir}/web

%clean

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}

%files
%defattr(0644, bitwarden, bitwarden, 0755)
%{service_homedir}/web

%changelog
* Sat Mar 14 2020 04:01:13 +0000 Martin Juhl <mj@casalogic.dk> v2.12.0e
- New version build: v2.12.0e
* Fri Sep 27 2019 07:58:54 +0000 Martin Juhl <mj@casalogic.dk> v2.12.0
- New version build: v2.12.0
* Wed Sep 04 2019 21:08:51 +0000 Martin Juhl <mj@casalogic.dk> v2.11.0b
- New version build: v2.11.0b
* Wed Jul 31 2019 03:02:43 +0000 Martin Juhl <mj@casalogic.dk> v2.11.0
- New version build: v2.11.0
* Wed Jul 17 2019 20:58:48 +0000 Martin Juhl <mj@casalogic.dk> v2.10.1
* Wed Jul 17 2019 20:54:07 +0000 Martin Juhl <mj@casalogic.dk> v2.10.1
* Wed Jul 17 2019 14:00:03 +0000 Martin Juhl <mj@casalogic.dk> v2.10.1
* Wed Jul 17 2019 13:53:55 +0000 Martin Juhl <mj@casalogic.dk> v2.10.1
- New version build: v2.10.1

