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
Source0: bw_web_¤RELEASE¤.tar.gz
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

%files
%defattr(0644, bitwarden, bitwarden, 0755)
%{service_homedir}/web

%changelog

